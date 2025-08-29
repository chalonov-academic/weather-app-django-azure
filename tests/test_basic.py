from django.test import TestCase, Client
from django.urls import reverse

class BasicFunctionalityTest(TestCase):
    """Tests básicos para verificar que la aplicación funciona"""
    
    def setUp(self):
        """Configuración inicial para los tests"""
        self.client = Client()

    def test_basic_math(self):
        """Test básico para verificar que los tests funcionan"""
        #self.assertEqual(1 + 1, 3) # FALLA INTENCIONALMENTE
        self.assertEqual(1 + 1, 2)
        self.assertEqual(2 * 3, 6)
