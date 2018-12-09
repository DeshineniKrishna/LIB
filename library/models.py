from django.db import models
from django.utils import timezone
from datetime import datetime

class User(models.Model):
    User_id = models.CharField(primary_key= True,max_length=45)
    User_name = models.CharField(max_length=45)
    User_mail = models.CharField(max_length=45)
    User_pwd = models.CharField(max_length=45)
    def __str__(self):
        return str(self.User_id)

class Admin(models.Model):
    Admin_id=models.CharField(primary_key= True,max_length=45)
    Admin_name = models.CharField(max_length=45)
    Admin_mail = models.CharField(max_length=45)
    Admin_pwd = models.CharField(max_length=45)
    def __str__(self):
        return str(self.Admin_id)

class Book_detail(models.Model):
    Book_id = models.AutoField(primary_key=True)
    Book_name = models.CharField(max_length=45)
    #Publisher = models.CharField(max_length=45)
    Edition = models.CharField(max_length=45)
    Author = models.CharField(max_length=45)
    Price = models.CharField(max_length=45)
    Bool = models.CharField(max_length=45)
    #Quantity = models.CharField(max_length=45)
    Created_by = models.CharField(max_length=45,null = True, default = None)
    Created_at = models.DateTimeField(blank=True, null = True, default = None)
    Modified_by = models.CharField(max_length=45,null = True, default = None)
    Modified_at = models.DateTimeField(default=datetime.now,blank=True, null = True)

    def __str__(self):
        return str(self.Book_name)+ ' ' +str(self.Book_id)

class Issue_master(models.Model):
    User_id =models.ForeignKey(User, on_delete=models.CASCADE)
    Book_id = models.ForeignKey(Book_detail,on_delete=models.CASCADE)
    Issue_date = models.DateField(blank = True, null = True)
    Admin_id = models.ForeignKey(Admin, on_delete=models.CASCADE)
    Actual_return_date = models.DateField(blank = True, null = True)
    Return_date = models.DateField(blank = True, null = True)
    Fine = models.CharField(max_length=45,default ='0')
    Payment_status=models.CharField(max_length=45,default ='0')
    Created_by = models.CharField(max_length=45, default = None,null = True)
    Created_at = models.DateTimeField(blank=True,null = True, default = None)
    Modified_by = models.CharField(max_length=45, default = None,null = True)
    Modified_at = models.DateTimeField(default=datetime.now, blank=True,null = True)
    def __str__(self):
        return str(self.User_id.User_name)+' '+str(self.Book_id)

class Feedback(models.Model):
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Complaint = models.CharField(max_length=500)
    Date = models.DateField()
    Created_by = models.CharField(max_length=45, default = None,null = True)
    Created_at = models.DateTimeField(blank=True,null = True, default = None)
    Modified_by = models.CharField(max_length=45, default = None,null = True)
    Modified_at = models.DateTimeField(default=datetime.now, blank=True,null = True)
    def __str__(self):
        return str(self.User_id)+' '+str(self.id)

class Orderbook(models.Model):
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Book_name = models.CharField(max_length=45)
    Author = models.CharField(max_length=45)
    Created_by = models.CharField(max_length=45, default = None,null = True)
    Created_at = models.DateTimeField(blank=True, null = True, default = None)
    Modified_by = models.CharField(max_length=45, default = None,null = True)
    Modified_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return str(self.User_id)+ ' '+str(self.Book_name)

class DonateBook(models.Model):
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=45)
    Book_name = models.CharField(max_length=45)
    Created_by = models.CharField(max_length=45, default = None,null = True)
    Created_at = models.DateTimeField(blank=True,null = True, default = None)
    Modified_by = models.CharField(max_length=45, default = None,null = True)
    Modified_at = models.DateTimeField(default=datetime.now, blank=True,null = True)
    def __str__(self):
        return str(self.User_id)+ ' '+str(self.Book_name)

class NewsFeed(models.Model):
    Description = models.CharField(max_length=1000)
    Current_date = models.DateField(blank=True, null=True)
    Designate_date = models.DateField(blank=True, null=True)
    Created_by = models.CharField(max_length=45, default = None,null = True)
    Created_at = models.DateTimeField(blank=True,null = True, default = None)
    Modified_by = models.CharField(max_length=45, default = None,null = True)
    Modified_at = models.DateTimeField(default=datetime.now, blank=True,null = True)
    def __str__(self):
        return str(self.Description)
