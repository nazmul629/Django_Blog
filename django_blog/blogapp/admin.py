from django.contrib import admin
from .models import author,category,articale,comment
# Register your models here.

class authorModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__","name"]
    class Meta:
        Model = author
admin.site.register(author,authorModel)

class categoryModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]
    list_per_page = 15
    class Meta:
        Model = category

admin.site.register(category,categoryModel)


class articalModel(admin.ModelAdmin):
    list_display = ["__str__", "posted_on"]
    search_fields = ["__str__","details"]
    list_per_page = 10
    list_filter = ["posted_on","category"]
    class Meta:
        Model = articale
admin.site.register(articale,articalModel)



class commentModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]
    list_per_page = 10
    class Meta:
        Model = comment
admin.site.register(comment,commentModel)


