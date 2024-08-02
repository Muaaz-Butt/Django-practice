from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Member
from django.contrib.auth.decorators import login_required
from .forms import MemberForm
# Create your views here.

def main(request) :
    return render(request, 'main.html')

def members(request):
    all_members = Member.objects.all().values()
    context = {
      'all_members' : all_members,
    }
    return render(request, "members.html", context)
  
def details(request, id) :
    member = get_object_or_404(Member, id=id)
    context = {
      'member' : member,
    }
    return render(request, 'details.html', context)
  

@login_required
def create_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('members')
    else:
        form = MemberForm()
    return render(request, 'create_member.html', {'form' : form})
  
@login_required
def update_member(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('members')
    else:
        form = MemberForm(instance=member)
    context = {
        'form' : form,
        'member' : member,
    }
    return render(request, 'update_member.html', context)


@login_required
def delete_member(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        member.delete()
        return redirect('members')
       
    return render(request, 'delete_member.html', {'member': member})