from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.

if __name__ == '__main__':
    user = User.objects.get(id=1)
    print(user.username)

