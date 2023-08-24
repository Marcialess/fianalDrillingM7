from django.urls import path

from .views import v_index, insertar, update,delete


urlpatterns = [
    path('', v_index),
    path('update/<int:laboratorio_id>/', update),
    path('delete/<int:laboratorio_id>/', delete),
    path('insertar', insertar)
]

