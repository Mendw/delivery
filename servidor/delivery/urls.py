from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from delivery import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', views.Registration.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('zones/', views.ZoneList.as_view()),
    path('zones/<int:pk>', views.ZoneDetail.as_view()),
    path('characteristics/', views.CharacteristicList.as_view()),
    path('characteristics/<int:pk>', views.CharacteristicDetail.as_view()),
    path('deliveries/', views.DeliveryList.as_view()),
    path('deliveries/<int:pk>', views.DeliveryDetail.as_view()),
    path('stores/', views.StoreList.as_view()),
    path('stores/<int:pk>', views.StoreDetail.as_view()),
    path('deliverypeople/', views.DeliveryPersonList.as_view()),
    path('deliverypeople/<int:pk>', views.DeliveryPersonDetail.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('parra/notes/', views.NoteList.as_view()),
    path('parra/notes/<int:pk>', views.NoteDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
