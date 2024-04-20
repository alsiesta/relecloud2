from django.shortcuts import render
from django.urls import reverse_lazy
from . import models
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from .forms import DestinationForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def destinations(request):
    all_destinations = models.Destination.objects.all()
    return render(request, 'destinations.html', { 'destinations': all_destinations})

class DestinationDetailView(generic.DetailView):
    template_name = 'destination_detail.html'
    model = models.Destination
    context_object_name = 'destination'

class DestinationCreateView(generic.CreateView):
    template_name = 'destination_form.html'
    model = models.Destination
    form_class = DestinationForm

class DestinationUpdateView(generic.UpdateView):
    template_name = 'destination_form.html'
    model = models.Destination
    form_class = DestinationForm

class DestinationDeleteView(generic.DeleteView):
    template_name = 'destination_confirm_delete.html'
    model = models.Destination
    success_url = reverse_lazy('destinations')

class CruiseDetailView(generic.DetailView):
    template_name = 'cruise_detail.html'
    model = models.Cruise
    context_object_name = 'cruise'

class InfoRequestCreate(SuccessMessageMixin, generic.CreateView):
    template_name = 'info_request_create.html'
    model = models.InfoRequest
    fields = ['name', 'email', 'cruise', 'notes']
    success_url = reverse_lazy('index')
    success_message = 'Thank you, %(name)s! We will email you when we have more information about %(cruise)s!'

def add_destination(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST)
        if form.is_valid():
            # Handle the cleaned data
            pass
    else:
        form = DestinationForm()

    return render(request, 'destination_form.html', {'form': form})