from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm
# Create your views here.

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


def new_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return HttpResponse('Thanks! Your event has been added.')
    else:
        form = EventForm()
    return render(request, 'new_event.html', {'form': form, 'type_of_request': 'Create'})

def update_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return HttpResponse('Thanks! Your event has been updated.')
    else:
        form = EventForm(instance=event)
    return render(request, 'new_event.html', {'form': form, 'type_of_request': 'Update'})

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)
    event.delete()
    return redirect('event_list')