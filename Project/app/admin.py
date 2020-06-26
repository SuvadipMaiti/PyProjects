from django.contrib import admin
from .models import Books,Character,Author

# Register your models here.
# admin.site.register(Books)
@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    fields = ['title','description','price','published','is_published','cover']
    list_display = ['title','description','price','published']
    list_filter = ['published']
    search_fields = ['title','description','price','published']


admin.site.register(Character)
admin.site.register(Author)

