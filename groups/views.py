from django.shortcuts import render, redirect, get_object_or_404
from groups.forms import CourseGroupForm
from .models import CourseGroup

# Create your views here.
def groups_list(request):
    groups = CourseGroup.objects.all()
    context = {
        'groups': groups
    }
    return render(request, 'groups/groups_list.html', context)

def group_detail(request, group_id):
    group = get_object_or_404(CourseGroup, id=group_id)
    context = {
        'group': group
    }
    return render(request, 'groups/group_detail.html', context)

def group_create(request):
    if request.method == 'POST':
        form = CourseGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups_list')
    else:
        form = CourseGroupForm()
    return render(request, 'groups/group_form.html', {'form': form})

def group_edit(request, group_id):
    group = get_object_or_404(CourseGroup, id=group_id)
    if request.method == 'POST':
        form = CourseGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('groups_list')
    context = {
        'group': group
    }
    return render(request, 'groups/group_form.html', context)

def group_delete(request, group_id):
    group = get_object_or_404(CourseGroup, id=group_id)
    if request.method == 'POST':
        group.delete()
        return redirect('groups_list')
    context = {
        'group': group
    }
    return render(request, 'groups/group_delete.html', context)