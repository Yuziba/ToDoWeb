from django import forms
from .models import Model_ToDoWeb


class TodoForm(forms.ModelForm):
    class Meta:
        model = Model_ToDoWeb
        fields = "__all__"


        #sTarih alanını Kullanıcıya seçtirecek şekilde açılır tarih alanı oluşturduk
        widgets = {
            'date':forms.DateInput(attrs={'type':'date'}),
        }