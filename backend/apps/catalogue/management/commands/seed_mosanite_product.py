from decimal import Decimal

from django.core.management.base import BaseCommand

from apps.catalogue.models import Category, Product


class Command(BaseCommand):
    help = "Create the Mosanite Portuguese Cut stones pendant & earring set product for the catalog."

    def handle(self, *args, **options):
        category, _ = Category.objects.get_or_create(
            name="Jewellery",
            defaults={
                "description": "Sterling silver jewellery and gemstone accessories.",
                "image_url": "",
                "is_active": True,
                "sort_order": 1,
            },
        )

        product_data = {
            "name": "Mosanite Portuguese Cut Stones Pendant & Earring Set",
            "slug": "mosanite-portuguese-cut-stones-pendant-earring-set",
            "sku": "NC3-40-MOSANITE-SET",
            "category": category,
            "short_description": "Mosanite Portuguese Cut Stones Pendant & Earring Set made in 925 Sterling Silver.",
            "description": (
                "Mosanite Portuguese Cut Stones Pendant & Earring Set made in 925 Sterling Silver. "
                "Pendant features 6 mm stones and earring pair features 4 mm stones. "
                "Designed for gifting and everyday wear."
            ),
            "weight": Decimal("5.00"),
            "weight_unit": Product.WeightUnit.GRAM,
            "retail_price": Decimal("8499.00"),
            "wholesale_price": Decimal("6999.00"),
            "selling_modes": [Product.SellingMode.RETAIL],
            "retail_moq": 1,
            "wholesale_moq": 10,
            "is_active": True,
            "is_featured": True,
        }

        product, created = Product.objects.update_or_create(
            sku=product_data["sku"],
            defaults=product_data,
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f"Created product: {product.name}"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Updated product: {product.name}"))
