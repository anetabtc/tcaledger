from django.urls import include, path
from . import views
from .views import OrderViews

app_name = 'paymentstatus'

urlpatterns = [
    path('page1/result/', OrderViews.as_view()),
    path('', views.IndexView.as_view(), name='index'),
]
