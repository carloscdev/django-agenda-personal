from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.contrib import messages

def index(request):
    contacts = Contact.objects.filter(name__contains=request.GET.get('search', '')).order_by('-is_favorite')

    context = {
        'contacts': contacts
    }
    return render(request, 'views/contact/index.html', context)

def detail(request, id):
    contact = Contact.objects.get(id=id)

    context = {
        'contact': contact
    }
    return render(request, 'views/contact/detail.html', context)

def update(request, id):
    contact = Contact.objects.get(id=id)

    if request.method == 'GET':
        form = ContactForm(instance=contact)
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'views/contact/update.html', context)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
            'id': id
        }
        messages.success(request, 'Contacto actualizado correctamente')
        return render(request, 'views/contact/update.html', context)

def create(request):
    if request.method == 'GET':
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'views/contact/create.html', context)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        context = {
            'form': form
        }
        return redirect('contact')

def delete(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()

    return redirect('contact')