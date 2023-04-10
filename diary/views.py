from django.shortcuts import render

from.forms import InquiryForm

# Create your views here.
from django.views import generic

class IndexView(generic.TemplateView):
  template_name="index.html"

class InquiryView(generic.FormView):
  template_name="inquiry.html"
  form_class=InquiryForm
