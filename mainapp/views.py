from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import ConsultationForm, ZapisForm, DoctorAtHomeForm, AccountLoginForm, AccountSignupForm, \
    DoctorAtHomePatientForm, ZapisDoctorForm, FeedbackForm
from .models import *


def home(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('home')
    form = ConsultationForm()
    if request.user.is_authenticated:
        if request.method == 'POST':
            form_call = DoctorAtHomeForm(user=request.user, data=request.POST)
            if form_call.is_valid():
                form_call = form_call.save(commit=False)
                form_call.save()
                return redirect('home')
        form_call = DoctorAtHomeForm(user=request.user)

        if request.method == 'POST':
            form_zapis = ZapisForm(user=request.user, data=request.POST)
            if form_zapis.is_valid():
                form_zapis = form_zapis.save(commit=False)
                form_zapis.save()
                return redirect('home')
        form_zapis = ZapisForm(user=request.user)
    else:
        form_zapis = ''
        form_call = ''

    context = {
        'title': 'Басты бет',
        'form': form,
        'form_zapis': form_zapis,
        'form_call': form_call,
    }
    return render(request, 'mainapp/home.html', context)


# admin
# tolqyn
# tolqynuser

def record(request):
    records = Zapis.objects.filter(patient=request.user.patient).order_by('-created')

    context = {
        'title': 'Жазылымдар',
        'records': records,
    }
    return render(request, 'mainapp/records.html', context)


def card(request):
    context = {"title": "Медкарта"}
    return render(request, 'mainapp/card.html', context)


def call_district_doctor(request):
    if request.method == 'POST':
        form = DoctorAtHomePatientForm(user=request.user, data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('home')
    form = DoctorAtHomePatientForm(user=request.user)
    context = {"title": "Учаскелік дәрігерді шақыру", "form": form}
    return render(request, 'mainapp/call_district_doctor.html', context)


def record_district_doctor(request):
    if request.method == 'POST':
        form = ZapisDoctorForm(user=request.user, data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('home')
    form = ZapisDoctorForm(user=request.user)

    context = {'title': 'Учаскелік дәрігерге жазылу', 'form': form}
    return render(request, 'mainapp/record_district_doctor.html', context)


def data(request):
    doctorathome = DoctorAtHome.objects.filter(patient=request.user.patient).order_by('-created')[:1]
    zapis = Zapis.objects.filter(patient=request.user.patient).order_by('-created')[:1]
    consultation = Consultation.objects.all()[:1]
    context = {
        'title': 'Медициналық деректер',
        'doctorathome': doctorathome,
        'zapis': zapis,
        'consultation': consultation,
    }
    return render(request, 'mainapp/data.html', context)


def account_login(request):
    if request.method == 'POST':
        form = AccountLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['login']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            login(request, user)

            return redirect('home')
    else:
        form = AccountLoginForm()

    return render(request, 'account/login.html', {'form': form})


def account_signup(request):
    error = ''
    if request.method == 'POST':
        form = AccountSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            Patient.objects.create(user=user,
                                   first_name=form.cleaned_data['first_name'],
                                   last_name=form.cleaned_data['last_name'],
                                   phone=form.cleaned_data['phone'],
                                   email=form.cleaned_data['email'],
                                   jsn=form.cleaned_data['jsn'],
                                   birthday=form.cleaned_data['birthday'],
                                   gender=form.cleaned_data['gender'],
                                   national=form.cleaned_data['national'],
                                   address=form.cleaned_data['address'],
                                   )
            return redirect('home')
        else:
            error = 'Форма дұрыс толтырылмады'

    else:
        form = AccountSignupForm()
    context = {'form': form, 'error': error}
    return render(request, 'account/signup.html', context)


def feedback(request):
    feedbacks = Feedback.objects.all()
    if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback_form = feedback_form.save(commit=False)
            feedback_form.save()
            return redirect('home')

    feedback_form = FeedbackForm()
    context = {'title': 'Пікірлер', 'feedback_form': feedback_form, 'feedbacks': feedbacks}
    return render(request, 'mainapp/feedback.html', context)
