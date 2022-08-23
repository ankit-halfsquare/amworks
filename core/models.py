from django.db import models

# Create your models here.
class Project(models.Model):
    organization_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    project_administrator_id = models.IntegerField(blank=True, null=True)
    company_id = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    cost = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    revenue = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    margin = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    email_address = models.CharField(max_length=50, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_user = models.IntegerField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.IntegerField(blank=True, null=True)
    obsolete = models.SmallIntegerField(blank=True, null=True)
    item_name_track = models.CharField(max_length=10, blank=True, null=True)
    item_name_order = models.CharField(max_length=50, blank=True, null=True)
    item_name_table = models.CharField(max_length=10, blank=True, null=True)
    item_name_alias = models.CharField(max_length=50, blank=True, null=True)
    ta1_alias = models.CharField(max_length=50, blank=True, null=True)
    ta2_alias = models.CharField(max_length=50, blank=True, null=True)
    ta3_alias = models.CharField(max_length=50, blank=True, null=True)
    ta4_alias = models.CharField(max_length=50, blank=True, null=True)
    ta5_alias = models.CharField(max_length=50, blank=True, null=True)
    sl1_list = models.IntegerField(blank=True, null=True)
    sl1_alias = models.CharField(max_length=50, blank=True, null=True)
    sl2_list = models.IntegerField(blank=True, null=True)
    sl2_alias = models.CharField(max_length=50, blank=True, null=True)
    sl3_list = models.IntegerField(blank=True, null=True)
    sl3_alias = models.CharField(max_length=50, blank=True, null=True)
    sl4_list = models.IntegerField(blank=True, null=True)
    sl4_alias = models.CharField(max_length=50, blank=True, null=True)
    sl5_list = models.IntegerField(blank=True, null=True)
    sl5_alias = models.CharField(max_length=50, blank=True, null=True)
    customization = models.TextField(blank=True, null=True)
    role_management = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    customer_feedback = models.TextField(blank=True, null=True)
    results = models.TextField(blank=True, null=True)
    building_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'project'



class Building(models.Model):  
    organization_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_user = models.IntegerField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.IntegerField(blank=True, null=True)
    obsolete = models.SmallIntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    ta1_alias = models.CharField(max_length=255, blank=True, null=True)
    ta2_alias = models.CharField(max_length=255, blank=True, null=True)
    ta3_alias = models.CharField(max_length=255, blank=True, null=True)
    ta4_alias = models.CharField(max_length=255, blank=True, null=True)
    ta5_alias = models.CharField(max_length=255, blank=True, null=True)
    ta6_alias = models.CharField(max_length=255, blank=True, null=True)
    ta7_alias = models.CharField(max_length=255, blank=True, null=True)
    ta8_alias = models.CharField(max_length=255, blank=True, null=True)
    ta9_alias = models.CharField(max_length=255, blank=True, null=True)
    ta10_alias = models.CharField(max_length=255, blank=True, null=True)
    ta11_alias = models.CharField(max_length=255, blank=True, null=True)
    ta12_alias = models.CharField(max_length=255, blank=True, null=True)
    ta13_alias = models.CharField(max_length=255, blank=True, null=True)
    ta14_alias = models.CharField(max_length=255, blank=True, null=True)
    ta15_alias = models.CharField(max_length=255, blank=True, null=True)
    ta16_alias = models.CharField(max_length=255, blank=True, null=True)
    ta17_alias = models.CharField(max_length=255, blank=True, null=True)
    ta18_alias = models.CharField(max_length=255, blank=True, null=True)
    ta19_alias = models.CharField(max_length=255, blank=True, null=True)
    ta20_alias = models.CharField(max_length=255, blank=True, null=True)
    sl1_alias = models.CharField(max_length=255, blank=True, null=True)
    sl1_list = models.IntegerField(blank=True, null=True)
    sl2_alias = models.CharField(max_length=255, blank=True, null=True)
    sl2_list = models.IntegerField(blank=True, null=True)
    sl3_alias = models.CharField(max_length=255, blank=True, null=True)
    sl3_list = models.IntegerField(blank=True, null=True)
    sl4_alias = models.CharField(max_length=255, blank=True, null=True)
    sl4_list = models.IntegerField(blank=True, null=True)
    sl5_alias = models.CharField(max_length=255, blank=True, null=True)
    sl5_list = models.IntegerField(blank=True, null=True)
    sl6_alias = models.CharField(max_length=255, blank=True, null=True)
    sl6_list = models.IntegerField(blank=True, null=True)
    sl7_alias = models.CharField(max_length=255, blank=True, null=True)
    sl7_list = models.IntegerField(blank=True, null=True)
    sl8_alias = models.CharField(max_length=255, blank=True, null=True)
    sl8_list = models.IntegerField(blank=True, null=True)
    sl9_alias = models.CharField(max_length=255, blank=True, null=True)
    sl9_list = models.IntegerField(blank=True, null=True)
    sl10_alias = models.CharField(max_length=255, blank=True, null=True)
    sl10_list = models.IntegerField(blank=True, null=True)
    sl11_alias = models.CharField(max_length=255, blank=True, null=True)
    sl11_list = models.IntegerField(blank=True, null=True)
    sl12_alias = models.CharField(max_length=255, blank=True, null=True)
    sl12_list = models.IntegerField(blank=True, null=True)
    sl13_alias = models.CharField(max_length=255, blank=True, null=True)
    sl13_list = models.IntegerField(blank=True, null=True)
    sl14_alias = models.CharField(max_length=255, blank=True, null=True)
    sl14_list = models.IntegerField(blank=True, null=True)
    sl15_alias = models.CharField(max_length=255, blank=True, null=True)
    sl15_list = models.IntegerField(blank=True, null=True)
    sl16_alias = models.CharField(max_length=255, blank=True, null=True)
    sl16_list = models.IntegerField(blank=True, null=True)
    sl17_alias = models.CharField(max_length=255, blank=True, null=True)
    sl17_list = models.IntegerField(blank=True, null=True)
    sl18_alias = models.CharField(max_length=255, blank=True, null=True)
    sl18_list = models.IntegerField(blank=True, null=True)
    sl19_alias = models.CharField(max_length=255, blank=True, null=True)
    sl19_list = models.IntegerField(blank=True, null=True)
    sl20_alias = models.CharField(max_length=255, blank=True, null=True)
    sl20_list = models.IntegerField(blank=True, null=True)
    zip = models.CharField(max_length=128, blank=True, null=True)
    guid = models.CharField(max_length=36, blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'building' 




class Test(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)

