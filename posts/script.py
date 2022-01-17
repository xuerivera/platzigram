from datetime import date

from django.db.models.fields import EmailField
from posts.models import User

users = [
    {
        'username': 'maniaco',
        'first_name': 'Maniaco',
        'last_name': 'Ramirez',
        'email': 'mani@co.com',
        'password': '12345678',
        'birth_date': date(1990, 1, 1),
        'is_admin': True,
    },
    {
        'username': 'juan',
        'first_name': 'Juanico',
        'last_name': 'Perez',
        'email': 'juan@mi.com',
        'password': '12345678',
        'birth_date': date(1990, 1, 1),
        'is_admin': False,
    },
    {
        'username': 'smith',
        'first_name': 'Smith',
        'last_name': 'Cena',
        'email': 'smith@th.com',    
        'password': '12345678',
        'birth_date': date(1990, 1, 1),
        'is_admin': False,
    }
    ]


for i in users:
    user = User(**i)
    user.save()
    print(user.pk, user.username, user.email)