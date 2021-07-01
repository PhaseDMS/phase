from django.contrib.auth.models import AnonymousUser

from categories.models import Category


class CategoryMiddleware:
    """Add category data to every request."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = getattr(request, "user")
        if not isinstance(user, AnonymousUser):
            request.user_categories = (
                Category.objects.filter(users=user)
                .select_related("category_template", "organisation")
                .order_by("organisation__name", "category_template__name")
            )

        return self.get_response(request)
