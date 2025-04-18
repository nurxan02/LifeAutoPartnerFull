from django.core.management.base import BaseCommand
from lifeautoimport.models import ImportedCar, MonthlyProfit
from datetime import datetime
from decimal import Decimal

class Command(BaseCommand):
    help = "Calculate monthly profit and save it to the MonthlyProfit table"

    def handle(self, *args, **kwargs):
        # Mevcut ayın ilk gününü al
        current_month = datetime.now().replace(day=1)

        # Sadece satılmış arabaları al
        sold_cars = ImportedCar.objects.filter(status='sold')

        # Toplam net karı ve araç sayısını hesapla
        total_net_profit = sum(car.net_profit for car in sold_cars)
        car_count = sold_cars.count()

        # MonthlyProfit tablosuna kaydet veya güncelle
        monthly_profit, created = MonthlyProfit.objects.get_or_create(
            month=current_month,
            defaults={'total_profit': total_net_profit, 'car_count': car_count}
        )
        if not created:
            # Eğer zaten mevcutsa, değerleri güncelle
            monthly_profit.total_profit += total_net_profit
            monthly_profit.car_count += car_count
            monthly_profit.save()

        self.stdout.write(self.style.SUCCESS(
            f"Mothly sum profit: {total_net_profit} $, Car count: {car_count}"
        ))