from django.shortcuts import render

# def login_view(request):
#     return render(request, 'accounts/login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == "admin" and password == "password":  # Dummy credentials
            return render(request, 'accounts/login.html', {'message': 'Login successful!'})
        else:
            return render(request, 'accounts/login.html', {'message': 'Invalid credentials!'})
    return render(request, 'accounts/login.html')