
from django.urls import path, include
from .views import QuestionGenericAPIView, AnswerGenericAPIView

urlpatterns = [
    path('questions/', QuestionGenericAPIView.as_view(), name = "all_questions"),
    path('questions/<int:id>/', QuestionGenericAPIView.as_view(), name = "single_question"),
    path('answers/', AnswerGenericAPIView.as_view(), name="all_answers"),
    path('answers/<int:id>/', AnswerGenericAPIView.as_view(), name = "single_answer"),
]