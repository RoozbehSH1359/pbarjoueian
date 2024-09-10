from django.urls import path
from .views import HomePageView,AboutPageView,basePageView
urlpatterns = [
    
    path("about/",AboutPageView.as_view(),name="about"),
    path("",HomePageView.as_view(),name="home"),
    path("base/",basePageView.as_view(),name="base"),
]
