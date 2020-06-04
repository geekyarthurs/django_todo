from django import forms
from todo.models import Todo


class AddTodo(forms.ModelForm):
    text = forms.CharField(
        max_length=100,
        label='',
        widget=forms.TextInput(attrs={
            'size': '145',
            'style': 'line-height:35px',
            'class': 'ml-3',
            'autocomplete' : 'off'
        }))

    class Meta:
        model = Todo
        fields = ('text', )
