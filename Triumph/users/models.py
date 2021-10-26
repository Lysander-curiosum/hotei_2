from django.db import models
from django.contrib.auth.models import User, Group
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(default="this is my bio", max_length=140)

    def __str__(self):
        return f'{self.user.username} Profile'

    @property
    def followers(self):
        return Follow.objects.filter(follow_user=self.user).count()

    @property
    def following(self):
        return Follow.objects.filter(user=self.user).count()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
          

class Follow(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    follow_user = models.ForeignKey(User, related_name='follow_user', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

#class Fund(models.Model):
    #creator = models.OneToOneField(User, on_delete=models.CASCADE)
    #image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    #bio = models.TextField(default="Here lieth a company which shall shake the world.", max_length=140)

    #@property
    #def members(self):
     #   return Join.objects.filter(join_fund=self.user).count()

    #def save(self, force_insert=False, force_update=False, using=None,
       #      update_fields=None):
        #super().save()

        #img = Image.open(self.image.path)
       # if img.height > 300 or img.width > 300:
      #      output_size = (300, 300)
     #       img.thumbnail(output_size)
    #        img.save(self.image.path)

#class Join(models.Model):
 #   user = models.ForeignKey(User, related_name='members', on_delete=models.CASCADE)
  #  join_fund = models.ForeignKey(User, related_name='join_fund', on_delete=models.CASCADE)
   # date = models.DateTimeField(auto_now_add=True)
