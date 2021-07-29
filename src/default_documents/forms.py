from django.utils.translation import ugettext_lazy as _

from crispy_forms.layout import Layout, Field

from documents.forms.models import BaseDocumentForm
from .models import (
    ContractorDeliverable,
    ContractorDeliverableRevision,
    Correspondence,
    CorrespondenceRevision,
    MinutesOfMeeting,
    MinutesOfMeetingRevision,
    DemoMetadata,
    DemoMetadataRevision,
    GtgMetadata,
    GtgMetadataRevision,
)
from transmittals.forms import TransmittableFormMixin
from .layout import (
    DocumentFieldset,
    ScheduleLayout,
    ScheduleStatusLayout,
    PropertyLayout,
    DateField,
)


class ContractorDeliverableForm(BaseDocumentForm):
    def build_layout(self):
        return Layout(
            DocumentFieldset(
                _("General information"),
                Field("document_key", type="hidden"),
                "document_number",
                Field("title", rows=2),
                "contract_number",
                "originator",
                "unit",
                "discipline",
                "document_type",
                "sequential_number",
                "system",
                "wbs",
                "weight",
            ),
            self.get_related_documents_layout(),
            DocumentFieldset(
                _("Schedule"),
                ScheduleLayout(
                    ScheduleStatusLayout("std"),
                    ScheduleStatusLayout("idc"),
                    ScheduleStatusLayout("ifr"),
                    ScheduleStatusLayout("ifa"),
                    ScheduleStatusLayout("ifd"),
                    ScheduleStatusLayout("ifc"),
                    ScheduleStatusLayout("ifi"),
                    ScheduleStatusLayout("asb"),
                ),
            ),
        )

    class Meta:
        model = ContractorDeliverable
        exclude = ("document", "latest_revision")


class ContractorDeliverableRevisionForm(TransmittableFormMixin, BaseDocumentForm):
    def build_layout(self):
        return Layout(
            DocumentFieldset(
                _("Revision"),
                DateField("revision_date"),
                Field("created_on", readonly="readonly"),
                "docclass",
                "status",
                "final_revision",
                "native_file",
                "pdf_file",
            ),
            *(self.get_review_layout() + self.get_trs_layout())
        )

    class Meta:
        model = ContractorDeliverableRevision
        exclude = (
            "metadata",
            "revision",
            "updated_on",
            "review_end_date",
            "reviewers_step_closed",
            "leader_step_closed",
            "transmittal",
            "transmittals",
        )


class CorrespondenceForm(BaseDocumentForm):
    def build_layout(self):
        return Layout(
            DocumentFieldset(
                _("General information"),
                Field("document_key", type="hidden"),
                "document_number",
                Field("subject", rows=2),
                DateField("correspondence_date"),
                DateField("received_sent_date"),
                "contract_number",
                "originator",
                "recipient",
                "document_type",
                "sequential_number",
                "author",
                "addresses",
                "response_required",
                DateField("due_date"),
                "external_reference",
                self.get_related_documents_layout(),
            )
        )

    class Meta:
        model = Correspondence
        exclude = ("document", "latest_revision")


class CorrespondenceRevisionForm(BaseDocumentForm):
    def build_layout(self):
        return Layout(
            DocumentFieldset(
                _("Revision"),
                DateField("revision_date"),
                Field("created_on", readonly="readonly"),
                "status",
                "native_file",
                "pdf_file",
            ),
            DocumentFieldset(
                _("Review"),
                DateField("received_date"),
                "under_review",
                "overdue",
                "leader",
            ),
        )

    class Meta:
        model = CorrespondenceRevision
        exclude = ("metadata", "revision", "updated_on")


class MinutesOfMeetingForm(BaseDocumentForm):
    def build_layout(self):
        response_reference = DocumentFieldset(
            _("Response reference"),
            "response_reference",
        )

        return Layout(
            DocumentFieldset(
                _("General information"),
                Field("document_key", type="hidden"),
                "document_number",
                Field("subject", rows=2),
                DateField("meeting_date"),
                DateField("received_sent_date"),
                "contract_number",
                "originator",
                "recipient",
                "document_type",
                "sequential_number",
                "prepared_by",
                "signed",
                response_reference,
            )
        )

    class Meta:
        model = MinutesOfMeeting
        exclude = ("document", "latest_revision")


class MinutesOfMeetingRevisionForm(BaseDocumentForm):
    def build_layout(self):
        return Layout(
            DocumentFieldset(
                _("Revision"),
                DateField("revision_date"),
                Field("created_on", readonly="readonly"),
                "status",
                "native_file",
                "pdf_file",
            ),
            DocumentFieldset(
                _("Review"),
                DateField("received_date"),
            ),
        )

    class Meta:
        model = MinutesOfMeetingRevision
        exclude = ("metadata", "revision", "updated_on")


class DemoMetadataForm(BaseDocumentForm):
    class Meta:
        model = DemoMetadata
        exclude = ("document", "latest_revision")

    def build_layout(self):
        return Layout(
            DocumentFieldset(
                _("General information"),
                Field("document_key", type="hidden"),
                "document_number",
                Field("title", rows=2),
                self.get_related_documents_layout(),
            )
        )


class DemoMetadataRevisionForm(BaseDocumentForm):
    class Meta:
        model = DemoMetadataRevision
        exclude = ("metadata", "revision", "updated_on")

    def build_layout(self):
        return Layout(
            DocumentFieldset(
                _("Revision"),
                DateField("revision_date"),
                Field("created_on", readonly="readonly"),
                "status",
                "native_file",
                "pdf_file",
            ),
            DocumentFieldset(
                _("Review"),
                DateField("received_date"),
                Field("review_start_date", readonly="readonly"),
                Field("review_due_date", readonly="readonly"),
                PropertyLayout("is_under_review"),
                PropertyLayout("is_overdue"),
                "reviewers",
                "leader",
                "approver",
            ),
        )


class GtgMetadataForm(BaseDocumentForm):
    class Meta:
        model = GtgMetadata
        exclude = ("document", "latest_revision")

    def build_layout(self):
        return Layout(
            DocumentFieldset(
                _("General information"),
                Field("document_key", type="hidden"),
                "document_number",
                Field("title", rows=2),
                "originator",
                "unit",
                "discipline",
                "document_type",
            ),
            self.get_related_documents_layout(),
            DocumentFieldset(
                _("Schedule"),
                ScheduleLayout(
                    ScheduleStatusLayout("ifr"),
                    ScheduleStatusLayout("ifa"),
                    ScheduleStatusLayout("ifi"),
                    ScheduleStatusLayout("ife"),
                    ScheduleStatusLayout("ifp"),
                    ScheduleStatusLayout("fin"),
                    ScheduleStatusLayout("asb"),
                ),
            ),
        )


class GtgMetadataRevisionForm(TransmittableFormMixin, BaseDocumentForm):
    def build_layout(self):
        return Layout(
            DocumentFieldset(
                _("Revision"),
                DateField("revision_date"),
                Field("created_on", readonly="readonly"),
                "docclass",
                "status",
                "final_revision",
                "native_file",
                "pdf_file",
            ),
            *(self.get_review_layout() + self.get_trs_layout())
        )

    class Meta:
        model = GtgMetadataRevision
        exclude = (
            "metadata",
            "revision",
            "updated_on",
            "review_end_date",
            "reviewers_step_closed",
            "leader_step_closed",
            "transmittal",
            "transmittals",
        )
