from django.urls import reverse

from restapi.widgets import AutocompleteTextInput


class BaseUserAutocomplete(AutocompleteTextInput):
    def set_category(self, category):
        self.attrs.update(
            {
                "data-value-field": "id",
                "data-label-field": "name",
                "data-search-fields": '["name"]',
                "data-url": reverse(
                    "user-list",
                    args=[category.organisation.slug, category.category_template.slug],
                ),
            }
        )


class UserAutocomplete(BaseUserAutocomplete):
    def set_category(self, category):
        super(UserAutocomplete, self).set_category(category)
        self.attrs.update(
            {
                "data-mode": "single",
            }
        )

    def render(self, name, value, attrs=None, renderer=None):
        if value:
            obj = self.choices.queryset.get(pk=value)
            attrs.update(
                {
                    "data-initial-id": value,
                    "data-initial-label": str(obj),
                }
            )
        else:
            attrs.update(
                {
                    "data-initial-id": "",
                    "data-initial-label": "",
                }
            )
        return super(AutocompleteTextInput, self).render(name, value, attrs, renderer)


class MultipleUserAutocomplete(BaseUserAutocomplete):
    def set_category(self, category):
        super(MultipleUserAutocomplete, self).set_category(category)
        self.attrs.update(
            {
                "data-mode": "multi",
            }
        )

    def render(self, name, value, attrs=None, renderer=None):
        value = value or []
        objects = self.choices.queryset.filter(pk__in=value).values_list("id", "name")
        attrs.update(
            {
                "data-initial-id": "[%s]" % ",".join(str(obj[0]) for obj in objects),
                "data-initial-label": "[%s]"
                % ",".join('"%s"' % obj[1] for obj in objects),
            }
        )
        return super(AutocompleteTextInput, self).render(name, value, attrs, renderer)
