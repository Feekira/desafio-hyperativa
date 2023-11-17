from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView
from core.views import list_cards, create_card, get_card, add_cards

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    re_path('^token/', TokenObtainPairView.as_view()),
    path('api/list_cards', list_cards),
    path('api/create-card/', create_card),
    path('api/get-card/<str:pk>', get_card),
    path('api/add-cards/', add_cards),
]