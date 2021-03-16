from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Choose(models.Model):
    title= models.CharField(max_length=100,blank=True)
    icon = models.ImageField(blank=True,null=True,verbose_name="Icon Image")
    description= models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Choose Us Info'

    def __str__(self):
        return self.title

class AboutUs(models.Model):
    story = RichTextField(blank=True,null=True)
    pic_1 = models.ImageField(blank=True,null=True,verbose_name="Story Image (Square)")
    mission = RichTextField(blank=True,null=True)
    pic_2 = models.ImageField(blank=True,null=True,verbose_name="Mission Image (Sqaure)")
    # choose_info = RichTextField(blank=True,null=True)
    # pic_3 = models.ImageField(blank=True,null=True)
    #created_at = models.DateTimeField(auto_now_add=True)
    choose = models.ManyToManyField(Choose,blank=True)

    class Meta:
        verbose_name_plural = 'About Us'

class Contact(models.Model):
    full_name = models.CharField(max_length=255,blank=True,null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50,blank=True)
    subject = models.CharField(max_length=255,blank=True)
    message = RichTextField(blank=True,null=True)

    class Meta:
        verbose_name_plural = 'Customer Messages'
