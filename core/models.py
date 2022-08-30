from django.db import models
from django.core.validators import MaxValueValidator




class Organization(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)
    code = models.CharField(max_length=50,blank=True, null=True)
    organization_administrator = models.IntegerField(blank=True, null=True)
    customer_company = models.CharField(max_length=50,blank=True, null=True)
    city = models.CharField(max_length=50,blank=True, null=True)
    state = models.CharField(max_length=50,blank=True, null=True)
    country = models.CharField(max_length=50,blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_user = models.IntegerField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.IntegerField(blank=True, null=True)
    update_user = models.SmallIntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'organization'






class People(models.Model):
    name_first = models.CharField(max_length=50,blank=True, null=True)
    name_last = models.CharField(max_length=50,blank=True, null=True)
    resume_file_name = models.CharField(max_length=50,blank=True, null=True)
    current_latest_position = models.CharField(max_length=50,blank=True, null=True)
    city = models.CharField(max_length=50,blank=True, null=True)
    state = models.CharField(max_length=50,blank=True, null=True)
    country = models.CharField(max_length=10,blank=True, null=True)
    phone = models.CharField(max_length=50,blank=True, null=True)
    email = models.CharField(max_length=50,blank=True, null=True)
    skills_keywords = models.CharField(max_length=255,blank=True, null=True)
    obsolete = models.SmallIntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_user = models.IntegerField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.IntegerField(blank=True, null=True)
    organization_id = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=50,blank=True, null=True)
    history_comments = models.TextField(max_length=50,blank=True, null=True)
    current_latest_company = models.CharField(max_length=255,blank=True, null=True)

    def __str__(self):
        return self.name_first

    class Meta:
        managed = False
        db_table = 'people'





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




class BuildingItem(models.Model):
    building = models.ForeignKey(Building,on_delete=models.CASCADE)
    name = models.CharField(max_length=512, blank=True, null=True)
    parent_building_item = models.IntegerField(blank=True, null=True)
    people_id = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=788,blank=True, null=True)
    comments  = models.TextField(blank=True, null=True)
    ta1 = models.CharField(max_length=788, blank=True, null=True)
    ta2 = models.CharField(max_length=788, blank=True, null=True)
    ta3 = models.CharField(max_length=788, blank=True, null=True)
    ta4 = models.CharField(max_length=788, blank=True, null=True)
    ta5 = models.CharField(max_length=788, blank=True, null=True)
    ta6 = models.CharField(max_length=788, blank=True, null=True)
    ta7 = models.CharField(max_length=788, blank=True, null=True)
    ta8 = models.CharField(max_length=788, blank=True, null=True)
    ta9 = models.CharField(max_length=788, blank=True, null=True)
    ta10 = models.CharField(max_length=788, blank=True, null=True)
    ta11 = models.CharField(max_length=788, blank=True, null=True)
    ta12 = models.CharField(max_length=788, blank=True, null=True)
    ta13 = models.CharField(max_length=788, blank=True, null=True)
    ta14 = models.CharField(max_length=788, blank=True, null=True)
    ta15 = models.CharField(max_length=788, blank=True, null=True)
    ta16 = models.CharField(max_length=788, blank=True, null=True)
    ta17 = models.CharField(max_length=788, blank=True, null=True)
    ta18 = models.CharField(max_length=788, blank=True, null=True)
    ta19 = models.CharField(max_length=788, blank=True, null=True)
    ta20 = models.CharField(max_length=788, blank=True, null=True)
    sl1 = models.IntegerField(blank=True, null=True)
    sl2 = models.IntegerField(blank=True, null=True)
    sl3 = models.IntegerField(blank=True, null=True)
    sl4 = models.IntegerField(blank=True, null=True)
    sl5 = models.IntegerField(blank=True, null=True)
    sl6 = models.IntegerField(blank=True, null=True)
    sl7 = models.IntegerField(blank=True, null=True)
    sl8 = models.IntegerField(blank=True, null=True)
    sl9 = models.IntegerField(blank=True, null=True)
    sl10 = models.IntegerField(blank=True, null=True)
    sl11 = models.IntegerField(blank=True, null=True)
    sl12 = models.IntegerField(blank=True, null=True)
    sl13 = models.IntegerField(blank=True, null=True)
    sl14 = models.IntegerField(blank=True, null=True)
    sl15 = models.IntegerField(blank=True, null=True)
    sl16 = models.IntegerField(blank=True, null=True)
    sl17 = models.IntegerField(blank=True, null=True)
    sl18 = models.IntegerField(blank=True, null=True)
    sl19 = models.IntegerField(blank=True, null=True)
    sl20 = models.IntegerField(blank=True, null=True)
    obsolete = models.SmallIntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_user = models.IntegerField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.IntegerField(blank=True, null=True)
    guid = models.CharField(max_length=255, blank=True, null=True)
    additional_data_type_form_instance_id = models.IntegerField(blank=True, null=True)
    additional_data_type_form_name = models.CharField(max_length=255, blank=True, null=True)
    building_item_category_id = models.IntegerField(blank=True, null=True)
    batch_id = models.CharField(max_length=255, blank=True, null=True)



    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'building_item'





