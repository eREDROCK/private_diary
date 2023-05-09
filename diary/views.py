import logging
from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from.forms import InquiryForm
from django.contrib import messages
from .models import Diary

logger=logging.getLogger(__name__)

# Create your views here.
from django.views import generic

class IndexView(generic.TemplateView):
  template_name="index.html"

class InquiryView(generic.FormView):
  template_name="inquiry.html"
  form_class=InquiryForm
  success_url=reverse_lazy('diary:inquiry')

  def form_valid(self, form):
    form.send_email()
    messages.success(self.request,'メッセージを送信しました。')
    logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
    return super().form_valid(form)

class DiaryListView(LoginRequiredMixin,generic.ListView):
  model=Diary
  template_name='diary_list.html'
  paginate_by=2

  def get_queryset(self):
    diaries=Diary.objects.filter(user=self.request.user).order_by('-created_at')
    return diaries