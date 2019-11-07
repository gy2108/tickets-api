from django.contrib import admin
from tickets.models import Ticket, Category

admin.site.register(Ticket)
admin.site.register(Category)