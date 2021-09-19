from django.urls import path
from .views import *
urlpatterns = [
    path('base/',baseview,name='base'),
    path('submit/',submitview,name='submitform'),
    path('showlist/',showALLview,name='showlist'),


    path('page-fucntion/',pageview,name='page-function'),
    path('page-class/',PageListView.as_view(),name='page-class'),

    path('delete/<int:id>',deletepersonview,name='delete'),
    path('update/<int:id>',updatepersonview,name='update'),

    path('addPeople/',addFakePeople,name='addPeople'),



]

