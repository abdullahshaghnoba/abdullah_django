from django.contrib import admin

# Register your models here.
from .models import Game

class CustomGameAdmin(admin.ModelAdmin):
    model = Game
    list_display = ['name', 'purchaser', 'genre',]
    fieldsets= (
        ('Owner',{
            'fields':('purchaser',
            )}
        ),
        ('Game info',{
            'fields':('name','genre',
            )}
        )
    )

    
admin.site.register(Game, CustomGameAdmin)