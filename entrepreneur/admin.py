from django.contrib import admin

from .models import (Entrepreneur,
                     BankAccount)

admin.site.register(Entrepreneur)
admin.site.register(BankAccount)
