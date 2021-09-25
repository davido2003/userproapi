from django.urls import path
from .views import NewsAPIView

urlpatterns = [
<<<<<<< HEAD
    path('News/<int:id>/', NewsAPIView.as_view()),
    path('News/', NewsAPIView.as_view())
=======
    path('profile/', ProfileAPIView.as_view()),
    path('profile/', ProfileAPIView.as_view())
>>>>>>> d9076ffac8f4b376932b155bde6b345978a15bf6
    #path('profile/', profile_list),
   # path('detail/<int:pk>/', profile_detail)
]
