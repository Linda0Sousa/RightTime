from django import forms
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from django.forms import inlineformset_factory

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ["location", "zip_code", "country", "city", "number"]
        
    def save(self, user, commit=True):
        #creates the object but does not saves it
        instance = super().save(commit=False)
        
        #get the user
        user = User.objects.get(id = user.id)
        instance.user = user
        
        if commit:
            instance.save()
        return instance
        
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
        
    def login(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user =  User.objects.get(email=email)
        
        if user:
            if not check_password(password, user.password):
                raise forms.ValidationError("Senha incorreta.")
            
            return user
        
        raise forms.ValidationError("user não existe")
    
            
class StaffForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "email", "password", "phone_number"]
        
    def verify_repetition(self):
        email = self.cleaned_data.get("email")
        phone_number = self.cleaned_data.get("phone_number")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está registrado!")
        if User.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("Este numero já está registrado!")
        return email
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        # puts the role
        instance.role = Role.objects.get(role="staff")
        
        #hashes the password
        instance.password = make_password(self.cleaned_data.get("password"))
        
        if commit:
            instance.save()
        return instance
    
class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ["name", "price", "description", "capacity", "is_active", "weeklySchedule"]
        
    location_name = forms.CharField(label="Nome da localização", max_length=50)
    location_zip = forms.CharField(label="Código Postal", max_length=8)
    location_country = forms.CharField(label="País", max_length=50)
    location_city = forms.CharField(label="Cidade", max_length=50)
    location_number = forms.CharField(label="Número", max_length=10)
        
    def save(self, commit = True):
        location = Location.objects.create(
            location=self.cleaned_data['location_name'],
            zip_code=self.cleaned_data['location_zip'],
            country=self.cleaned_data['location_country'],
            city=self.cleaned_data['location_city'],
            number=self.cleaned_data['location_number']
        )
        
        activity = super().save(commit=False)
        activity.location = location
        activity

        if commit:
            activity.save()
            self.save_m2m()

        return activity