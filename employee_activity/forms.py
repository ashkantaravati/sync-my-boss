from django.forms import ModelForm
from .models import AvailabilityStatus


class AvailabilityStatusForm(ModelForm):
    class Meta:
        model = AvailabilityStatus
        fields = ["reason", "until"]
