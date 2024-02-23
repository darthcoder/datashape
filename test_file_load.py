import unittest
import pandas as pd
import os
from file_utils import load_data  # assuming file_utils.py is in the same directory

class TestLoadData(unittest.TestCase):
    def setUp(self):
        self.csv_filename = 'test.csv'
        self.xlsx_filename = 'test.xlsx'
        self.df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'C': ['p', 'q', 'r']
        })
        self.df.to_csv(self.csv_filename, index=False)
        self.df.to_excel(self.xlsx_filename, index=False)

    def tearDown(self):
        if os.path.exists(self.csv_filename):
            os.remove(self.csv_filename)
        if os.path.exists(self.xlsx_filename):
            os.remove(self.xlsx_filename)

    def test_load_data_csv(self):
        df_loaded = load_data(self.csv_filename)
        pd.testing.assert_frame_equal(df_loaded, self.df)

    def test_load_data_xlsx(self):
        df_loaded = load_data(self.xlsx_filename)
        pd.testing.assert_frame_equal(df_loaded, self.df)

    def test_load_data_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            load_data('nonexistent.csv')

if __name__ == '__main__':
    unittest.main()