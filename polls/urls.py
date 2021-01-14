from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #Arguments inside brackets should be the same as the expected argument in the method in the second argument of path
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]