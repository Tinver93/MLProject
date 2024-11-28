import unittest
import import_ipynb
import HLTV

class parser_test(unittest.TestCase):
    
    def test_driver(self):
        user_id = 3
        self.assertIsNotNone(create_driver(user_id))

    def test_str_to_number_mean(self):
        self.assertEqual(str_to_number('12'), 12)
        self.assertEqual(str_to_number('0.25'), 0.25)

    def test_str_to_number_ex(self):
        with self.assertRaises(ValueError) as e:
            str_to_number('asdfg')
        self.assertEqual('Cannot convert ' + "'asdfg'" + ' to a number', e.exception.args[0])
        
        
unittest.main(argv=[''], verbosity=2, exit=False)