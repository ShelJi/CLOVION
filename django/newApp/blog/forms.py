# from .forms import ModelForm
from blog.models import blogData, blogUser
    
class blogDataForm(forms.ModelForm):
    class Meta:
        model = blogData
        fields = __all__

class blogUserForm(forms.ModelForm):
    class Meta:
        model = blogUser
        fields = __all__
