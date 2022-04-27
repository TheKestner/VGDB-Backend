from django.contrib import admin

from .models import Game
from .models import Company
from .models import Franchise
from .models import Platform
from .models import Screenshot
from .models import Genre
from .models import Mode

# Register your models here.

admin.site.register(Game)
admin.site.register(Company)
admin.site.register(Franchise)
admin.site.register(Platform)
admin.site.register(Screenshot)
admin.site.register(Genre)
admin.site.register(Mode)