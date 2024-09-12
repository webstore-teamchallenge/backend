from django.urls import path
from store_app.api.views import index

urlpatterns = [
    path('', index, name='index'),
]