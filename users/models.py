from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.conf import settings
# from datetime import date
from django.contrib.auth.models import User


# ! 1- Normal django user modelindeki bilgileri geliştirmek istersek Useri import edebiliriz, user içinde birkaç override yöntemiyle bu işlem yapılabilir 
# ! bunlardan biri MyUser(AbstractUser)  i kullanabiliriz.aşağıda user tablosuna istediğimiz sütunları ekleyebliriz.
# ! bunub için settings kısmına ,settings parçalara ayrılmışsaa base.py ye  # AUTH_USER_MODEL = 'users.MyUser'  eklenir. jangoya artık user tablosu içimn bunu kullan dedik
# ? aynı işlemi  MyUser(AbstractUser) in bir üstü olan   MyUser(AbstractBaseUser) den de yaparız çok uzar !!!!
# * 2- 2.yöntem olarak yeni bir tablo oluşturup oneToone olarak user tablosuyla ilişkilendiririz bu daha pratik olur. 
# * Bu projede bu şekilde profile tablosu oluşturuldu  TABLO USERLE İLGİLİ O YÜZDEN BURAYA YAZDIK


# class MyUser(AbstractUser):
#   username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
#   email = models.EmailField(('email address'), unique = True)
#   native_name = models.CharField(max_length = 5)
#   phone_no = models.CharField(max_length = 10)
#   USERNAME_FIELD = 'email'
#   REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
  
#   def __str__(self):
#       return "{}".format(self.email)



    # MEDIA_URL = '/media/'
    # MEDIA_ROOT = BASE_DIR / "pictures"
# * GÖRSEL İŞLEMLER İÇİN YUKARIDAKİ KISIMLARI SETTİNGSE/YADA BASE/ EKLEYELİM
# * 
# * 
# * 
# * 


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=30, blank=True, null=True)
    avatar = models.ImageField(upload_to="pictures", default="avatar.png") ## img lerin yükleneceği klasörü belirledik
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile'"
    

