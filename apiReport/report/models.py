from django.db import models

# Create your models here.

class Customers(models.Model):
    name = models.CharField(max_length=200, blank=False, default='')
    
class Agents(models.Model):
    agent_id = models.ForeignKey(Customers,on_delete=models.CASCADE)
    agent_state = models.CharField(max_length=50, blank=False, default='')
    agent_reason_code_text = models.CharField(max_length=50, blank=False, default='')
    station_dn = models.CharField(max_length=50, blank=False, default='')

