from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


class ZapisForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(ZapisForm, self).__init__(*args, **kwargs)
        self.user = user
        self.fields['doctor'] = forms.ModelChoiceField(
            queryset=Doctor.objects.all(), initial=True,
            widget=forms.Select(attrs={"class": "form-control", }, ))
        self.fields['patient'] = forms.ModelChoiceField(
            queryset=Patient.objects.filter(user=self.user), initial=True,
            widget=forms.Select(attrs={"class": "form-control", }, ))

    class Meta:
        model = Zapis
        fields = ('doctor', 'patient', 'data')
        widgets = {

            "data": forms.DateTimeInput(attrs={"class": "form-control", "placeholder": "Күн.Ай.Жыл САҒ:МИН", }),

        }


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = '__all__'
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Есіміңіз"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Тегіңіз"}),
            "department": forms.TextInput(attrs={"class": "form-control", "placeholder": "Терапия, Травматология ..."}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "+77771234567"}),
            "date": forms.DateInput(attrs={"class": "form-control", "placeholder": "Күн", 'type': 'date'}),
            "time": forms.TimeInput(attrs={"class": "form-control", "placeholder": "Уақыт", 'type': 'time'}),
            "question": forms.Textarea(
                attrs={"class": "form-control", "cols": 30, "rows": 2, "placeholder": "Сұрағыңыз"}),

        }


class DoctorAtHomeForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(DoctorAtHomeForm, self).__init__(*args, **kwargs)
        self.user = user
        self.fields['doctor'] = forms.ModelChoiceField(
            queryset=Doctor.objects.all(), initial=True,
            widget=forms.Select(attrs={"class": "form-control", }, ))
        self.fields['patient'] = forms.ModelChoiceField(
            queryset=Patient.objects.filter(user=self.user), initial=True,
            widget=forms.Select(attrs={"class": "form-control", }, ))

    class Meta:
        model = DoctorAtHome
        fields = ('doctor', 'patient', 'address', 'data',)
        widgets = {
            'address': forms.TextInput(attrs={"class": "form-control", "placeholder": "Мекен-жай", }),
            "data": forms.DateTimeInput(attrs={"class": "form-control", "placeholder": "Күн.Ай.Жыл САҒ:МИН", }),

        }


class AccountLoginForm(forms.ModelForm):
    login = forms.CharField(label='Логин',
                            widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Логин"}))
    password = forms.CharField(label='password',
                               widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Құпия сөз"}))

    class Meta:
        model = User
        fields = ('login', 'password',)


class AccountSignupForm(UserCreationForm):
    GENDER_CHOICE = (
        ('Ер', 'Ер'),
        ('Әйел', 'Әйел'),
    )
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Логин"}))
    password1 = forms.CharField(label='password1',
                                widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Құпия сөз"}))
    password2 = forms.CharField(label='password2',
                                widget=forms.PasswordInput(
                                    attrs={"class": "form-control", "placeholder": "Құпия сөзді қайталаңыз"}))
    first_name = forms.CharField(label='Есімі',
                                 widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Есіміңіз"}))
    last_name = forms.CharField(label='Тегі',
                                widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Тегіңіз"}))

    phone = forms.CharField(label='Телефон',
                            widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Телефон"}))

    email = forms.EmailField(label='Email',
                             widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"}))
    jsn = forms.CharField(label='ЖСН',
                          widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "ЖСН"}))
    birthday = forms.DateField(label='Туылған күн', widget=forms.DateInput(
        attrs={"class": "form-control", "placeholder": "Туылған күніңіз", "type": "date"}))
    gender = forms.ChoiceField(label='Жынысы', choices=GENDER_CHOICE,
                               widget=forms.Select(
                                   attrs={"class": "form-control", "placeholder": "Жынысыңыз"}))
    national = forms.CharField(label='Ұлты',
                               widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ұлтыңыз"}))
    address = forms.CharField(label='Мекен-жай',
                              widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Мекен-жайыңыз"}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'phone', 'email',
                  'jsn', 'gender', 'national', 'address', 'birthday',
                  )


class ZapisDoctorForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(ZapisDoctorForm, self).__init__(*args, **kwargs)
        self.user = user
        self.fields['doctor'] = forms.ModelChoiceField(
            queryset=Doctor.objects.filter(user=self.user.patient.doctor.user), initial=True,
            widget=forms.Select(attrs={"class": "form-control", }, ))
        self.fields['patient'] = forms.ModelChoiceField(
            queryset=Patient.objects.filter(user=self.user), initial=True,
            widget=forms.Select(attrs={"class": "form-control", }, ))

    class Meta:
        model = Zapis
        fields = ('doctor', 'patient', 'data')
        widgets = {

            "data": forms.DateTimeInput(attrs={"class": "form-control", "placeholder": "Күн.Ай.Жыл САҒ:МИН", }),

        }


class DoctorAtHomePatientForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(DoctorAtHomePatientForm, self).__init__(*args, **kwargs)
        self.user = user
        self.fields['doctor'] = forms.ModelChoiceField(
            queryset=Doctor.objects.filter(user=self.user.patient.doctor.user), initial=True,
            widget=forms.Select(attrs={"class": "form-control", "readonly": "readonly", }, ))
        self.fields['patient'] = forms.ModelChoiceField(
            queryset=Patient.objects.filter(user=self.user), initial=True,
            widget=forms.Select(attrs={"class": "form-control", "readonly": "readonly", }, ))
        self.fields['address'].initial = self.user.patient.address

    class Meta:
        model = DoctorAtHome
        fields = ('doctor', 'patient', 'address', 'data',)
        widgets = {
            'address': forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Мекен-жай", "readonly": "readonly"}),
            "data": forms.DateTimeInput(attrs={"class": "form-control", "placeholder": "Күн.Ай.Жыл САҒ:МИН", }),

        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('first_name', 'last_name', 'message')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Есіміңіз'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тегіңіз'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Хабарлама мәтіні'})
        }
