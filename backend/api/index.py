from django.shortcuts import redirect

def home(request):
    context={}
    return redirect("/api");