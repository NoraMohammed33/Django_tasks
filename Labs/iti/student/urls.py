from django.urls import path
from .views import *

urlpatterns=[
    path('viewlist',viewlist),
    path('insert',insert),
    path('update',update),
    path('delete',delete)
]