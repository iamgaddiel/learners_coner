from core.models import CustomUser
from uuid import uuid4


for users in CustomUser.objects.all():
    users.id = uuid4
    users.save()
