from django.test import TestCase


def parse_csv_at(sheet_url):
    import requests
    import csv

    lines = requests.get(sheet_url).text.splitlines()
    return csv.DictReader(lines)


def make_models(parsed_csv):
    from .models import Activity, ActivityEvent

    for header in parsed_csv.fieldnames[1:]:
        Activity.objects.get_or_create(category=header)

    print(Activity.objects.all())
    
    for row in parsed_csv:
        print(row)
    print(ActivityEvent.objects.all())

class ImportTests(TestCase):
    def test_can_import_csv(self):
        import os
        csv = parse_csv_at(os.environ['SHEET_URL'])
        make_models(csv)

        self.assertFalse(csv)
