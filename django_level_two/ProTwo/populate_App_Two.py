import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

import random
from faker import Faker
from  AppTwo.models import User

fakegen = Faker()

def populate(N=5):
    for entry in range(N):

        fake_firstname = fakegen.first_name()
        fake_lastname = fakegen.last_name()
        fake_email = fakegen.email()

        users = User.objects.get_or_create(firstname=fake_firstname,lastname=fake_lastname,email=fake_email)[0]

if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('populating complete')
