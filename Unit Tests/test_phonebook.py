import unittest
from phonebook import Phonebook



class PhonebookTest(unittest.TestCase):

    def test_phonebook_by_name(self):
        phonebook = Phonebook()
        phonebook.add("John", "555-555-5555")
        number = phonebook.lookup("John")
        self.assertEqual("555-555-5555", number)
    
    def test_missing_name(self):
        phonebook = Phonebook()
        number = phonebook.lookup("Vohn")
        self.assertIsNone(number)
    
    @unittest.skip("demonstrating skipping")
    def test_phonebook_by_number(self):
        phonebook = Phonebook()
        phonebook.add("John", "555-555-5555")
        names = phonebook.names()
        self.assertEqual(["John"], names)
        
    def test_empty_phonebook(self):
        phonebook = Phonebook()
        names = phonebook.names()
        self.assertEqual([], names)
        

if __name__ == '__main__':
    unittest.main()