from django.db import models
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
import alpaca_trade_api as tradeapi




class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='post_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    #def get_absolute_url(self):
	    #return redirect('post-detail', kwargs={'pk': self.pk})
    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
          output_size = (300, 300)
          img.thumbnail(output_size)
          img.save(self.image.path)


    def get_absolute_url(self):
    	return reverse('blog-home')


class Comment(models.Model):
    content = models.TextField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_connected = models.ForeignKey(Post, on_delete=models.CASCADE)

# Okay does the alpaca stuff need to be passed through a model?!


# look up how to pass information from an API through DJANGO
# the model system is just a framework, can be manipulated (as all code can)
class Alpaca(models.Model):
    base_url = 'https://paper-api.alpaca.markets'
    api_key_id = 'PKOKXTI9L8W4SBW41LAW'
    api_secret = 'LQwzw7xKp16scEzdLUDOby9elbeXleWebArNBxCg'

    api = tradeapi.REST(
        base_url=base_url,
        key_id=api_key_id,
        secret_key=api_secret
    )

    account = api.get_account()

    #cashums = account.buying_power()


    # okay does this just not work? How can I put the info on a screen



