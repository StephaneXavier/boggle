from boggle import Boggle
from unittest import TestCase



class BoggleTestCase(TestCase):
    '''Test the Boggle Class'''
    def setUp(self):
        test_boggle = Boggle()
    
    def test_make_board(self):
        
