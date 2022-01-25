from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_detail(request):

    return render(request,'post/postlist.html')

