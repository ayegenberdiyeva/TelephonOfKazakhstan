from django.contrib import admin
from .models import User, TariffPlan, UserTariffPlan, Transaction

admin.site.register(User)
admin.site.register(TariffPlan)
admin.site.register(UserTariffPlan)
admin.site.register(Transaction)
