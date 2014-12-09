from django import forms
#from django.forms import ModelForm, Textarea
from django.forms import *
from django.contrib.auth.models import User



class RegistrationForm(ModelForm):
    password_confirmation = CharField(widget= PasswordInput(attrs={
        "placeholder" : "Confirm Password", "name" : "password_confirmation", 
        "class" : "form-control input-sm"}))

    class Meta:
        model = User
        fields = [ 'username', 'password', 'email', 'password_confirmation' ]

        widgets = {
            'username': TextInput(attrs={"placeholder" : "User Name", "name" : "username", 
                "class" : "form-control input-sm"}),
            'email' : EmailInput(attrs={"placeholder" : "Email Address", "name" : "email", 
                "class":"form-control input-sm"}),
            'password': PasswordInput(attrs={"placeholder" : "Password", "name" : "password", 
                "class" : "form-control input-sm"}) 
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.select_related().filter(email = email)
        if user:
            raise forms.ValidationError("Email already present!")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.select_related().filter(username = username)
        if user:
            raise forms.ValidationError("Username already present!")
        return username

    def clean_password_confirmation(self):
        password_confirmation = self.cleaned_data['password_confirmation']
        password = self.cleaned_data['password']
        if password_confirmation != password:
            raise forms.ValidationError("Password not Match")
        return password_confirmation



##########################################################

#class RegistrationForm(forms.Form):
#    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={
#    	"placeholder" : "First Name", "name" : "first_name"}))
#    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={
#   	"placeholder" : "Last Name", "name" : "last_name"}))
#    email = forms.EmailField(label='Email Addres', widget=forms.TextInput(attrs={
#    	"placeholder" : "Email Address", "name" : "email"}))
#    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
#    	"placeholder" : "Password", "name" : "password", "class" : "form-control input-sm"}))
#    password_confirmation = forms.CharField(label='Confirm Password', 
#    	widget=forms.PasswordInput(attrs={
#    		"placeholder" : "Confirm Password", "name" : "password_confirmation", 
#    		"class" : "form-control input-sm" }))


#   def clean_email(self):
#        email = self.cleaned_data['email']
#        user = User.objects.select_related().filter(email = email)
#        if user:
#            raise forms.ValidationError("Email already present!")
#        return email

#    def clean_password_confirmation(self):
#    	password_confirmation = self.cleaned_data['password_confirmation']
#    	password = self.cleaned_data['password']
#    	if password_confirmation != password:
#    		raise forms.ValidationError("Password not Match")
#    	return password_confirmation"""





