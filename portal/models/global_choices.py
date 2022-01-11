from django.contrib.auth.models import User

USERS = tuple(map(lambda obj: (obj.username, obj.username), User.objects.all()))