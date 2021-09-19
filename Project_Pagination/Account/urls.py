
from django.urls import path
from .views import registerview,loginview,logoutview
#from django.contrib.auth.views import PasswordChangeView


urlpatterns = [
    path('register/', registerview, name='register'),
    path('login/', loginview, name='login'),
    path('logout/', logoutview, name='logout'),

]

