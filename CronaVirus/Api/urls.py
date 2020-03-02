from django.urls import path, include
from . import views

# ListAPIView
urlpatterns = [
    path('cronavirues/overall/', views.CronaView.as_view()),
    path('cronavirues/area/', views.AreaView.as_view()),
    path('cronavirues/news/', views.NewsView.as_view()),
    path('cronavirues/rumors/', views.RemourView.as_view()),

]
