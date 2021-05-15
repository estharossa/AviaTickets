from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('profile', ProfilesView)
router.register('users', UsersView)

urlpatterns = [
    path('login', login),
    path('register', register)
] + router.urls
