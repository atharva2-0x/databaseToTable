
import unittest

from mapping_2 import map_consumer_data

class TestMapConsumerData(unittest.TestCase):
    def test_mapping(self):
       
        mock_consumer_data = [
            (4, 'Atharva Swami', 'Main St, new hospital, maharashatra, LAtur, 413521', '9421-754-5555', 'Atharva.Swami@example.com', '123456789', '1234567890123456789', 'Standard', '[100, 200, 300]', 'Paid')
        ]

        expected_mapped_data = [
            {
                'Consumer ID': 4,
                'First Name': 'Atharva',
                'Last Name': 'Swami',
                'Address Line 1': 'Main St',
                'Address Line 2': 'new hospital',
                'City': 'LAtur',
                'State': 'maharashatra',
                'Zip Code': '413521',
                'Phone Number': '9421-754-5555',
                'Email Address': 'Atharva.Swami@example.com'
            }
        ]

        
        mapped_data = map_consumer_data(mock_consumer_data)

        self.assertEqual(mapped_data, expected_mapped_data)

if __name__ == '__main__':
    unittest.main()
