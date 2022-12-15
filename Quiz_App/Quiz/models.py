from django.db import models

# Create your models here.

class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateField(auto_now=True, null=True)

    class Meta:
        abstract = True
    
class Category(BaseModel):
    category_name = models.CharField(max_length= 100, null=True)
    
    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name_plural="Categories"
    
class Question(BaseModel):
    question = models.CharField(max_length=400, null=True)
    category = models.ForeignKey(Category, null=True, on_delete= models.SET_NULL)
    
    def __str__(self):
        return self.question
    
class Answer(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.answer
    
    
