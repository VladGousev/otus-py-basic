from django.core.management import BaseCommand
from main.models import Engineer, EquipmentType, Site


class Command(BaseCommand):
    help = "Fill database"

    def handle(self, *args, **options):
        engineers = Engineer.objects.all()
        engineers.delete()
        Engineer.objects.create(
            name="Муковнин Александр Дмитриевич",
            phone="+7(985)197-75-86",
        )

        eq_types = EquipmentType.objects.all()
        eq_types.delete()
        EquipmentType.objects.create(name="Сервер")
        EquipmentType.objects.create(name="Коммутатор")

        sites = Site.objects.all()
        sites.delete()
        Site.objects.create(
            name="МЦОД",
            address="Москва, 2-ой Южнопортовый проезд, д.12в, стр.2",
        )
        Site.objects.create(
            name="МиниЦОД",
            address="Москва, 2-ой Южнопортовый проезд, д.12в, стр.2",
        )
        Site.objects.create(
            name="СЦОД",
            address='Москва, территория инновационного центра "Сколково", '
            "Большой бульвар, д.64",
        )
        # Site.objects.create(
        #     name="",
        #     address="",
        # )
        # Site.objects.create(
        #     name="",
        #     address="",
        # )
        # Site.objects.create(
        #     name="",
        #     address="",
        # )
        # Site.objects.create(
        #     name="",
        #     address="",
        # )
        # Site.objects.create(
        #     name="",
        #     address="",
        # )
        # Site.objects.create(
        #     name="",
        #     address="",
        # )
        # Site.objects.create(
        #     name="",
        #     address="",
        # )
