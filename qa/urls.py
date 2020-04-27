
from django.urls import path, include
from .views import QuestionGenericAPIView, AnswerGenericAPIView

urlpatterns = [
    path('questions/', QuestionGenericAPIView.as_view()),
    path('questions/<int:id>/', QuestionGenericAPIView.as_view()),
    path('answers/', AnswerGenericAPIView.as_view()),
    path('answers/<int:id>/', AnswerGenericAPIView.as_view()),
]