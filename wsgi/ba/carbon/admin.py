from django.contrib import admin
from django.contrib.admin import AdminSite

# Register your models here.
from .models import Carbon, Binder, Bag, Anode, Cell, Electrolyte, Experiment,Base

def make_used(modeladmin, request, queryset):
    queryset.update(status='n')
make_used.short_description = "Mark selected items as used"

class BagAdmin(admin.ModelAdmin):
    list_display = ('sn', 'carbon', 'binder','pub_date','status')
    search_fields = ('sn', 'carbon__sn', 'binder__sn','pub_date')
    list_filter = ('carbon','binder','pub_date','status')
    ordering = ('-pub_date',)
    actions = [make_used]
    exclude = ('author',)
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
    def get_queryset(self, request):
        qs = super(BagAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

class BinderAdmin(admin.ModelAdmin):
    list_display = ('sn', 'material','pub_date','status')
    search_fields =  ('sn', 'material','pub_date')
    list_filter =  ('material','pub_date','status')
    ordering = ('-pub_date',)
    actions = [make_used]
    exclude = ('author',)
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
    def get_queryset(self, request):
        qs = super(BinderAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)
    
class CarbonAdmin(admin.ModelAdmin):
    list_display = ('sn', 'source','pub_date','status')
    search_fields =  ('sn', 'source','pub_date')
    list_filter =  ('source','status','pub_date')
    ordering = ('-pub_date',)
    actions = [make_used]
    exclude = ('author',)
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
    def get_queryset(self, request):
        qs = super(CarbonAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)
    
class CellAdmin(admin.ModelAdmin):
    list_display = ('sn', 'anode', 'electrolyte','pub_date')
    search_fields = ('sn', 'anode__sn', 'electrolyte__sn','pub_date')
    list_filter = ('anode', 'electrolyte','pub_date')
    ordering = ('-pub_date',)
    exclude = ('author',)
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
    def get_queryset(self, request):
        qs = super(CellAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    
class ElectrolyteAdmin(admin.ModelAdmin):
    list_display = ('sn', 'salt', 'solvent','pub_date')
    search_fields = ('sn', 'salt', 'solvent','pub_date')
    list_filter = ('salt', 'solvent','pub_date')
    ordering = ('-pub_date',)
    actions = [make_used]
    exclude = ('author',)
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
    def get_queryset(self, request):
        qs = super(ElectrolyteAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)
class AnodeAdmin(admin.ModelAdmin):
    list_display = ('sn', 'weight', 'bag','pub_date','status')
    search_fields = ('sn', 'weight', 'bag__sn','pub_date')
    list_filter = ('bag','pub_date','status')
    ordering = ('-pub_date',)
    actions = [make_used]
    exclude = ('author',)
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
    def get_queryset(self, request):
        qs = super(AnodeAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)


class ExperimentAdmin(admin.ModelAdmin):
    
    def anode(self, obj):
        return obj.cell.anode
    anode.short_description = 'anode'
    
    def electrolyte(self, obj):
        return ("%s" % (obj.cell.electrolyte))
    electrolyte.short_description = 'electrolyte'
    
    def bag(self, obj):
        return  obj.cell.anode.bag
    bag.short_description = 'bag'

    def carbon(self, obj):
        return  obj.cell.anode.bag.carbon
    carbon.short_description = 'carbon'
    
    def binder(self, obj):
        return  obj.cell.anode.bag.binder
    binder.short_description = 'binder'
    
      
    list_display = ('sn', 'cell', 'experiment_type','anode','carbon','binder','electrolyte','pub_date')
    search_fields =('sn', 'cell__sn','cell__electrolyte__sn', 'cell__anode__bag__carbon__source','cell__anode__bag__carbon__sn','cell__anode__bag__binder__sn','pub_date')
    list_filter =('cell__electrolyte', 'cell__anode__bag__carbon','cell__anode__bag__binder','cell__anode__bag__carbon__source','experiment_type','pub_date')
    ordering = ('-pub_date',)
    exclude = ('author',)
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
    def get_queryset(self, request):
        qs = super(ExperimentAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)


  
    
admin.site.site_title="Battery Admin"
admin.site.index_title="Battery Disciplines"
admin.site.site_header="Battery Administration"
admin.site.site_url=None


##admin=BatteryAdmin(name='BatteryAdmin')
admin.site.register(Carbon,CarbonAdmin)
admin.site.register(Binder,BinderAdmin)
admin.site.register(Bag, BagAdmin)
admin.site.register(Cell,CellAdmin)
admin.site.register(Electrolyte,ElectrolyteAdmin)
admin.site.register(Experiment,ExperimentAdmin)
admin.site.register(Base)
admin.site.register(Anode,AnodeAdmin)
