from .models import Question, Answer
from django.forms import ModelForm

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'

class QuestionForm(ModelForm):
    # inlines = [AnswerForm]
    class Meta:
        model = Question
        fields = '__all__'