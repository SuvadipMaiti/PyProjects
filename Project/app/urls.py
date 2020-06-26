from django.urls import path, include
from . import views
from .views import Another
from rest_framework import routers
from .views import BookViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('first',views.first),
    path('another', Another.as_view()),
    path('temp', views.temp),
    path('api/', include(router.urls))

]