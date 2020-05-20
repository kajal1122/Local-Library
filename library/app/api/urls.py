
from django.urls import include,path
from .views import BookViewSet

from rest_framework import routers

router = routers.DefaultRouter()



router.register('', BookViewSet)
#router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
