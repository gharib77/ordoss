from django.urls import path
#from demo.views import home,personne
from .views import personne,home
app_name="demo"
urlpatterns = [
    path('',home.index,name='home'),
    path('list_pers',personne.list_pers,name='list_pers'),
]

