from django.urls import path
from laboratorio import views

urlpatterns = [
    path('', v_index.site.urls)
    
]