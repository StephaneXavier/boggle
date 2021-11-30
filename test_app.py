from unittest import TestCase
from app import app
import boggle

class AppRouteTests(TestCase):
    @classmethod
    def setUpClass(cls):
       pass
        
    
    def test_root(self):
        with app.test_client() as client:
            
            resp = client.get('/')
            # import pdb
            # pdb.set_trace()
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Welcome to boggle!</h1>',html )
            self.assertIn('<td>', html )
        
    def test_guess(self):
        with app.test_client() as client:
            with client.session_transaction() as session:
                session['board'] = [['L','E','M','O','N'],
                ['L','E','M','O','N'],
                ['L','E','M','O','N'],
                ['L','E','M','O','N'],
                ['L','E','M','O','N']]
                                        
                
        resp = client.get('/guess?word=lemon')
        self.assertEqual(resp.json,'ok')
    
    def test_score(self):
        with app.test_client() as client:
            resp = client.get('/score?score=50')
        import pdb
        pdb.set_trace()