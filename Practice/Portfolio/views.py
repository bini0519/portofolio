from django.shortcuts import render,redirect,get_object_or_404
from .forms import Ppform, CommentForm
from .models import Mission
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')


def detail(request):  
    my_pp = get_object_or_404(Mission, pk=jss_id)
    comment_form = CommentForm()
    return render(request, 'detail.html',{'my_pp':my_pp, 'comment_form':comment_form})


def create_comment(request):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        temp_form = comment_form.save(commit=False)
        temp_form.author = request.user
        temp_form.jasoseal = Mission.objects.get(pk=jss_id)
        temp_form.save()
        return redirect('detail')

def delete_comment(request):
    my_comment = Comment.objects.get(pk=comment_id)
    if request.user == my_comment.author:
        my_comment.delete()
        return redirect('detail')
    else:
        raise PermissionDenied