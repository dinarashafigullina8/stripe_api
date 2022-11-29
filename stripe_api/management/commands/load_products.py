from django.core.management.base import BaseCommand, CommandError
import csv
from stripe_api.models import Item

class Command(BaseCommand):
    help = 'load people from csv'

    def handle(self, *args, **options):
        with open('item.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                price = row['Amount'][0:-2]
                name = row['Name']
                description = row['Description']
                price_id = row['Price ID']
                item = Item(price = price, name = name, description = description, price_id = price_id)
                item.save()