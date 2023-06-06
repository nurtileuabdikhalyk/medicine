from django.contrib.auth.models import User
from django.db import models


class Poliklinika(models.Model):
    organization = models.CharField('Поликлиника аты', max_length=255)
    address = models.CharField('Поликлиника мекен-жайы', max_length=255)
    phone = models.CharField('Телефон', max_length=12)

    class Meta:
        verbose_name = "Поликлиника"
        verbose_name_plural = "Поликлиника"

    def __str__(self):
        return f"{self.organization} {self.address}"


class Doctor(models.Model):
    user = models.OneToOneField(User, verbose_name='Қолданушы', on_delete=models.CASCADE)
    first_name = models.CharField("Есімі", max_length=150)
    last_name = models.CharField("Тегі", max_length=150)
    poliklinika = models.ForeignKey(Poliklinika, verbose_name='Поликлиника', on_delete=models.CASCADE)
    rejim = models.CharField("Жұмыс уақыты", max_length=255)
    position = models.CharField("Кәсіби мамандығы", max_length=150)

    class Meta:
        verbose_name = "Дәрігер"
        verbose_name_plural = "Дәрігерлер"

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.position} {self.poliklinika.address}"


class Patient(models.Model):
    user = models.OneToOneField(User, verbose_name='Қолданушы', on_delete=models.CASCADE)
    first_name = models.CharField("Есімі", max_length=150)
    last_name = models.CharField("Тегі", max_length=150)
    phone = models.CharField("Телефон", max_length=12)
    email = models.EmailField("Почта")
    jsn = models.CharField("ЖСН", max_length=12)
    birthday = models.DateField("Туылған күні")
    gender = models.CharField("Жынысы", max_length=4)
    national = models.CharField("Ұлты", max_length=20)
    address = models.CharField("Мекен-жайы", max_length=1000)
    doctor = models.ForeignKey(Doctor, verbose_name='Учаскелік дәрігер', on_delete=models.CASCADE, null=True,
                               blank=True)

    class Meta:
        verbose_name = "Пациент"
        verbose_name_plural = "Пациенттер"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Zapis(models.Model):
    doctor = models.ForeignKey(Doctor, verbose_name='Дәрігер', on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, verbose_name='Пациент', on_delete=models.CASCADE)
    completed = models.BooleanField("Статус", default=False)
    data = models.DateTimeField("Жазылым уақыты", )
    created = models.DateTimeField("Жазылған уақыты", auto_now_add=True)

    class Meta:
        verbose_name = "Жазылым"
        verbose_name_plural = "Жазылымдар"

    def __str__(self):
        return f"{self.doctor} - {self.patient} {self.created}"


class Consultation(models.Model):
    first_name = models.CharField("Есімі", max_length=150)
    last_name = models.CharField("Тегі", max_length=150)
    department = models.CharField("Бөлімі", max_length=150)
    phone = models.CharField("Телефон", max_length=12)
    date = models.DateField("Күні")
    time = models.TimeField("Уақыты")
    question = models.TextField("Сұрағы", max_length=5000)

    class Meta:
        verbose_name = "Кеңес алушы"
        verbose_name_plural = "Кеңес алушылар"

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone}"


class DoctorAtHome(models.Model):
    doctor = models.ForeignKey(Doctor, verbose_name='Дәрігер', on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, verbose_name='Пациент', on_delete=models.CASCADE)
    address = models.CharField("Адресс", max_length=150)
    data = models.DateTimeField("Жазылым уақыты", )
    created = models.DateTimeField("Жазылған уақыты", auto_now_add=True)

    class Meta:
        verbose_name = "Үйге шақырту"
        verbose_name_plural = "Үйге шақыртулар"

    def __str__(self):
        return f"{self.doctor} {self.patient} {self.address}"


class Feedback(models.Model):
    first_name = models.CharField('Есімі', max_length=150)
    last_name = models.CharField('Тегі', max_length=150)
    message = models.TextField('Хабарлама мәтіні')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Пікір'
        verbose_name_plural = 'Пікірлер'
