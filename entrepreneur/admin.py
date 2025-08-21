from django.contrib import admin

from .models import (Entrepreneur,
                     BankAccount,
                     Nationality)

admin.site.register(Entrepreneur)
admin.site.register(BankAccount)
admin.site.register(Nationality)
