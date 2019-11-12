from app import app
import unittest

class AppTests(unittest.TestCase): 

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_home_status_code(self):
        result = self.app.get('/') 
        self.assertEqual(result.status_code, 200)

    def test_fortune_results_default_response(self):
        result = self.app.get('/fortune_results')
        self.assertIn('good luck in life!', str(result.data))

    def test_fortune_results_unicorn(self):
        result = self.app.get('/fortune_results?animal=aquatic')
        self.assertIn('A dream you have will come true.', str(result.data))

    def test_fortune_results_cat(self):
        result = self.app.get('/fortune_results?animal=cat')
        self.assertIn('People are naturally attracted to you.', str(result.data))

# run the tests
if __name__ == '__main__':
    unittest.main()
