from django.contrib import admin

# Register your models here.
from .models import Category, Question, Answer

admin.site.register(Category)

class answer_stack(admin.StackedInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [answer_stack]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)