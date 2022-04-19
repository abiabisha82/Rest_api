from django.urls import path,include
from profiles_user import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('profile',views.UserProfileViewSet)

urlpatterns = [
    path('hello-vieww/', views.UserProfileViewSet.as_view()),
    path('', include(router.urls)),
]
