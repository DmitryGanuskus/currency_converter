from django.urls import path

from api.views import converter

app_name = 'api'

urlpatterns = [
    path('api/rates/', converter, name='converter'),
]
