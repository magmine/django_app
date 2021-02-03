from django.urls import path, include
from . import views
from .views import SignUpView

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('signup/', SignUpView.as_view(template_name='registration/signup.html'), name='signup'),
    #path('', views.IndexView.as_view(), name='index'),
    #Arguments inside brackets should be the same as the expected argument in the method in the second argument of path
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'), 
    path('<int:question_id>/', views.detail, name='detail'),
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

# app_name = 'polls'
# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#     path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]