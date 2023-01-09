from django import forms
from django.forms import Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from gallery.models import *
from django.contrib.auth.forms import AuthenticationForm

from django.forms import ClearableFileInput, Select, ModelForm, DateTimeInput, Textarea, CharField, TextInput, Select, NumberInput, PasswordInput, FileInput, FileField

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Имя', widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form_input',
            'placeholder': 'name',
            'required': True
        }
    ))

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={
            'type': 'password',
            'class': 'form_input',
            'placeholder': 'password',
            'required': True
        }
    ))

    password2 = forms.CharField(label='Повторить пароль', widget=forms.PasswordInput(
        attrs={
            'type': 'password',
            'class': 'form_input',
            'placeholder': 'repeat password',
            'required': True
        }
    ))
    email = forms.CharField(label='Почта', widget=forms.EmailInput(
        attrs={
            'type': 'email',
            'class': 'form_input',
            'placeholder': 'email',
            'required': False
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form_input',
            'placeholder': 'name',
            'required': True
        }
    ))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={
            'type': 'password',
            'class': 'form_input',
            'placeholder': 'password',
            'required': True
        }
    ))


class ExhibitionForm(ModelForm):
    class Meta:
        model = Exhibition
        fields = ['title', 'description', 'date_and_time']
        widgets = {'title': TextInput(attrs={
            'class': 'form_input',
            'placeholder': 'title',
            'required': True
            }),
            'description': Textarea(attrs={
                'class': 'form_input',
                'placeholder': 'description',
                'required': True
            }),
            'date_and_time': DateTimeInput(
                                attrs={
                                    'class': 'form_input',
                                    'placeholder': '31/01/2022 11:11',
                                    # 'format': '%d/%m/%Y %H:%M',
                                    'required': True
                                })
            # 'images': FileField(widget=forms.ClearableFileInput(attrs={
            #     'multiple': True,
            #     'class': 'form_input',
            #     'placeholder': 'images',
            #     'required': False
            # }))
        }

class Exhibition_museum_pieceForm(ModelForm):
    class Meta:
        model = Exhibition_museum_piece
        fields = ['museum_piece_id']
        widgets = {
            'museum_piece_id': Select(attrs={
                'class': 'form_input',
                'required': False
            })
        }

class Museum_pieceForm(ModelForm):
    class Meta:
        model = Museum_piece
        fields = ['piece_name', 'description', 'date_of_creation', 'piece_type', 'author_id', 'hall_id']
        widgets = {'piece_name': TextInput(attrs={
            'class': 'form_input',
            'placeholder': 'piece_name',
            'required': True
            }),
            'description': Textarea(attrs={
                'class': 'form_input',
                'placeholder': 'description',
                'required': True
            }),
            'date_of_creation': DateTimeInput( attrs={
                    'class': 'form_input',
                    'placeholder': '31/01/2022 11:11',
                    # 'format': '%d/%m/%Y %H:%M',
                    'required': True
            }),
            'piece_type': TextInput(attrs={
                'class': 'form_input',
                'placeholder': 'type',
                'required': True
            }),
            'author_id': Select(attrs={
                'class': 'form_input',
                'required': False,
            }),
            'hall_id': Select(attrs={
                'class': 'form_input',
                'required': True
            })
            # 'images': FileField(widget=forms.ClearableFileInput(attrs={
            #     'multiple': True,
            #     'class': 'form_input',
            #     'placeholder': 'images',
            #     'required': False
            # }))
        }


class ImagesForm(ModelForm):
    class Meta:
        model = Images
        fields = ['image']
        widgets = {'image': ClearableFileInput(
                    attrs={
                        'multiple': True,
                        'class': 'form_input',
                        'placeholder': 'images',
                        'required': False
                    })}


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['full_name']
        widgets = {'full_name': TextInput(attrs={
            'class': 'form_input',
            'placeholder': 'full name',
            'required': True
            })
        }

class HallForm(ModelForm):
    class Meta:
        model = Hall
        fields = ['hall_number', 'title']
        widgets = {'hall_number': TextInput(attrs={
            'class': 'form_input',
            'placeholder': 'hall number',
            'required': True
            }),
            'title': TextInput(attrs={
                'class': 'form_input',
                'placeholder': 'title',
                'required': False
            })
        }


class VisitForm(ModelForm):
    class Meta:
        model = Visitor
        fields = ['full_name', 'phone_number', 'email']
        widgets = {'full_name': TextInput(attrs={
            'class': 'form_input',
            'placeholder': 'name',
            'required': False
            }),
            'phone_number': TextInput(attrs={
                'class': 'form_input',
                'placeholder': 'phone number',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form_input',
                'placeholder': 'email',
                'required': False
            })
        }

class ExhibitionVisitForm(ModelForm):
    class Meta:
        model = Exhibition_visitor
        fields = ['exhibition_id']
        widgets = {
            'exhibition_id': Select(attrs={
                'class': 'form_input',
                'required': False
            })
        }