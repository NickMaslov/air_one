from django.core.exceptions import ValidationError
from django.db import models

from cities.models import City


class Plane(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Plane number')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Travel time')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE,
                                  # null=True, blank=True,
                                  related_name='from_city_set',
                                  verbose_name='departure from'
                                  )
    to_city = models.ForeignKey('cities.City', on_delete=models.CASCADE,
                                related_name='to_city_set',
                                verbose_name='arrive in'
                                )

    def __str__(self):
        return f'Plane № {self.name}  {self.from_city} to {self.to_city}'

    class Meta:
        verbose_name = 'Plane'
        verbose_name_plural = 'Planes'
        ordering = ['travel_time']

    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError('Departing and arrival cities are the same')
        qs = Plane.objects.filter(
            from_city=self.from_city, to_city=self.to_city,
            travel_time=self.travel_time).exclude(pk=self.pk)
        # Train == self.__class__
        if qs.exists():
            raise ValidationError('Change travel time')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class TrainTest(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Train number')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE,
                                  # null=True, blank=True,
                                  related_name='from_city',
                                  verbose_name='Departing from'
                                  )
