import re

from django.db import models, transaction
from django.utils import timezone
from django.utils.translation import ugettext, ugettext_lazy as _
from django.conf import settings

from accounts.models import User
from documents.models import Document
from notifications.models import notify


mentions_re = re.compile(r"@([\w\-_]+)", re.IGNORECASE)


class Note(models.Model):
    """A single message in a discussion thread.

    Discussion threads are for a single revision under review,
    and limited to the member of the distribution list.

    """

    document = models.ForeignKey(
        Document, on_delete=models.PROTECT, verbose_name=_("Document")
    )
    revision = models.PositiveIntegerField(_("Revision"))
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name=_("Author")
    )
    body = models.TextField(_("Body"))
    created_on = models.DateTimeField(_("Created on"), default=timezone.now)
    deleted_on = models.DateTimeField(_("Deleted on"), null=True, blank=True)

    class Meta:
        verbose_name = _("Note")
        verbose_name_plural = _("Notes")
        app_label = "discussion"

    def soft_delete(self):
        """Mark object as deleted, but keep in db.

        Discussion items should no be really deleted, as it could cause
        confusion and change the meaning of existing discussion threads.

        Instead, we just mark the item as deleted, and show an empty message.

        """
        message = ugettext("Deleted")
        self.body = message
        self.deleted_on = timezone.now()

    @transaction.atomic
    def notify_mentionned_users(self):
        """Parse @mentions and create according notifications."""
        message = _(
            "%(user)s mentionned you on document "
            '<a href="%(url)s">%(doc)s</a> (revision %(revision)02d)'
        ) % {
            "user": self.author.name,
            "url": self.document.get_absolute_url(),
            "doc": self.document.document_key,
            "revision": int(self.revision),
        }
        users = self.parse_mentions()
        for user in users:
            notify(user, message)

    def parse_mentions(self):
        """Get the list of all users mentionned in the message."""
        usernames = mentions_re.findall(self.body)
        if len(usernames) > 0:
            users = User.objects.filter(username__in=usernames)
        else:
            users = []
        return list(users)
