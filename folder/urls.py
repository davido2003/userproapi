from django.urls import path
from .views import NewsAPIView

urlpatterns = [
    path('News/<int:id>/', NewsAPIView.as_view()),
    path('News/', NewsAPIView.as_view())
    #path('profile/', profile_list),
   # path('detail/<int:pk>/', profile_detail)
]