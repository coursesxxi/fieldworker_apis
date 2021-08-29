from django import forms
from .models import Fieldworker


class FieldworkerForm(forms.ModelForm):

    class Meta:
        model = Fieldworker
        fields = ('first_name','last_name','function')  # ('title',)
        labels = {			  # 'title':'title' 
            'first_name':'name','last_name':'last name','function':'function'
        }


    def __init__(self, *args, **kwargs):
        super(FieldworkerForm,self).__init__(*args, **kwargs)


