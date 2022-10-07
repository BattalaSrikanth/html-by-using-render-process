from django.shortcuts import render

# Create your views here.
def srikanth(request):
    d={'name':'srikanth','age':21}
    return render(request,'puli.html',d)
