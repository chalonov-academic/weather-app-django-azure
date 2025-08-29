from django.test import TestCase, Client
from django.urls import reverse
from climante.models import Worldcities
import json

class BasicFunctionalityTest(TestCase):
    """Tests básicos para verificar que la aplicación funciona"""
    
    def setUp(self):
        """Configuración inicial para los tests"""
        self.client = Client()
        # Crear una ciudad de prueba
        Worldcities.objects.create(
            id=1,
            city="Madrid",
            lat=40.4168,
            lng=-3.7038,
            country="Spain"
        )

    def test_basic_math(self):
        """Test básico para verificar que los tests funcionan"""
        self.assertEqual(1 + 1, 2)
        self.assertEqual(2 * 3, 6)

    def test_home_page_loads(self):
        """Test que la página principal carga correctamente"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Climante')

    def test_discover_page_loads(self):
        """Test que la página de descubrir funciona"""
        response = self.client.get('/discover')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Climante')

    def test_worldcities_model(self):
        """Test que el modelo Worldcities funciona"""
        city = Worldcities.objects.get(id=1)
        self.assertEqual(city.city, "Madrid")
        self.assertEqual(city.country, "Spain")
        self.assertIsInstance(city.lat, float)
        self.assertIsInstance(city.lng, float)

    def test_random_city_selection(self):
        """Test que se puede seleccionar una ciudad aleatoria"""
        random_city = Worldcities.objects.all().order_by('?').first()
        self.assertIsNotNone(random_city)
        self.assertIsInstance(random_city.city, str)

    def test_template_context(self):
        """Test que el contexto del template contiene los datos necesarios"""
        response = self.client.get('/discover')
        self.assertIn('city', response.context)
        self.assertIn('country', response.context)
        self.assertIn('temp', response.context)

class ViewsTest(TestCase):
    """Tests específicos para las vistas"""
    
    def setUp(self):
        """Configuración para tests de vistas"""
        self.client = Client()
        # Crear datos de prueba
        Worldcities.objects.create(
            id=2,
            city="Barcelona",
            lat=41.3851,
            lng=2.1734,
            country="Spain"
        )

    def test_temp_somewhere_view(self):
        """Test de la vista temp_somewhere"""
        response = self.client.get(reverse('temp_somewhere'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('city', response.context)
        self.assertIn('temp', response.context)

    def test_temp_here_view(self):
        """Test de la vista temp_here"""
        response = self.client.get(reverse('temp_here'))
        self.assertEqual(response.status_code, 200)
        # Nota: Este test podría fallar si no hay conexión a internet
        # pero al menos verifica que la vista responde
