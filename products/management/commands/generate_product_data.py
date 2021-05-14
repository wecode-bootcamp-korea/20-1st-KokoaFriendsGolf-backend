from django.core.management.base import BaseCommand, CommandError
from utils.data_factory import DataFactory

class Command(BaseCommand):
    help = "Generate Mockup Data and Save them to data folder."

    def handle(self, *args, **options):
        
        try:

            self.stdout.write(self.style.NOTICE("Start Generating Products Data"))
            filepath = "./data/product_mockup_data.csv"
            factory = DataFactory()
            products = factory.gen_products()
            factory.save_to_csv(products, filepath)

            self.stdout.write(self.style.SUCCESS("Successfully Generated Products Data."))
            
        except CommandError as e:
            print(e)