from django.urls import path

from .views import BrewListView, BrewTodayView

app_name = "brew"


urlpatterns = [path("today", BrewTodayView.as_view()), path("", BrewListView.as_view())]
