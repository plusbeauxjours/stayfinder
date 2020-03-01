from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """Reservation Admin Definition"""

    list_display = (
        "room",
        "guest",
        "status",
        "check_in",
        "check_out",
        "in_progress",
        "is_finished",
    )

    list_filter = ("status",)


@admin.register(models.BookedDay)
class BokedDayAdmin(admin.ModelAdmin):

    list_display = ("day", "reservation")
