from django.core.management.base import BaseCommand, CommandError
from utils.data_factory import DataFactory

class Command(BaseCommand):
    help = "Read Data from Mockup csv file and Populate DB"

    def add_arguments(self, parser):
        parser.add_argument("-f", "--file_path", default='./data/product_mockup_data.csv', type=str, help="Path for user data csv file.")
    
    def handle(self, *args, **options):
        try:
            file_path = options['file_path']

            self.stdout.write(self.style.NOTICE("Start Populating Product DB"))

            factory      = DataFactory()
            product_data = factory.load_from_csv(file_path)
            print(product_data[0])
            factory.populate_products(product_data)
            
            self.stdout.write(self.style.SUCCESS("Successfully Populated Product DB"))
            
        except CommandError as e:
            print(e)
