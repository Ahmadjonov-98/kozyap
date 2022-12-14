from django.db import models
from datetime import datetime, timedelta

def get_date(*args, **kwargs):
    return datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')


class Object(models.Model):  # Obyekt
    name = models.CharField(verbose_name="Obyekt nomi", max_length=56)
    location = models.CharField(verbose_name="Joylashuvi ", max_length=56)
    geolokatsiyasi = models.CharField(verbose_name="Geolokatsiyasi", max_length=129)
    brigadier = models.ForeignKey(verbose_name="Brigadir", to='kozyap.Brigadier', related_name="ojects",
                                  on_delete=models.SET_NULL, null=True)


    class Meta:
        db_table = "object"
        verbose_name = "Obyekt"
        verbose_name_plural = "Obyektlar"

    def __str__(self):
        return self.name


class Brigadier(models.Model):  # Brigadir
    full_name = models.CharField(verbose_name="Ism Familya", max_length=50)
    tgid = models.BigIntegerField(verbose_name="Telegram ID", unique=True)
    username = models.CharField(verbose_name="Telegram Username", max_length=20, null=True)
    phone = models.CharField(max_length=13, null=True)

    class Meta:
        db_table = "bridgadier"
        verbose_name = "Brigader"
        verbose_name_plural = "Brigadirlar"

    def __str__(self):
        return self.full_name

    @property
    def staffs(self):
        return self.staff.all()


class Staff(models.Model):  # Xodim
    full_name = models.CharField(verbose_name="Ism Familya", max_length=56)
    tgid = models.IntegerField(verbose_name="Telegram ID", unique=True, null=True, blank=True)
    username = models.CharField(verbose_name="Telegram Username", max_length=120, unique=True, null=True)
    brigadier = models.ForeignKey(verbose_name="Brigadir", to=Brigadier, related_name="staff",
                                  on_delete=models.SET_DEFAULT, default=1)

    class Meta:
        db_table = "stuff"
        verbose_name = "Ishchi"
        verbose_name_plural = "Ishchilar"

    def __str__(self):
        return self.full_name

    @property
    def salary(self):
        return self.reports.all()


class StaffReport(models.Model):  # Xodimlar Keldi Kettisi Bitta Hodim uchun
    date = models.DateField(verbose_name="Sana", editable=True)
    work_hour = models.DecimalField(verbose_name="Ish Smena", decimal_places=1, max_digits=3)
    stuff = models.ForeignKey(verbose_name="Hodim", to=Staff, on_delete=models.SET_DEFAULT, default=0,
                              related_name="reports")
    dwage = models.BigIntegerField(default=0)

    def __str__(self):
        return f"{self.date}"

    class Meta:
        db_table = "staff_report"
        verbose_name = "KunlikHodim"
        verbose_name_plural = "KunlikHodimlar"


class Intruments(models.Model):
    owner = models.ForeignKey(verbose_name="Brigadier", to=Brigadier, on_delete=models.SET_DEFAULT, default=-1)
    status = models.CharField(verbose_name="Holati", max_length=128)
    name = models.CharField(verbose_name="Instrument Nomi", max_length=128)
    number = models.CharField(verbose_name="Instrument Nomeri", max_length=45, default=0)

    class Meta:
        db_table = "instrument"
        verbose_name = "Uskuna"
        verbose_name_plural = "Uskunalar"

    def __str__(self):
        return f"{self.name} {self.number} "


class Transport(models.Model):
    name = models.CharField(verbose_name="Mashina Nomi", max_length=128)
    number = models.CharField(verbose_name="Mashina Raqami", max_length=128)
    company = models.CharField(verbose_name="Mashina Raqami", max_length=128)


class Driver(models.Model):
    fullname = models.CharField(verbose_name="Ism Familya", max_length=128)
    username = models.CharField(verbose_name="Telegram Username", max_length=56)
    phone = models.CharField(verbose_name="Telefon Raqam", max_length=13)
    tgid = models.IntegerField(verbose_name="Telegram ID")
    transport = models.ForeignKey(verbose_name="Mashinasi", to=Transport, on_delete=models.SET_DEFAULT, default=-1)


# class CABack(Model): #Keldi Ketdi Oylik Hisobot
#     brigadier_id = models.ForeignKey(verbose_name="Brigadir", to=Brigadier, on_delete=models.SET_NULL)
#     object = models.ForeignKey(verbose_name="Obyekt", to=Object, on_delete=models.SET_NULL, max_length=512)
#     location_name = models.CharField(verbose_name="Lokatsiya", max_length=512, on_delete=models.SET_NULL, null=True)
#     staff = models.ForeignKey(verbose_name="Hodim", to=Staff, max_length=56, on_delete=models.SET_NULL)
#     staff_postion = models.CharField(verbose_name="Hodim Lavozimi", max_length=56)
#     thour = models.ForeignKey(verbose_name="Jami ishlagan soati", decimal_places=1, null=True)
#     dwage = models.DecimalField(verbose_name="Kunlik Ish Haqi", decimal_places=2)
#     twage = models.DecimalField(verbose_name="Jami Kunlik Ish Haqi", decimal_places=2)
#
#     class Meta:
#         db_table = "cback"
#         verbose_name = "Keldi Ketdi"
#
#     def __str__(self):
#         return self.brigadier_id.__str__()
#
#
class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    # class LocationField(MultiValueField):
    #     def __init__(self, *args, **kwargs):
    #         fields = (
    #             FloatField(max_value=90, min_value=-90),
    #             FloatField((max_value=90, min_value=-90)
    #         )
    #         super().__init__(*args, **kwargs)
    #

    def compress(self, data_list):
        latitude, longitude = data_list
        return Location(latitude, longitude)


