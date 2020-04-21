from django.contrib import admin
from django import forms
from .models import Person, Queue

class formQueue(forms.ModelForm):
    class meta:
        model = Person
    def clean(self):
        cleaned_data = super().clean()
        in_att = Person.objects.filter(status = 'in_att')
        queue = cleaned_data.get('queue')
        status = cleaned_data.get('status')
        if in_att.filter(queue = queue).exists() and status == 'in_att':
            raise forms.ValidationError("Queue already has someone in attendance") 
        return cleaned_data

class personAdmin(admin.ModelAdmin):
    form = formQueue

    list_display=  ('name','arrival','queue','status')

class queueAdmin(admin.ModelAdmin):
    def getOrder(self, obj):
        queue = Person.objects.filter(queue = obj)
        first = queue.filter(status = 'in_att')
        first = [q.name for q in first]
        queue = queue.filter(status = 'wai')
        person = [q.name for q in queue]
        return "("  + "".join(first) + ") -- " + " -- ".join(person)
        

    list_display = ('service','getOrder',)
admin.site.register(Person,personAdmin)
admin.site.register(Queue, queueAdmin)
