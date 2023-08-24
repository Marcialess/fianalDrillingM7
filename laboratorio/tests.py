from django.test import TestCase
from .models import Laboratorio

class LaboratorioTests(TestCase):
    def setUp(self):
        lab1 = Laboratorio()
        lab1.nombre = "Laborat1"
        lab1.ciudad = "Santiago"
        lab1.pais = "Chile"
        lab1.save()


        lab2 = Laboratorio()
        lab2.nombre = "Laborat1"
        lab2.ciudad = "Coyahique"
        lab2.pais = "Chile"
        lab2.save()

        lab3 = Laboratorio()
        lab3.nombre = "Laborat1"
        lab3.ciudad = "Concepcion"
        lab3.pais = "Chile"
        lab3.save()

    def test_index(self):
        response = self.client.get("/")
        labs = response.context["laborat"]
        self.assertEqual(3, labs.count())

    def test_create(self):
        respuesta = self.client.post("/insertar",{
            "nombre": "Lab 4",
            "ciudad": "Valdivia",
            "pais":"Chile"},follow= True)
        
        self.assertEqual(200, respuesta.status_code)
        self.assertTemplateUsed(respuesta, "v_index.html")

        self.assertEqual(4,Laboratorio.objects.all().count())
