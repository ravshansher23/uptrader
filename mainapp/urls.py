from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view(), name="main_page"),
    path("<slug:slug>/", views.Page1View.as_view(), name="news"),
    path("<slug:slug1>/<slug:slug>/", views.Page2View.as_view(), name="news_paginator"),
]
