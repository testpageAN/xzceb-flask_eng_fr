import unittest

#from translator import english_to_french, french_to_english
from . import translator

class Testenglish_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(translator.english_to_french('None'), '') # test null input.
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour') # Test for the translation of the world 'Hello' and 'Bonjour'.
        

class Testfrench_to_english(unittest.TestCase): 
    def test1(self):
        self.assertNotEqual(translator.french_to_english('None'), '') # test null input.
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello') # Test for the translation of the world 'Bonjour' and 'Hello'.
        
        

unittest.main()
