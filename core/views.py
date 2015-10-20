import json
import datetime

from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.conf import settings
from django.views.generic import View, ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView

from core.models import Doctor, Entry
from core.forms import EntryForm


class CreateEntry(CreateView):
    form_class = EntryForm
    template_name = 'create_entry.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.save()
        return redirect('/success/')


class GetHours(View):
    def get_context(self, request):
        pass
   
    def get(self, request, *args, **kwargs):
        context = self.get_context(request)
        doctor = request.GET.get('doctor')
        date = request.GET.get('date')
        hour_list = list()
        
        try:
            date = datetime.datetime.strptime(date, '%d.%m.%Y').date()
            doctor = get_object_or_404(Doctor, id=doctor)
            hours = Entry.objects.filter(doctor=doctor,
                                        start_at__day=date.day, 
                                        start_at__month=date.month, 
                                        start_at__year=date.year)

            busy_hours = [h.start_at.hour for h in hours]
            # Generate list with hour specifieds
            for hour in settings.ENTRY_HOURS:
                item = {'hour': '%d:00' % hour}
                item['busy'] = hour in busy_hours
                hour_list.append(item)
        except:
            pass

        return JsonResponse(hour_list, safe=False)
