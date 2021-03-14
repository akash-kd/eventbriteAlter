from django.shortcuts import render
from .models import post
from .forms import postForm
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
# Create your views here.

def home(request):
    context = {}
    return render(request,'main/base.html',context)

class PostView(FormView):
    form_class = postForm
    template_name = "main/post_list.html"
    success_url ="/"