from django.test import TestCase


def fetch_file():
    import os
    import requests
    sheet_url = os.environ['SHEET_URL']
    return requests.get(sheet_url)


class ImportTests(TestCase):
    def test_can_import_csv(self):
        self.assertFalse(fetch_file())
