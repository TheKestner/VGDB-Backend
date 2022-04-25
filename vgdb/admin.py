from django.contrib import admin

from .models import Game
from .models import Company
from .models import Franchise

# Register your models here.

admin.site.register(Game)
admin.site.register(Company)
admin.site.register(Franchise)