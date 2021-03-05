from django.urls import path

from . import views

app_name = 'wiki'
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.Entry, name="title"),
    path("edit/", views.edit, name = "edit"),
    path("SearchPage/", views.SearchPage, name="search"),
    path("CreateNewPage/", views.CreatNewPage, name="newpage"),
	path("savePage/", views.savePage, name ="save"),
	path("randomPage/", views.randomPage, name="randomPage")
]
