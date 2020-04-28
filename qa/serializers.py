from rest_framework import serializers
from .models import Question, Answer

class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.HyperlinkedRelatedField(view_name="single_question", read_only=True, lookup_field='id')
    class Meta:
        model = Answer
        fields = ['user', 'question','content','votes']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title', 'description', 'user']
     
class QuestionAnswerSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only = True)
    class Meta:
        model = Question
        fields = ['id', 'title', 'description', 'answers']
        #fields = '__all__'     