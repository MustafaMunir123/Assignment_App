from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_question/', views.add_question, name="add_question"),
    path('add_answers/<str:pk>/', views.add_answers, name="add_answers"),
    path('update_question/<str:pk>/', views.update_question, name="update_question"),
    path('all_questions', views.all_questions, name="all_questions"),
    path('delete_question/<str:pk>/', views.delete_question, name="delete_question"),
    
    path('login_page', views.login_page, name='login_page'),
    path('logoutpage', views.logoutpage, name='logoutpage'),
    
    path('questions_base_page', views.questions_base_page, name='questions_base_page'),

    



    

]