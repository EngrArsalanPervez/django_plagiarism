from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from core.backend import plagiarism_checker
from core.forms import InputDocumentForm


class HomePage(CreateView):
    template_name = 'core/homepage.html'

    def get(self, request, *args, **kwargs):
        form = InputDocumentForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        result = {}
        form = InputDocumentForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            result = plagiarism_checker(query)
            print(result)
        return render(request, self.template_name, {
            'form': form,
            'result': result
        })
