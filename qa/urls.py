
from django.urls import path, include
from .views import QuestionGenericAPIView, AnswerGenericAPIView, QuestionAnswerGenericAPIView

urlpatterns = [
    path('questions', QuestionAnswerGenericAPIView.as_view(), name = "all_questions"),
    path('questions/<int:id>', QuestionAnswerGenericAPIView.as_view(), name = "single_question"),
    path('questions/<int:id>/answers',QuestionAnswerGenericAPIView.as_view(), name='single_question_answers'),
    path('answers', AnswerGenericAPIView.as_view(), name="all_answers"),
    path('answers/<int:id>', AnswerGenericAPIView.as_view(), name = "single_answer"),
    #path('questions/answers', QuestionAnswerGenericAPIView.as_view(), name = "all_questions_answers"),
]