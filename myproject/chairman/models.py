from django.db import models
from django.utils import timezone 
import math

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 20)
    otp = models.IntegerField(default = 459)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    role = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return self.email

class MemberDetails(models.Model):
    homeno = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    job_profession = models.CharField(max_length=50,blank=True)
    job_address = models.CharField(max_length=200,blank=True)
    vehicle_type = models.CharField(max_length=20,blank=True)
    vehicle_no = models.CharField(max_length=30,blank=True)
    blood_group = models.CharField(max_length=30,blank=True)
    family_member_details = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=30)

    def __str__(self):
        return self.homeno

class Chairman(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    m_id = models.ForeignKey(MemberDetails,on_delete=models.CASCADE)
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    profile_pic = models.FileField(upload_to='img/',blank=True,default='default.jpg')

    def __str__(self):
        return self.fname

class Member(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    m_id = models.ForeignKey(MemberDetails,on_delete=models.CASCADE)
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    profile_pic = models.FileField(upload_to='img/',blank=True,default='default.jpg')

    def __str__(self):
        return self.fname


class Notice(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    m_id = models.ForeignKey(Member,on_delete=models.CASCADE,null=True)
    c_id = models.ForeignKey(Chairman,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True,blank=False)

    def __str__(self):
        return self.title

    def whenpublished(self):
        now = timezone.now()  
        diff= now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            if seconds == 1:
                return str(seconds) +  "second ago"
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)
            if minutes == 1:
                return str(minutes) + " minute ago"
            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)
            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
            if days == 1:
                return str(days) + " day ago"
            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years= math.floor(diff.days/365)
            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"

class Event(models.Model):
    event_title = models.CharField(max_length=50)
    event_desc = models.CharField(max_length=200)
    event_pic = models.FileField(upload_to='img/',blank=True,default='defaultpic.jpg')
    event_date = models.DateField(blank=True)
    event_time = models.TimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True,blank=False)

    def __str__(self):
        return self.event_title

    def whenpublished(self):
        now = timezone.now()  
        diff= now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            if seconds == 1:
                return str(seconds) +  "second ago"
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)
            if minutes == 1:
                return str(minutes) + " minute ago"
            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)
            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
            if days == 1:
                return str(days) + " day ago"
            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years= math.floor(diff.days/365)
            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"

class Complaint(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    m_id = models.ForeignKey(Member,on_delete=models.CASCADE, blank=True, null=True)
    cid = models.ForeignKey(Chairman,on_delete=models.CASCADE, blank=True, null=True)
    complaint_subject = models.CharField(max_length=50)
    complaint_desc = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True,blank=False)

    def __str__(self):
        return self.complaint_subject

    def whenpublished(self):
        now = timezone.now()  
        diff= now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            if seconds == 1:
                return str(seconds) +  "second ago"
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)
            if minutes == 1:
                return str(minutes) + " minute ago"
            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)
            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
            if days == 1:
                return str(days) + " day ago"
            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years= math.floor(diff.days/365)
            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"

class Suggestions(models.Model):
    suggested_by = models.CharField(max_length=50)
    suggestion_title = models.CharField(max_length=50)
    suggestion_desc = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True,blank=False)


    def __str__(self):
        return self.suggestion_title

    def whenpublished(self):
        now = timezone.now()  
        diff= now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            if seconds == 1:
                return str(seconds) +  "second ago"
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)
            if minutes == 1:
                return str(minutes) + " minute ago"
            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)
            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
            if days == 1:
                return str(days) + " day ago"
            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years= math.floor(diff.days/365)
            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"

class Image(models.Model):
    name = models.CharField(max_length=20)
    imagefile = models.FileField(upload_to='images/',default='defaultset.jpg')

    def __str__(self):
        return self.name

    
class Video(models.Model):
    name = models.CharField(max_length=20)
    videofile = models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name

class Maintenance(models.Model):  
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    member_id = models.ForeignKey(Member,on_delete=models.CASCADE, blank=True, null=True)
    cid = models.ForeignKey(Chairman,on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True)
    amount = models.CharField(max_length=2000, blank=True)
    due_date = models.DateTimeField(auto_now_add=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    status=models.CharField(max_length=30,default="Pending")

    def __str__(self):
        return self.title

    def whenpublished(self):
        now = timezone.now()  
        diff= now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            if seconds == 1:
                return str(seconds) +  "second ago"
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)
            if minutes == 1:
                return str(minutes) + " minute ago"
            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)
            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
            if days == 1:
                return str(days) + " day ago"
            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years= math.floor(diff.days/365)
            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"


class Watchman(models.Model):
    c_id = models.ForeignKey(Chairman,on_delete=models.CASCADE,blank=True,null=True)
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    role=models.CharField(max_length=20,blank=True)
    email=models.EmailField(max_length=30,unique=True)
    password=models.CharField(max_length=30,blank=True)
    otp = models.IntegerField(default = 459)
    address=models.CharField(max_length=200,blank=True)
    contact_no=models.CharField(max_length=20,blank=True)
    family_contact_no=models.CharField(max_length=20,blank=True)
    age=models.CharField(max_length=30,blank=True)
    profile_picture=models.FileField(upload_to='img/',default="defaultpicw.jpg")
    status=models.CharField(max_length=30,default="Pending")
    
    def __str__(self):
        return self.fname

class Visitor(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    m_id = models.ForeignKey(MemberDetails,on_delete=models.CASCADE,blank=True,null=True)
    mem_id = models.ForeignKey(Member,on_delete=models.CASCADE,blank=True,null=True)
    c_id = models.ForeignKey(Chairman,on_delete=models.CASCADE,blank=True,null=True)
    v_homeno = models.CharField(max_length=20)
    v_name = models.CharField(max_length=50)
    v_mobile_no = models.CharField(max_length=20)
    v_date = models.DateField()
    v_time = models.TimeField()
    reason = models.CharField(max_length=50)

    def __str__(self):
        return self.v_name

class Transaction(models.Model):
    main_id = models.ForeignKey(Maintenance, on_delete=models.CASCADE, blank=True, null=True, default="")
    made_by = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, null=True, default="")
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=30, default="Pending")

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)

    # def __str__(self):
    #     return self.made_by