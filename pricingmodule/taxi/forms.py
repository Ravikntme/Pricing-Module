from .models import *
from django.forms import ModelForm

class RatesForm(ModelForm):
    class Meta:
        model = Rates
        fields = '__all__'
        labels = {
            'dbp': 'Distance Base Price',
            'tbp': 'Time Base Price',
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(RatesForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'