from django.db import models

class Aircraft(models.Model):
    user_id = models.IntegerField()
    guid = models.CharField(max_length=36)
    platform = models.IntegerField()
    modified = models.IntegerField()
    fin = models.CharField(max_length=100, blank=True)
    sea = models.BooleanField(default=False)
    tmg = models.BooleanField(default=False)
    efis = models.BooleanField(default=False)
    fnpt = models.IntegerField(default=0)
    make = models.CharField(max_length=100)
    run2 = models.BooleanField(default=False)
    class_field = models.IntegerField(default=0)  # 'class' is a reserved keyword
    model = models.CharField(max_length=100)
    power = models.IntegerField(default=1)
    seats = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    kg5700 = models.BooleanField(default=False)
    rating = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    complex = models.BooleanField(default=False)
    cond_log = models.IntegerField(default=0)
    fav_list = models.BooleanField(default=False)
    category = models.IntegerField(default=0)
    high_perf = models.BooleanField(default=False)
    sub_model = models.CharField(max_length=100, blank=True)
    aerobatic = models.BooleanField(default=False)
    ref_search = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    tailwheel = models.BooleanField(default=False)
    default_app = models.IntegerField(default=0)
    default_log = models.IntegerField(default=0)
    default_ops = models.IntegerField(default=0)
    device_code = models.IntegerField(default=0)
    aircraft_code = models.CharField(max_length=36)
    default_launch = models.IntegerField(default=0)
    record_modified = models.IntegerField(default=0)

    def __str__(self):
        return self.reference

