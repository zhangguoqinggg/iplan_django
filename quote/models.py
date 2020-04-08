from django.db import models
import django.utils.timezone as timezone

class Company(models.Model):
    id = models.AutoField(primary_key=True,)
    company_name = models.CharField(max_length=255,)
    company_name_english = models.CharField(max_length=255,)
    create_time = models.DateTimeField(default = timezone.now)
    class Meta:						# 如果读取已有数据的必要参数！
        db_table = "m_company"

    def __str__(self):
        return self.company_name

class Current_Status(models.Model):
    id = models.AutoField(primary_key=True,)
    current_status_name = models.CharField(max_length=255,)
    create_time = models.DateTimeField(default = timezone.now)

    class Meta:						# 如果读取已有数据的必要参数！
        db_table = "m_current_status"

    def __str__(self):
        return self.current_status_name

class Dept(models.Model):
    id = models.AutoField(primary_key=True,)
    dep_name = models.CharField(max_length=255)
    dep_parent_id = models.IntegerField()
    create_time = models.DateTimeField( default = timezone.now)

    class Meta:						# 如果读取已有数据的必要参数！
        db_table = "m_dept"
    def __str__(self):
        return self.dep_name

class Employe(models.Model):
    employe_id = models.AutoField(primary_key=True,)
    employe_name = models.CharField(max_length=255 )
    employe_code = models.CharField(max_length=255 )
    phone_number = models.CharField(max_length=50 )
    email = models.CharField(max_length=50 )
    dep_id = models.IntegerField()
    base_on  = models.CharField(max_length=255 )
    create_time = models.DateTimeField(default = timezone.now)

    class Meta:						# 如果读取已有数据的必要参数！
        db_table = "m_employe"
    def __str__(self):
        return self.employe_name


class User_Info(models.Model):
    user_id = models.AutoField(primary_key=True,)
    username = models.CharField(max_length=255 )
    password = models.CharField(max_length=255 )
    create_time = models.DateTimeField(default = timezone.now)

    class Meta:						# 如果读取已有数据的必要参数！
        db_table = "m_user_info"
    def __str__(self):
        return self.username


#
#
#
# class Company(models.Model):
#     ID = models.IntegerField(primary_key=True,)
#     NAME = models.CharField(max_length=255,)
#
#     class Meta:						# 如果读取已有数据的必要参数！
#         db_table = "Test_Table"
#
#     def __str__(self):
#         return self.NAME


class TEST(models.Model):
    ID = models.IntegerField(primary_key=True,)
    NAME = models.CharField(max_length=255,)

    class Meta:						# 如果读取已有数据的必要参数！
        db_table = "Test_Table"

    def __str__(self):
        return self.NAME


  #  python     manage.py    makemigrations
