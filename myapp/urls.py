from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'data',views.recuritorViewset, basename='data')
router.register(r'edu', views.recuritor_education, basename='education')



urlpatterns = [
   path('',include(router.urls)),

  
]