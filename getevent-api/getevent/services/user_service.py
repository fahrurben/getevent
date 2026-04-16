from django.db import transaction

from getevent.models import BaseUser


@transaction.atomic
def user_create(*, email: str, password: str) -> BaseUser:
    user = BaseUser.objects.create_user(email=email, password=password)

    return user
