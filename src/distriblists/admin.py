from django.contrib import admin
from django.urls import path

from distriblists.models import DistributionList
from distriblists.forms import DistributionListForm
from distriblists.views import (
    DistributionListImport,
    DistributionListExport,
    ReviewMembersImport,
    ReviewMembersExport,
)


class DistributionListAdmin(admin.ModelAdmin):
    list_display = ("name",)
    filter_horizontal = ("reviewers", "categories")
    form = DistributionListForm

    def get_urls(self):
        urls = super(DistributionListAdmin, self).get_urls()
        return [
            path(
                "import/",
                self.admin_site.admin_view(
                    DistributionListImport.as_view(model_admin=self)
                ),
                name="distriblists_distriblist_import",
            ),
            path(
                "export/",
                self.admin_site.admin_view(
                    DistributionListExport.as_view(model_admin=self)
                ),
                name="distriblists_distriblist_export",
            ),
            path(
                "review_members_import/",
                self.admin_site.admin_view(
                    ReviewMembersImport.as_view(model_admin=self)
                ),
                name="distriblists_reviewmembers_import",
            ),
            path(
                "review_members_export/",
                self.admin_site.admin_view(
                    ReviewMembersExport.as_view(model_admin=self)
                ),
                name="distriblists_reviewmembers_export",
            ),
        ] + urls


admin.site.register(DistributionList, DistributionListAdmin)
