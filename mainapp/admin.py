from django.contrib import admin
from .models import Group,Collection_type, Members,Contribution

admin.site.register(Group)
admin.site.register(Collection_type)
admin.site.register(Members)
admin.site.register(Contribution)

