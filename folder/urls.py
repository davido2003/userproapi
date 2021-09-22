from django.urls import path
from .views import ProfileAPIView

urlpatterns = [
    path('generic/<int:id>/', ProfileAPIView.as_view()),
    path('generic/', ProfileAPIView.as_view())
    #path('profile/', profile_list),
   # path('detail/<int:pk>/', profile_detail)
]