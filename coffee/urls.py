from django.urls import path

from .views import CoffeeLatestView, CoffeeListView

app_name = "coffee"
urlpatterns = [
    path("now", CoffeeLatestView.as_view()),
    path("", CoffeeListView.as_view()),
]
