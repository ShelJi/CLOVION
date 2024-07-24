from django.forms import ModelForm
from hello.models import Wow_model

class Wow_form(ModelForm):
    class Meta:
        model = Wow_model
        fields = "__all__"
