from django.urls import path

from . import views

# we can give path a view route (views.index) and the name of our view function (index)
# and it will attach that view function to the route '' 
# (which becuase is /polls because we're in that subdirectory)
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]



