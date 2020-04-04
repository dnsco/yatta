from django.test import TestCase


def parse_csv_at(sheet_url):
    import requests
    import csv

    lines = requests.get(sheet_url).text.splitlines()
    return csv.DictReader(lines)


class ImportTests(TestCase):
    def test_can_import_csv(self):
        import os
        csv = parse_csv_at(os.environ['SHEET_URL'])
        for row in csv:
            print(row)
        self.assertFalse(csv)
