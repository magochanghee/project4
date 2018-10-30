from django.contrib import admin
from django.urls import path
from pagination.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert',insert),
    path('list', board_list),
]
