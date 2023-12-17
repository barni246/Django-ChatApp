from django.contrib import admin
from chat.models import Message

# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    fields = ('text','created_at','author','receiver',)
    list_display = ('text','created_at','author','receiver',)
    search_fields = ('text',)
    
    
    

admin.site.register(Message,MessageAdmin)
