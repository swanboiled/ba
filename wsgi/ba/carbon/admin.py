from django.contrib import admin
from django.contrib.admin import AdminSite

# Register your models here.
from .models import Carbon, Binder, Bag, Anode, Cell, Electrolyte, Experiment,Base

def make_used(modeladmin, request, queryset):
    queryset.update(status='n')
make_used.short_description = "Mark selected items as used"

class BagAdmin(admin.ModelAdmin):
    list_display = ('sn', 'carbon', 'binder','pub_date','status')
    search_fields = ('sn', 'carbon', 'binder','pub_date')
    list_filter = ('carbon','binder','pub_date','status')
    ordering = ('-pub_date',)
    actions = [make_used]

class BinderAdmin(admin.ModelAdmin):
    list_display = ('sn', 'material','pub_date','status')
    search_fields =  ('sn', 'material','pub_date')
    list_filter =  ('sn', 'material','pub_date','status')
    ordering = ('-pub_date',)
    actions = [make_used]
    
class CarbonAdmin(admin.ModelAdmin):
    list_display = ('sn', 'source','pub_date','status')
    search_fields =  ('sn', 'source','pub_date')
    list_filter =  ('sn', 'source','pub_date','status')
    ordering = ('-pub_date',)
    actions = [make_used]
    
class CellAdmin(admin.ModelAdmin):
    list_display = ('sn', 'anode', 'electrolyte','pub_date')
    search_fields = ('sn', 'anode', 'electrolyte','pub_date')
    list_filter = ('sn', 'anode', 'electrolyte','pub_date')
    #ordering = ('-pub_date',)

    
class ElectrolyteAdmin(admin.ModelAdmin):
    list_display = ('sn', 'salt', 'solvent','pub_date')
    search_fields = ('sn', 'salt', 'solvent','pub_date')
    list_filter = ('sn', 'salt', 'solvent','pub_date')
    ordering = ('-pub_date',)
    actions = [make_used]
    
class AnodeAdmin(admin.ModelAdmin):
    list_display = ('sn', 'weight', 'bag','pub_date','status')
    search_fields = ('sn', 'weight', 'bag','pub_date')
    list_filter = ('sn', 'weight', 'bag','pub_date','status')
    ordering = ('-pub_date',)
    actions = [make_used]
    


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
    
      
    list_display = ('sn', 'cell', 'anode','carbon','binder','electrolyte','pub_date')
    search_fields =('sn', 'cell', 'pub_date')
    list_filter =('sn', 'cell','pub_date')
    #ordering = ('-pub_date',)



  
    
class BatteryAdmin(AdminSite):
    site_header = 'BatteryAdmin'
    site_title='BatteryAdmin'
    site_url=None
    index_title='Battery Administration'
    date_hierarchy = 'pub_date'
    
carbonadmin=BatteryAdmin(name='BatteryAdmin')
carbonadmin.register(Carbon,CarbonAdmin)
carbonadmin.register(Binder,BinderAdmin)
carbonadmin.register(Bag, BagAdmin)
carbonadmin.register(Cell,CellAdmin)
carbonadmin.register(Electrolyte,ElectrolyteAdmin)
carbonadmin.register(Experiment,ExperimentAdmin)
carbonadmin.register(Base)
carbonadmin.register(Anode,AnodeAdmin)