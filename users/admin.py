from django.contrib import admin
from users.models import Biodata

# Register your models here.
class BiodataAdmin(admin.ModelAdmin):

    list_display = ('user', 'nama', 'telp', 'alamat')

    search_fields = ('user', 'nama')

admin.site.register(Biodata, BiodataAdmin)