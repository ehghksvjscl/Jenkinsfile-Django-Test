from django.test import TestCase
from django.test import Client

# Create your tests here.
class SampleTest(TestCase):
    maxDiff = None

    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_sample_get_success(self):
        client = Client()
        response = client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello word"})

    def test_sample_get_fale(self):
        client = Client()
        response = client.get("/fale")

        self.assertEqual(response.status_code, 404)
  