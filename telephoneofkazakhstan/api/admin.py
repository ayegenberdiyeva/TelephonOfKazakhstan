from django.contrib import admin
from .models import User, TariffPlan, UserTariff, Transaction

admin.site.register(User)
admin.site.register(TariffPlan)
admin.site.register(UserTariff)
admin.site.register(Transaction)
