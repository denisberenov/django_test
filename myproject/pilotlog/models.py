from django.db import models

from django.db import models

class Aircraft(models.Model):
    user_id = models.IntegerField()
    guid = models.CharField(max_length=255)
    platform = models.IntegerField()
    modified = models.DateTimeField()
    fin = models.CharField(max_length=255, blank=True, default='')
    sea = models.BooleanField(default=False)
    tmg = models.BooleanField(default=False)
    efis = models.BooleanField(default=False)
    fnpt = models.IntegerField(default=0)
    make = models.CharField(max_length=255, blank=True, default='')
    run2 = models.BooleanField(default=False)
    class_field = models.IntegerField(default=0)
    model = models.CharField(max_length=255, blank=True, default='')
    power = models.IntegerField(default=1)
    seats = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    kg5700 = models.BooleanField(default=False)
    rating = models.CharField(max_length=255, blank=True, default='')
    company = models.CharField(max_length=255, blank=True, default='')
    complex = models.BooleanField(default=False)
    cond_log = models.IntegerField(default=0)
    fav_list = models.BooleanField(default=False)
    category = models.IntegerField(default=0)
    high_perf = models.BooleanField(default=False)
    sub_model = models.CharField(max_length=255, blank=True, default='')
    aerobatic = models.BooleanField(default=False)
    ref_search = models.CharField(max_length=255, blank=True, default='')
    reference = models.CharField(max_length=255, blank=True, default='')
    tailwheel = models.BooleanField(default=False)
    default_app = models.IntegerField(default=0)
    default_log = models.IntegerField(default=0)
    default_ops = models.IntegerField(default=0)
    device_code = models.IntegerField(default=0)
    aircraft_code = models.CharField(max_length=255, blank=True, default='')
    default_launch = models.IntegerField(default=0)
    record_modified = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.make} {self.model} ({self.guid})'

class Flight(models.Model):
    flight_id = models.CharField(max_length=255)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    origin = models.CharField(max_length=255, blank=True, default='')
    destination = models.CharField(max_length=255, blank=True, default='')
    pilot = models.CharField(max_length=255, blank=True, default='')
    duration = models.DurationField()
    remarks = models.TextField(blank=True, default='')

    def __str__(self):
        return f'Flight {self.flight_id} from {self.origin} to {self.destination}'


