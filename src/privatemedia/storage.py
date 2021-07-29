from django.core.files.storage import FileSystemStorage
from django.utils.deconstruct import deconstructible
from django.conf import settings


@deconstructible
class ProtectedStorage(FileSystemStorage):
    def __init__(self, *args, **kwargs):
        kwargs.update(
            {
                "location": "{}".format(settings.PROTECTED_ROOT),
                "base_url": "{}".format(settings.PROTECTED_URL),
            }
        )
        super(ProtectedStorage, self).__init__(*args, **kwargs)
        self.xaccel_prefix = settings.PROTECTED_X_ACCEL_PREFIX


@deconstructible
class PrivateStorage(FileSystemStorage):
    def __init__(self, *args, **kwargs):
        kwargs.update(
            {
                "location": "{}".format(settings.PRIVATE_ROOT),
                "base_url": "{}".format(settings.PRIVATE_URL),
            }
        )
        super(PrivateStorage, self).__init__(*args, **kwargs)
        self.xaccel_prefix = settings.PRIVATE_X_ACCEL_PREFIX

    def get_available_name(self, name, max_length=None):
        u"""Erase existing file before proceeding."""

        # The `delete` methods takes care of checking if the file already
        # exists before deletion.
        self.delete(name)
        return super().get_available_name(name, max_length)


# We had to override `FileSystemStorage` instead of just instanciating it
# with the correct parameters because those parameters were ending up in
# the migrations file, with paths that only existed on the machine that
# generated the migration.
protected_storage = ProtectedStorage()
private_storage = PrivateStorage()
