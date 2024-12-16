from django.core.management.base import BaseCommand
from django_seed import Seed

from example.models import Supplier, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        seeder = Seed.seeder()
        seeder.add_entity(Supplier, 5)
        seeder.add_entity(Product, 10000)
        seeder.execute()
