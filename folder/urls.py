from django.urls import path
from .views import ProfileAPIView

urlpatterns = [
    path('/', ProfileAPIView.as_view()),
    path('/', ProfileAPIView.as_view())
    #path('profile/', profile_list),
   # path('detail/<int:pk>/', profile_detail)
]
