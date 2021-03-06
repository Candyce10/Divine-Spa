from django.shortcuts import redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from .models import Service, Review, Appointment, Contact
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from .forms import ReviewForm

class Home(View):
    def get(self, request):
        return HttpResponse("Divine Spa")

class About(View):
    def get(self, request):
        return HttpResponse("About Us")

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"


class ServiceList(TemplateView):
    template_name = "services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()
        return context
        
class ServiceDetail(DetailView):
    model = Service
    template_name = "service_detail.html"


class ReviewList(TemplateView):
    template_name = "reviews.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.all()
        return context


class ReviewCreate(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "review_create.html"
    success_url = "/reviews/"
  

class AppointmentPage(View):
     def get(self, request):
        return HttpResponse("Book Appointment")


class AppointmentPage(TemplateView):
    template_name = "appointment.html"
    

class AppointmentCreate(View):
    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        service = request.POST.get("service")
        number = request.POST.get("number")
        date = request.POST.get("date")
        time = request.POST.get("time")
        appointment = Appointment.objects.create(fname=fname, lname=lname, email=email, number=number, date=date, service=service, time=time)
        appointment.save()
        return HttpResponseRedirect('confirmation')


class ConfirmationPage(TemplateView):
    template_name = "confirmation.html"
    model = Appointment
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["appointments"] = Appointment.objects.all()
        return context


class ContactPage(View):
    def get(self, request):
        return HttpResponse("Contact Us")

class ContactPage(TemplateView):
    template_name = "contact.html"
    

class ContactCreate(View):
    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        contact = Contact.objects.create(name=name, email=email, subject=subject, message=message)
        contact.save()
        return HttpResponseRedirect('submitted')


class ContactSubmit(TemplateView):
    template_name = "submit_contact.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submit_contacts"] = Contact.objects.all()
        return context