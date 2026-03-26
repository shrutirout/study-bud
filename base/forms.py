from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, Textarea, FileInput
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'name': TextInput(attrs={'class': 'form__input', 'placeholder': 'Enter your name'}),
            'username': TextInput(attrs={'class': 'form__input', 'placeholder': 'Enter a username'}),
            'email': EmailInput(attrs={'class': 'form__input', 'placeholder': 'Enter your email'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form__input'})


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Room name...'}),
            'description': Textarea(attrs={'placeholder': 'Add a description...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form__input'})


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Display name...'}),
            'username': TextInput(attrs={'placeholder': 'Username...'}),
            'email': EmailInput(attrs={'placeholder': 'Email address...'}),
            'bio': Textarea(attrs={'placeholder': 'Tell us about yourself...'}),
            'avatar': FileInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form__input'})
