from django.core.management.base import BaseCommand, CommandError
from utils.data_factory import DataFactory

class Command(BaseCommand):
    help = "Generate Mockup Data and Save them to data folder."

    def add_arguments(self, parser):
        parser.add_argument("-n", "--num_user", type=int, help="How many fake users to create?")
        
    
    def handle(self, *args, **options):
        try:
            num_user = options['num_user']
            
            if not num_user or (num_user < 1):
                raise CommandError("Invalid Number of User.")

            self.stdout.write(self.style.NOTICE("Start Generating User Data"))

            filepath = "./data/user_mockup_data.csv"
            factory  = DataFactory()
            users    = factory.gen_users(num_users = num_user)
            factory.save_to_csv(users, filepath)

            self.stdout.write(self.style.SUCCESS("Successfully Generated User Data."))
            
        except CommandError as e:
            print(e)