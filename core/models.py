from django.db import models
from django.conf import settings
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError


class Doctor(models.Model):
    name = models.CharField(max_length=255, verbose_name="ФИО")
    is_active = models.BooleanField(default=True, verbose_name="Запись разрешена?")

    class Meta:
        verbose_name = "врач"
        verbose_name_plural = "Врачи"

    @classmethod
    def get_active(cls):
        return cls.objects.filter(is_active=True)

    def __str__(self):
        return "%s" % self.name


class Entry(models.Model):
    doctor = models.ForeignKey("Doctor", related_name="entries", verbose_name="Врач")
    patient = models.CharField(max_length=255, verbose_name="Пациент")
    start_at = models.DateTimeField(verbose_name="Начало приема")

    class Meta:
        verbose_name = "запись"
        verbose_name_plural = "Записи"
        ordering = ['start_at']

    def clean(self):
        if self.doctor_id is not None and self.start_at is not None:
            entries = Entry.objects.filter(doctor=self.doctor,
                                            start_at__hour=self.start_at.hour, 
                                            start_at__day=self.start_at.day, 
                                            start_at__month=self.start_at.month, 
                                            start_at__year=self.start_at.year)
            if entries:
                raise ValidationError({
                    NON_FIELD_ERRORS: ['Указаное время не доступно для записи',],
                })
