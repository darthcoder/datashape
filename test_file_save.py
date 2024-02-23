import unittest
import pandas as pd
import os
from file_utils import save_report  # assuming file_utils.py is in the same directory

class TestSaveReport(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'C': ['p', 'q', 'r']
        })
        self.filename = 'test.csv'

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_save_report(self):
        save_report(self.df, self.filename)
        self.assertTrue(os.path.exists(self.filename))

        df_loaded = pd.read_csv(self.filename)
        pd.testing.assert_frame_equal(df_loaded, self.df)

    def test_save_report_empty_df(self):
        df_empty = pd.DataFrame()
        save_report(df_empty, self.filename)
        self.assertTrue(os.path.exists(self.filename))

        df_loaded = pd.read_csv(self.filename)
        pd.testing.assert_frame_equal(df_loaded, df_empty)

if __name__ == '__main__':
    unittest.main()