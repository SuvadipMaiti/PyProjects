from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls import include
from .views import MovieViewSet,RatingViewSet


router = routers.DefaultRouter()
router.register('movies',MovieViewSet)
router.register('ratings',RatingViewSet)




urlpatterns = [
    path('',include(router.urls)),

]