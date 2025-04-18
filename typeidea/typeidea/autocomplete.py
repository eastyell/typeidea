from dal import autocomplete

from blog.models import Category, Tag


class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # if not self.has_add_permission(self.request):
        #     return Category.objects.none()
        qs = Category.objects.filter(owner=self.request.user)
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs


class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # if not self.has_add_permission(self.request):
        #     return Tag.objects.none()
        qs = Tag.objects.filter(owner=self.request.user)
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs
