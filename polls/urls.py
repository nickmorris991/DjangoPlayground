from django.urls import path

from . import views

# we can give path a view route (views.index) and the name of our view function (index)
# and it will attach that view function to the route '' 
# (which becuase is /polls because we're in that subdirectory)
urlpatterns = [
    path('', views.index, name='index'),
]