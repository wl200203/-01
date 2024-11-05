from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('Post', views.BlogImages)

urlpatterns = [
    path('api_root/', include(router.urls)),
]



