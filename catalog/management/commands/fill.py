import json
from django.core.management import BaseCommand
from django.db import connection
from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):

        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE catalog_category RESTART IDENTITY CASCADE;')

        Category.objects.all().delete()
        Product.objects.all().delete()

        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

            products_for_create = []
            categories_for_create = []

            for category in data:
                if category["model"] == "catalog.category":
                    categories_for_create.append(Category(category_name=category['fields']['category_name'],
                                                          category_description=category['fields']
                                                          ['category_description']))
                    Category.objects.bulk_create(categories_for_create)
            for product in data:
                if product["model"] == "catalog.product":
                    products_for_create.append(Product(product_name=product['fields']['product_name'],
                                                       product_description=product['fields']['product_description'],
                                                       product_category=Category.objects.get(
                                                            pk=product['fields']['product_category']),
                                                       product_price=product['fields']['product_price']))

            Product.objects.bulk_create(products_for_create)
