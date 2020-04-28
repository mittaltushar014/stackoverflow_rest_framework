from rest_framework import serializers
from .models import Question, Answer

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        #fields = ['user', 'question','content','views']
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only = True)
    class Meta:
        model = Question
        fields = ['title', 'description','answers']
        #fields = '__all__'
     