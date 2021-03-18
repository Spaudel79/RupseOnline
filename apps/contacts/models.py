from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
#from upload_validator import FileTypeValidator

# validator = FileTypeValidator(
#     =['application/msword'],
#     allowed_extensions=['.doc', '.docx']
# )


class Choose(models.Model):
    title= models.CharField(max_length=100,blank=True)
    icon = models.FileField(blank=True,null=True,verbose_name="IconImage(.svg)",)

    # def validate_svg(file, valid):
    #     if not is_svg(file):
    #         raise ValidationError("File not svg")

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

class ContactInfo(models.Model):
    location_1 = models.CharField(max_length=255,blank=True)
    location_2 = models.CharField(max_length=255, blank=True)
    phone_1 = models.CharField(max_length=55,blank=True)
    phone_2 = models.CharField(max_length=55, blank=True)
    email_1 = models.EmailField(blank=True)
    email_2 = models.EmailField(blank=True)
    web_url = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.web_url

    class Meta:
        verbose_name_plural = "RupseOnline Info"




