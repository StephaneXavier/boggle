import boggle
from unittest import TestCase



class BoggleTestCase(TestCase):
    '''Test the Boggle Class'''
    @classmethod
    def setUpClass(cls):
        cls.boggle_instance = boggle.Boggle()
        cls.board = cls.boggle_instance.make_board()
        cls.test_board = [
            ['L','E','M','O','N'],
            ['L','E','M','O','N'],
            ['L','E','M','O','N'],
            ['L','E','M','O','N'],
            ['L','E','M','O','N']
        ]
        cls.test_board2 = [
            ['L','E','M','O','O'],
            ['L','E','M','O','O'],
            ['L','E','M','O','O'],
            ['L','E','M','O','O'],
            ['L','E','M','O','O']
        ]
        
         
    
    def test_make_board(self):
        self.assertEqual(len(self.board), 5)
        self.assertEqual(len(self.board[0]), 5)
    
    def test_check_valid_word(self):
        self.assertEqual(self.boggle_instance.check_valid_word(self.board, 'wafwa'), 'not-word')
        self.assertEqual(self.boggle_instance.check_valid_word(self.test_board,'lemon'), 'ok')
        self.assertEqual(self.boggle_instance.check_valid_word(self.test_board2,'lemon'), 'not-on-board')

    