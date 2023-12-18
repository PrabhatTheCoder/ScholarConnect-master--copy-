
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout
from .forms import CustomUserForm, StudentForm
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .models import *
# Create your views here.


from django.contrib.auth.hashers import make_password

def register_student(request):
    if request.method == 'POST':
        user_form = CustomUserForm(request.POST)
        student_form = StudentForm(request.POST)

        # Check if both forms are valid
        if user_form.is_valid() and student_form.is_valid():
            # Save the user form with user_type set to 1 for students
            user = user_form.save(commit=False)
            user.user_type = 1  # Assuming 1 represents the "Student" user type
            user.password = make_password(user_form.cleaned_data['password'])  # Manually hash the password
            user.save()

            # Save the student form with the user instance
            student = student_form.save(commit=False)
            student.user = user
            student.save()

            return HttpResponseRedirect(reverse("users:registration_success"))

    else:
        user_form = CustomUserForm()
        student_form = StudentForm()

    return render(request, 'users/register.html', {'user_form': user_form, 'student_form': student_form})



def registration_success(request):
    print('it worked')
    print(request.user)
    return render(request, 'users/registration_success.html')


def Scholar_application(request):
    if request.method == "POST":
        
        data = request.POST
        
        applicant_photo = request.FILES.get('applicant_photo')
        domicile_certificate = request.FILES.get('applicant_photo')
        income_certficate = request.FILES.get('income_certficate')
        caste_certificate = request.FILES.get('caste_certificate')
        aadhar_card = request.FILES.get('aadhar_card')
        bonafide = request.FILES.get('bonafide')
        fee_receipt = request.FILES.get('fee_receipt')
        passbook = request.FILES.get('passbook')
        
        institute_state = data.get('institute_state')
        institute_name = data.get('institute_name')
        
        applicant_name = data.get('applicant_name')
        father_name = data.get('father_name')
        mother_name = data.get('mother_name')
        gender = data.get('gender')
        annual_income = data.get('annual_income')
        category = data.get('category')
        religion = data.get('religion')
        course = data.get('course')
        enrollment = data.get('enrollment')
        adm_year = data.get('adm_year')
        pr_year = data.get('pr_year')
        mode = data.get('mode')
        pre_board = data.get('pre_board')
        prev_class = data.get('prev_class')
        pass_year = data.get('pass_year')
        disabled = data.get('disabled')
        parents_profession = data.get('parents_profession')
        acc_no = data.get('acc_no')
        ifsc = data.get('ifsc')
        
        student = Student.objects.create(
            
            applicant_name = applicant_name,
            father_name = father_name,
            mother_name = mother_name,
            gender = gender,
            annual_income = annual_income,
            category = category,
            religion = religion,
            course = course,
            enrollment = enrollment,
            adm_year = adm_year,
            pr_year = pr_year,
            mode = mode,
            pre_board = pre_board,
            prev_class = prev_class,
            pass_year = pass_year,
            disabled = disabled,
            parents_profession = parents_profession,
            acc_no = acc_no,
            ifsc = ifsc,
            
            institute_name = institute_name,
            
            applicant_photo = applicant_photo,
            domicile_certificate = domicile_certificate,
            income_certficate = income_certficate,
            caste_certificate = caste_certificate,
            aadhar_card = aadhar_card,
            bonafide = bonafide,
            fee_receipt = fee_receipt,
            passbook = passbook,
        )

        
        

    



def student_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print('working')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            print('working')
            if user is not None:
                login(request, user)
                print('login working')
                print(user.user_type)
                if user.user_type == 1:
                    print(' a student logged in')
                    return HttpResponseRedirect(reverse('scholar:dashboard'))

            else:
                messages.error(request, 'Invalid username or password.')

    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})



def student_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:student_login'))