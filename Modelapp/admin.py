from django.contrib import admin
from .models import Students
from .models import Teacher
from .models import Parents
from .models import Post


admin.site.register(Students)
admin.site.register(Teacher)
admin.site.register(Parents)
admin.site.register(Post)


# Register your models here.
