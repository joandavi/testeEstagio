
from django.db import models
   


class Queue(models.Model):
    service = models.CharField(max_length = 50, default='42')
    
    def __str__(self):
        return self.service



class Person(models.Model):
    arrival = models.DateTimeField(auto_now_add=True, blank=True)
    name = models.CharField(max_length=200)
    queue = models.ForeignKey(Queue, on_delete=models.CASCADE, default='42')
    STATUS = [
        ('att', 'attended'),
        ('in_att', 'in attendance'),
        ('wai', 'waiting'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS,
        default= 'wai',
    )


    def __str__(self):
        return self.name
    
