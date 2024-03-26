from django.views.generic import TemplateView


class PageListView(TemplateView):
    template_name = "pages.html"
    context_object_name = "page"