class TestBuilding(models.Model):
    id = models.AutoField(primary_key=True)  
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
        # managed = False
        db_table = 'building_test' 




class TestBuildingItem(models.Model):
    id = models.AutoField(primary_key=True)
    building_test = models.ForeignKey(TestBuilding,on_delete=models.CASCADE)
    name = models.CharField(max_length=512, blank=True, null=True)
    parent_building_item = models.IntegerField(blank=True, null=True)
    people_id = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=788,blank=True, null=True)
    comments  = models.TextField(blank=True, null=True)
    ta1 = models.CharField(max_length=788, blank=True, null=True)
    ta2 = models.CharField(max_length=788, blank=True, null=True)
    ta3 = models.CharField(max_length=788, blank=True, null=True)
    ta4 = models.CharField(max_length=788, blank=True, null=True)
    ta5 = models.CharField(max_length=788, blank=True, null=True)
    ta6 = models.CharField(max_length=788, blank=True, null=True)
    ta7 = models.CharField(max_length=788, blank=True, null=True)
    ta8 = models.CharField(max_length=788, blank=True, null=True)
    ta9 = models.CharField(max_length=788, blank=True, null=True)
    ta10 = models.CharField(max_length=788, blank=True, null=True)
    ta11 = models.CharField(max_length=788, blank=True, null=True)
    ta12 = models.CharField(max_length=788, blank=True, null=True)
    ta13 = models.CharField(max_length=788, blank=True, null=True)
    ta14 = models.CharField(max_length=788, blank=True, null=True)
    ta15 = models.CharField(max_length=788, blank=True, null=True)
    ta16 = models.CharField(max_length=788, blank=True, null=True)
    ta17 = models.CharField(max_length=788, blank=True, null=True)
    ta18 = models.CharField(max_length=788, blank=True, null=True)
    ta19 = models.CharField(max_length=788, blank=True, null=True)
    ta20 = models.CharField(max_length=788, blank=True, null=True)
    sl1 = models.IntegerField(blank=True, null=True)
    sl2 = models.IntegerField(blank=True, null=True)
    sl3 = models.IntegerField(blank=True, null=True)
    sl4 = models.IntegerField(blank=True, null=True)
    sl5 = models.IntegerField(blank=True, null=True)
    sl6 = models.IntegerField(blank=True, null=True)
    sl7 = models.IntegerField(blank=True, null=True)
    sl8 = models.IntegerField(blank=True, null=True)
    sl9 = models.IntegerField(blank=True, null=True)
    sl10 = models.IntegerField(blank=True, null=True)
    sl11 = models.IntegerField(blank=True, null=True)
    sl12 = models.IntegerField(blank=True, null=True)
    sl13 = models.IntegerField(blank=True, null=True)
    sl14 = models.IntegerField(blank=True, null=True)
    sl15 = models.IntegerField(blank=True, null=True)
    sl16 = models.IntegerField(blank=True, null=True)
    sl17 = models.IntegerField(blank=True, null=True)
    sl18 = models.IntegerField(blank=True, null=True)
    sl19 = models.IntegerField(blank=True, null=True)
    sl20 = models.IntegerField(blank=True, null=True)
    obsolete = models.SmallIntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_user = models.IntegerField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.IntegerField(blank=True, null=True)
    guid = models.CharField(max_length=255, blank=True, null=True)
    additional_data_type_form_instance_id = models.IntegerField(blank=True, null=True)
    additional_data_type_form_name = models.CharField(max_length=255, blank=True, null=True)
    building_item_category_id = models.IntegerField(blank=True, null=True)
    batch_id = models.CharField(max_length=255, blank=True, null=True)



    def __str__(self):
        return self.name

    class Meta:
        # managed = False
        db_table = 'building_item_test'


