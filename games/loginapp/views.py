from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    if request.method == "POST":

        username = request.POST.get('username')

        password = request.POST.get('password')

        # return redirect('/index/'))

    return render(request, 'login.html')

def logout(request):
    pass
    return redirect('/index/')

def register(request):
    pass
    return render(request, 'register.html')
