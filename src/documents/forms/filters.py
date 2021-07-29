from collections import OrderedDict

from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class BaseDocumentFilterForm(forms.Form):
    """Base form for filtering documents of any type."""

    size = forms.IntegerField(
        widget=forms.HiddenInput(), required=False, initial=settings.PAGINATE_BY
    )
    start = forms.IntegerField(widget=forms.HiddenInput(), required=False, initial=0)
    search_terms = forms.CharField(label="Search all columns", required=False)


# Additional fields that could be needed, e.g for filter fields that are
# not model fields.
# TODO Find a better way to do this.
additional_filter_fields = {
    "overdue": forms.ChoiceField(
        choices=(("", "---------"), ("true", "Yes"), ("false", "No")),
        required=False,
        widget=forms.Select,
        label=_("Overdue"),
    ),
    "under_review": forms.ChoiceField(
        choices=(("", "---------"), ("true", "Yes"), ("false", "No")),
        required=False,
        widget=forms.Select,
        label=_("Under review"),
    ),
    "ack_of_receipt": forms.ChoiceField(
        choices=(("", "---------"), ("true", "Yes"), ("false", "No")),
        required=False,
        widget=forms.Select,
        label=_("Acknowledgment of receipt"),
    ),
}


def filterform_factory(model):
    """Dynamically create a filter form for the given Metadata model.

    Filter fields can be either located in the Metadata class, or in the
    corresponding Revision class.

    """
    revision_model = model.latest_revision.get_queryset().model
    all_fields = dict(
        (field.name, field)
        for field in (
            model._meta.concrete_fields + revision_model._meta.concrete_fields
        )
    )
    # Get the list of all configured fields
    config = getattr(model, "PhaseConfig")
    field_list = []
    kwargs = {"required": False}

    # Add all field filters to form
    filter_fields = config.filter_fields

    # Get the optional `filter_fields_order` in PhaseConfig
    filter_fields_order = getattr(config, "filter_fields_order", None)

    for field_name in filter_fields:
        if field_name in all_fields:
            f = all_fields[field_name]

            # Create form field from model field
            # TODO Include indexes in choices
            field = f.formfield(**kwargs)
            field.required = False
            field.empty_value = None
            field.initial = ""
            field.choices = f.get_choices(include_blank=True)
            field_list.append((f.name, field))
        else:
            field = additional_filter_fields[field_name]
            field_list.append((field_name, field))

    # Add custom filters to filter form
    custom_filters = getattr(config, "custom_filters", {})
    for field_name, filter_config in list(custom_filters.items()):
        field_kwargs = filter_config.get("field_kwargs", {})
        field_kwargs.update(kwargs)
        field = filter_config["field"](**field_kwargs)
        field.required = False
        field.label = filter_config["label"]
        field_list.append((field_name, field))
    field_list.append(
        (
            "sort_by",
            forms.CharField(
                widget=forms.HiddenInput(),
                required=False,
                initial=model._meta.ordering[0],
            ),
        )
    )
    class_name = model.__name__ + "FilterForm"
    field_dict = OrderedDict(field_list)

    form = type(class_name, (BaseDocumentFilterForm,), field_dict)

    if filter_fields_order:
        # We need to modify `base_fields` to get the wanted order
        # Trick used in django admin:
        # https://github.com/django/django/blob/1.8/django/contrib/auth/forms.py#L318

        # These hidden fields belong to `BaseDocumentFilterForm` or are added
        # above.
        # We have to add them to the `base_fields` by appending them to the
        # `filter_fields_order` list manually.
        # TODO Find a better way to do this.
        fields_order = ["size", "start"] + filter_fields_order
        form.base_fields = OrderedDict((k, form.base_fields[k]) for k in fields_order)
    return form
