from django.urls import path

from .views import v_index, insertar, update,delete


urlpatterns = [
    path('', v_index, name="index"),
    path('insertar/', insertar, name="insert"),
    path('update/<int:laboratorio_id>/', update),
    path('delete/<int:laboratorio_id>/', delete),
    
]