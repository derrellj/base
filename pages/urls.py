from django.urls import path
from .views import PageListView

app_name = "pages"


urlpatterns = [
    path("", PageListView.as_view(), name="home"),
]
