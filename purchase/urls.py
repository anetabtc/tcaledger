from django.urls import include, path
#from rest_framework import routers
from . import views
from .views import OrderViews
#router = routers.DefaultRouter()
#router.register(r'orders', views.OrderViewSet)

app_name = 'purchase'
urlpatterns = [
    path('page1/result/', OrderViews.as_view()),
    path('page1/result/<int:id>', OrderViews.as_view()),
    #path('page1/result/', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.IndexView.as_view(), name='index'),
    path('page1/', views.Page1.as_view(), name='page1'),
    path('page2/', views.page2, name='page2'),
    path('page3/', views.Page3.as_view(), name='page3'),
]
