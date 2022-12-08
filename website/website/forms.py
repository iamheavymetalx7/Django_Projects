from django import forms

class usersForm(forms.Form):          ##class name will be used in views!
    num1=forms.CharField(label="Value 1", required=False, widget = forms.TextInput(attrs={'class': "form-control"}))                  ##input name
    num2=forms.CharField(label="Value 2",widget = forms.TextInput(attrs={'class': "form-control"}))
    num3=forms.CharField(label="Value 3",widget = forms.TextInput(attrs={'class': "form-control"}))
    email=forms.EmailField()
## more on django fields....