from django.contrib import admin
from mytest.models import GameKind, GameFor
# Register your models here.


class GameKindAdmin(admin.ModelAdmin):

    pass


class GameForAdmin(admin.ModelAdmin):

    pass


admin.site.register(GameKind, GameKindAdmin)

admin.site.register(GameFor, GameForAdmin)
