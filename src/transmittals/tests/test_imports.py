import os
from os.path import join
import tempfile
from shutil import rmtree, copytree

from django.test import TestCase
from django.contrib.contenttypes.models import ContentType

from documents.models import Document
from categories.factories import CategoryFactory
from transmittals.imports import TrsImport
from transmittals.models import Transmittal, TrsRevision


class TestImports(TestCase):
    fixtures = [
        "initial_categories",
        "initial_values_lists",
        "initial_accounts",
        "initial_documents",
        "initial_entities",
    ]

    def setUp(self):
        document = Document.objects.get(document_key="FAC10005-CTR-000-EXP-LAY-4891")
        self.doc_category = document.category

        trs_content_type = ContentType.objects.get_for_model(Transmittal)
        self.trs_category = CategoryFactory(
            category_template__metadata_model=trs_content_type
        )

        self.tmpdir = tempfile.mkdtemp(prefix="phasetest_", suffix="_trs")
        self.incoming = join(self.tmpdir, "incoming")
        self.tobechecked = join(self.tmpdir, "tobechecked")
        self.accepted = join(self.tmpdir, "accepted")
        self.rejected = join(self.tmpdir, "rejected")

        os.mkdir(self.accepted)
        os.mkdir(self.rejected)
        os.mkdir(self.tobechecked)

        self.config = {
            "INCOMING_DIR": self.incoming,
            "REJECTED_DIR": self.rejected,
            "TO_BE_CHECKED_DIR": self.tobechecked,
            "ACCEPTED_DIR": self.accepted,
            "EMAIL_LIST": ["test@phase.fr"],
        }

    def tearDown(self):
        if os.path.exists(self.tmpdir):
            rmtree(self.tmpdir)

    def prepare_fixtures(self, fixtures_dir, trs_dir):
        """Create the fixtures import dir."""
        src = os.path.join(os.path.dirname(__file__), "fixtures", fixtures_dir)
        dest = self.config["INCOMING_DIR"]
        copytree(src, dest)

        trs_fullname = join(self.config["INCOMING_DIR"], trs_dir)
        trs_import = TrsImport(
            trs_fullname,
            tobechecked_dir=self.config["TO_BE_CHECKED_DIR"],
            accepted_dir=self.config["ACCEPTED_DIR"],
            rejected_dir=self.config["REJECTED_DIR"],
            email_list=self.config["EMAIL_LIST"],
            contractor=fixtures_dir,
            doc_category=self.doc_category,
            trs_category=self.trs_category,
        )
        return trs_import

    def test_save_import_to_db(self):
        self.assertEqual(Transmittal.objects.all().count(), 0)
        self.assertEqual(TrsRevision.objects.all().count(), 0)

        trs_import = self.prepare_fixtures(
            "single_correct_trs", "FAC10005-CTR-CLT-TRS-00001"
        )
        self.assertTrue(trs_import.is_valid())
        trs_import.save()

        self.assertEqual(Transmittal.objects.all().count(), 1)
        self.assertEqual(TrsRevision.objects.all().count(), 4)

    def test_saved_transmittal_data(self):
        trs_import = self.prepare_fixtures(
            "single_correct_trs", "FAC10005-CTR-CLT-TRS-00001"
        )
        self.assertTrue(trs_import.is_valid())
        trs_import.save()

        transmittal = Transmittal.objects.all()[0]
        self.assertEqual(transmittal.document.category, self.trs_category)
        self.assertEqual(transmittal.contract_number, "FAC10005")
        self.assertEqual(transmittal.originator, "CTR")
        self.assertEqual(transmittal.recipient, "CLT")
        self.assertEqual(transmittal.sequential_number, 1)

    def test_saved_revision_data(self):
        trs_import = self.prepare_fixtures(
            "single_correct_trs", "FAC10005-CTR-CLT-TRS-00001"
        )
        self.assertTrue(trs_import.is_valid())
        trs_import.save()

        revision = TrsRevision.objects.order_by("revision").all()[0]
        self.assertEqual(revision.document_key, "FAC10005-CTR-000-EXP-LAY-4891")
        self.assertEqual(revision.originator.trigram, "CTR")
        self.assertEqual(revision.unit, "000")
        self.assertEqual(revision.discipline, "EXP")
        self.assertEqual(revision.document_type, "LAY")
        self.assertEqual(revision.sequential_number, "4891")
        self.assertEqual(revision.docclass, 1)
        self.assertEqual(revision.revision, 1)
        self.assertEqual(revision.status, "SPD")

    def test_new_or_updated_revisions(self):
        trs_import = self.prepare_fixtures(
            "single_correct_trs", "FAC10005-CTR-CLT-TRS-00001"
        )
        trs_import.save()

        updated_revisions = TrsRevision.objects.filter(is_new_revision=False)
        self.assertEqual(updated_revisions.count(), 2)

        new_revisions = TrsRevision.objects.filter(is_new_revision=True)
        self.assertEqual(new_revisions.count(), 2)
