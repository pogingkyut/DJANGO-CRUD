from django.shortcuts import render, redirect
from .models import Person

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        query = Person.objects.create(name=name, age=age, gender=gender)
        query.save()
        return redirect('index')
    else:
        data = Person.objects.all()
        context = {
            'data': data,
        }
        return render (request, 'index.html', context)
    
def edit(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        query = Person.objects.get(id=id)
        query.name=name
        query.age=age
        query.gender=gender
        query.save()

        return redirect ('index')
    else:
        data = Person.objects.get(id=id)
        context = {
            'data': data,
        }
        return render (request, 'edit.html', context)
    
def delete(request, id):
    query = Person.objects.get(id=id)
    query.delete()
    return redirect('index')