from django.urls import path

from . import views

# we can give path a view route (views.index) and the name of our view function (index)
# and it will attach that view function to the route '' 
# (which becuase is /polls because we're in that subdirectory)
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