class ToDoList(models.Model):  # Qilingan IShlar Royhati
    date = models.DateField(verbose_name="Sana", unique=False)
    brigadier = models.ForeignKey(verbose_name="Brigadir", to=Brigadier, on_delete=models.SET_DEFAULT, default=-1)
    object = models.ForeignKey(verbose_name="Obyekt", to=Object, on_delete=models.SET_DEFAULT, default=-1)
    stuff_count = models.IntegerField(verbose_name="Hodimlar Soni", null=False)
    todos = models.TextField(verbose_name="Qilingan Ishlar")
    comment = models.TextField(verbose_name="Izoh", null=True)
    measure = models.CharField(max_length=56, verbose_name="O'lchov birligi", null=True)
    size = models.CharField(max_length=128, verbose_name="Qilingan ish obyomi", null=True)
    price = models.IntegerField(verbose_name="Narxi", null=True)
    total = models.BigIntegerField(verbose_name="Jami", null=True)
    admin_comment = models.TextField(verbose_name="Admin Izohi", null=True)

    class Meta:
        db_table = "todos"
        verbose_name = "Qilinga Ish Qo'shish"
        verbose_name_plural = "Qilingan Ishlar Ro'yhati"

    def __str__(self):
        return f"{self.object}"


class Cost(models.Model):  # Pul Harajatlari
    date = models.DateField()
    owner = models.CharField(verbose_name="Kim Berdi", null=True, max_length=128)
    stuff = models.CharField(verbose_name="Kim Oldi", null=True, max_length=128)
    object = models.ForeignKey(verbose_name="Qaysi obyekt uchun harajat", to=Object, related_name="costs",
                               on_delete=models.SET_NULL, default=-1, null=True)
    reason = models.CharField(verbose_name="Maqsadi", null=True, max_length=128)
    input = models.IntegerField(verbose_name="Kirim", null=True)
    output = models.IntegerField(verbose_name="Chiqim", null=True)
    balance = models.IntegerField(verbose_name="Qolgan Summa", null=False)
    admin_comment = models.TextField(verbose_name="Admin Izoh", null=True)

    class Meta:
        db_table = "cost"
        verbose_name = "Pul Harajarti"
        verbose_name_plural = "Pul Harajartlari"


class ExChangeInstrument(models.Model):  # Instrument  Oldi berdisi
    date = models.DateField(verbose_name="Olingan Sana")
    owner = models.ForeignKey(verbose_name="Kim berdi", to=Brigadier, on_delete=models.SET_DEFAULT, default=-1,
                              related_name="owner")
    object = models.ForeignKey(verbose_name="Obyekt nomi", to=Object, on_delete=models.SET_DEFAULT, default=-1)
    given = models.ForeignKey(verbose_name="Kim Oldi", to=Brigadier, on_delete=models.SET_DEFAULT, default=-1,
                              related_name="given")
    instrument = models.ForeignKey(verbose_name="Instrument", to=Intruments, on_delete=models.SET_DEFAULT, default=-1,
                                   related_name="exchange")
    status = models.CharField(verbose_name="Instrument holati", max_length=128, default="-")
    count = models.IntegerField(verbose_name="Soni", default=0)
    count_type = models.CharField(verbose_name="Sanoq Turi", max_length=24, default='-')
    input = models.IntegerField(verbose_name="Kirim", default=0)
    output = models.IntegerField(verbose_name="Chiqim", default=0)
    admin_comment = models.CharField(verbose_name="Admin Izohi", max_length=128, default='')

    class Meta:
        db_table = "exchangeinstrument"
        verbose_name = "Instrument Oldi Berdi"
        verbose_name_plural = "Instrument Ooldi Berdisi"

    def __str__(self):
        return f"{self.owner} : {self.given}"


class TechnicTodos(models.Model):  # Texnikalar Hisobi
    date = models.DateField(verbose_name="Sana")
    driver = models.ForeignKey(verbose_name="Texnika Mashinisti", to=Driver, on_delete=models.SET_DEFAULT, default=-1,
                               related_name="techtodos")
    object = models.ForeignKey(verbose_name="Texnika Nomi", to=Object, on_delete=models.SET_DEFAULT, default=-1,
                               related_name="techtodos")
    transport = models.ForeignKey(verbose_name="Texnika Nomi", to=Transport, on_delete=models.SET_DEFAULT, default=-1,
                                  related_name="techtodos")
    todos = models.CharField(verbose_name="Nima Ish Qildi", max_length=256)

