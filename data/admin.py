from django.contrib import admin
from data.models import Category, Workflow





class WorkflowAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
	list_display = ('name', 'slug', 'views', 'downloads', 'client_ip', 'created')
    	#prepopulated_fields = {'slug':('name',)}
	#admin.site.register(Category)


# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
	list_display = ('name', 'slug')

# Update the registration to include this customised interface
admin.site.register(Category, CategoryAdmin)
admin.site.register(Workflow, WorkflowAdmin)
