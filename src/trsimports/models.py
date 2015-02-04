# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os

from trsimports.validation import TrsValidator


class TrsImport(object):
    """A transmittals import encapsulation."""

    def __init__(self, trs_dir, tobechecked_dir, accepted_dir, rejected_dir):
        self.trs_dir = trs_dir
        self.tobechecked_dir = tobechecked_dir
        self.accepted_dir = accepted_dir
        self.rejected_dir = rejected_dir

        self._errors = None

    def do_import(self):
        pass

    def is_valid(self):
        return not bool(self.errors)

    @property
    def basename(self):
        return os.path.basename(self.trs_dir)

    @property
    def errors(self):
        if self._errors is None:
            self.validate()
        return self._errors

    def validate(self):
        """Performs a full automatic validation of the transmittals."""
        validator = TrsValidator()
        self._errors = validator.validate(self)
