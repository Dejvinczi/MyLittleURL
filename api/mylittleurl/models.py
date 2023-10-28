import random
import string

from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.conf import settings
from django.db import models

# Vars for set little url length (min, max)
LITTLE_URL_MIN_LENGTH = 5
LITTLE_URL_MAX_LENGTH = 10


def generate_unique_little_url():
    '''
    Function to generate little url
    '''
    while True:
        length = random.randint(LITTLE_URL_MIN_LENGTH, LITTLE_URL_MAX_LENGTH)
        little_url = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        if not LittleURL.objects.filter(little_url=little_url).exists():
            return little_url


class LittleURL(models.Model):
    ''''
    Main model, ordering set on created_dt field. Use min and max validators for little_url length
    '''
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    raw_url = models.URLField()
    little_url = models.CharField(unique=True, validators=[MinLengthValidator(LITTLE_URL_MIN_LENGTH), 
                                                           MaxLengthValidator(LITTLE_URL_MAX_LENGTH)], 
                                  blank=True, default=generate_unique_little_url)
    created_dt = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['created_dt']
