
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from joblib import load # type: ignore

def home(request):
    return render(request,'homepage.html')

       

def signup(request):
    if request.method == 'POST':
        # Get form data safely using the get() method with default values
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        # Check if required fields are empty
        if not username or not email or not password:
            # Handle case where required fields are missing
            return render(request, 'signup.html', {'error_message': 'Please fill in all required fields'})

        # Create user with provided data
        data = User.objects.create_user(username=username, email=email, password=password)
        data.save()
        return redirect('loginn')  # Redirect to the login page after successful registration
    
    
    # Render the signup form template for GET requests
    return render(request, 'signup.html')


def user_loginmain(request):
    return render(request,'login.html')
    
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            
            auth_login(request, user)  # Log in the user
            return redirect('dashboard')
              # Redirect to the home page after successful login
        else:
            print("Authentication failed")
    return render(request, 'login.html')

def eduloan(request):
    return render(request,'eduloanform.html')

def perloan(request):
    return render(request,'personalloanform.html')

def vehiloan(request):
    return render(request,'vehicleloanform.html')

def dashboard(request):
    return render(request,'dashboard.html')

model=load('./saved_models/decision.joblib')

def predictor(request):
    return render(request,'homeloanform.html')

def logout(request):
    return render(request,'homepage.html')

def formInfo(request):
    
    gender=request.GET['gender']
    
    if(gender=='Male'):
        gender=1.0
    else:
        gender=0.0
        
        
    married=request.GET['married']
    
    if(married=='Yes'):
        married=1.0
    else:
        married=0.0
    
    dependents=request.GET['dependents']
    dependents=float(dependents)
    if(dependents>4.0):
        dependents=4.0
    
    education=request.GET['education']
    
    if(education=='Graduate'):
        education=1.0
    else:
        education=0.0
        
    employed=request.GET['employed']
    
    if(employed=='Yes'):
        employed=1.0
    else:
        employed=0.0
    
    income=request.GET['income']
    income=float(income)
    
    coincome=request.GET['coincome']
    coincome=float(coincome)
    
    loanamount=request.GET['loanamount']
    loanamount=float(loanamount)
    
    loanterm=request.GET['loanterm']
    loanterm=float(loanterm)
    
    history=request.GET['history']
    if(history=='Yes'):
        history=1.0
    else:
        history=0.0
    
    area=request.GET['area']
    
    if(area=='rural'):
        area=0.0
    elif(area=='urban'):
        area=2
    else:
        area=1
    
    
    
    
        
    
    
    print(gender,married,dependents,education,employed,income,coincome,loanamount,loanterm,history,area)
    
    y_predit=model.predict([[gender,married,dependents,education,employed,income,coincome,loanamount,loanterm,history,area]])
    
    print(y_predit)
    
    if(y_predit==0.0 or y_predit==0):
        y_predit=0
    else:
        y_predit=1
        
    if(y_predit==1):
        res="Eligible"
    else:
        res="Not Eligible"
    return render(request,'result.html',{'res':res})


def formInfo_edu(request):
    
    gender=request.GET['gender']
    
    if(gender=='Male'):
        gender=1.0
    else:
        gender=0.0
        
    income=request.GET['income']
    income=float(income)
    
    coincome=request.GET['coincome']
    coincome=float(coincome)
    
    loanamount=request.GET['loanamount']
    loanamount=float(loanamount)

    history=request.GET['history']
    if(history=='Yes'):
        history=1.0
    else:
        history=0.0
    
    employed=request.GET['employed']
    
    if(employed=='Yes'):
        employed=1.0
    else:
        employed=0.0
        
    print(gender,loanamount,employed,income,coincome,history)
    
    y_predit=model.predict([[gender,0.0,0.0,1.0,employed,income,coincome,loanamount,1.0,history,2]])
    
    print(y_predit)
    
    if(y_predit==0.0 or y_predit==0):
        y_predit=0
    else:
        y_predit=1
        
    if(y_predit==1):
        res="Eligible"
    else:
        res="Not Eligible"
    return render(request,'result.html',{'res':res})

def formInfo_vehi(request):
    
    income=request.GET['income']
    income=float(income)
    
    coincome=request.GET['coincome']
    coincome=float(coincome)
    
    loanamount=request.GET['loanamount']
    loanamount=float(loanamount)
    
    loanterm=request.GET['loanterm']
    loanterm=float(loanterm)
    
    history=request.GET['history']
    if(history=='Yes'):
        history=1.0
    else:
        history=0.0
        
    employed=request.GET['employed']
    
    if(employed=='Yes'):
        employed=1.0
    else:
        employed=0.0
        
    gender=request.GET['gender']
    
    if(gender=='Male'):
        gender=1.0
    else:
        gender=0.0
    
    print(gender,employed,loanamount,income,coincome,loanterm,history)
    y_predit=model.predict([[gender,0.0,1.0,1.0,employed,income,coincome,loanamount,loanterm,history,2]])
    
    print(y_predit)
    
    if(y_predit==0.0 or y_predit==0):
        y_predit=0
    else:
        y_predit=1
        
    if(y_predit==1):
        res="Eligible"
    else:
        res="Not Eligible"
    return render(request,'result.html',{'res':res})

def formInfo_per(request):
    
    income=request.GET['income']
    income=float(income)
    
    coincome=request.GET['coincome']
    coincome=float(coincome)
    
    loanamount=request.GET['loanamount']
    loanamount=float(loanamount)
    
    loanterm=request.GET['loanterm']
    loanterm=float(loanterm)
    
    history=request.GET['history']
    if(history=='Yes'):
        history=1.0
    else:
        history=0.0
    
    area=request.GET['area']
    
    if(area=='rural'):
        area=0.0
    elif(area=='urban'):
        area=2
    else:
        area=1
    
    
    employed=request.GET['employed']
    
    if(employed=='Yes'):
        employed=1.0
    else:
        employed=0.0
    
    
    y_predit=model.predict([[1.0,0.0,0.0,1.0,employed,income,coincome,loanamount,loanterm,history,area]])

    print(y_predit)
    
    if(y_predit==0.0 or y_predit==0):
        y_predit=0
    else:
        y_predit=1
        
    if(y_predit==1):
        res="Eligible"
    else:
        res="Not Eligible"
    return render(request,'result.html',{'res':res})