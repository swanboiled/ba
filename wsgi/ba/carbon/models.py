from django.db import models
# Create your models here.

STATUS_CHOICES = (
    ('a', 'Available'),
    ('n', 'Used'),
)
EXP_CHOICES = (
    ('l', 'Low rate cycling'),
    ('h', 'High rate cycling'),
     ('c', 'Cyclic voltammetry'),
)
class Carbon(models.Model):
    sn = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    pyrolysis_temperature = models.IntegerField(default=1400)
    pyrolysis_duration = models.IntegerField(default=2)
    comments = models.TextField(default='Leave your comments here')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,default='a')
    pub_date = models.DateTimeField('date produced')
    def __str__(self):
        return self.sn
class Binder(models.Model):
    sn = models.CharField(max_length=30)
    material = models.CharField(max_length=30)
    comments = models.TextField(default='Leave your comments here')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,default='a')
    pub_date = models.DateTimeField('date produced')
    def __str__(self):
        return self.sn
class Base(models.Model):
    sn = models.CharField(max_length=30)
    metal=models.CharField(max_length=30)
    weight=models.FloatField(default=5.64)
    comments = models.TextField(default='Leave your comments here')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,default='a')
    pub_date = models.DateTimeField('date produced')
    def __str__(self):
        return self.sn
class Bag(models.Model):
    sn = models.CharField(max_length=30)
    carbon = models.ForeignKey(Carbon)
    binder = models.ForeignKey(Binder)
    base = models.ForeignKey(Base)
    comments = models.TextField(default='Leave your comments here')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,default='a')
    pub_date = models.DateTimeField('date produced')
    def __str__(self):
        return u'%s:%s%s'   % (self.sn,self.carbon, self.binder)
class Anode(models.Model):
    sn = models.CharField(max_length=30)
    weight=models.FloatField(default=2)
    bag = models.ForeignKey(Bag)
    comments = models.TextField(default='Leave your comments here')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,default='a')
    pub_date = models.DateTimeField('date produced')
    def __str__(self):
        return u'%s:%s(%s)' %(self.bag.sn, self.sn,self.weight)
    
class Electrolyte(models.Model):
    sn = models.CharField(max_length=30)
    salt=models.CharField(max_length=30, default='NaF6')
    solvent=models.CharField(max_length=30, default='EC:DMC')
    comments = models.TextField(default='Leave your comments here')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,default='a')
    pub_date = models.DateTimeField('date produced')
    def __str__(self):
        return self.sn
    
class Cell(models.Model):
    sn = models.CharField(max_length=30)
    anode = models.ForeignKey(Anode)
    electrolyte=models.ForeignKey(Electrolyte)
    comments = models.TextField(default='Leave your comments here')
    pub_date = models.DateTimeField('date produced')
    def __str__(self):
        return self.sn
class Experiment(models.Model):
    sn = models.CharField(max_length=30)
    cell = models.ForeignKey(Cell)
    experiment_type= models.CharField(max_length=1, choices=EXP_CHOICES,default='l')
    result = models.FileField(upload_to='uploads/%Y/%m/%d/', default='none')
    comments = models.TextField(default='Leave your comments here')
    pub_date = models.DateTimeField('date produced')
    def __str__(self):
        return self.sn

