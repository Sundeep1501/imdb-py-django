from django.views.generic import TemplateView
from imdb.forms import IndexForm
from django.shortcuts import render
from imdb.models import Namebasics
from imdb.models import LegacySQLViews

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get(self, request):
        form = IndexForm()
        args = {'form':form}
        return render(request, self.template_name, args)
    
    def post(self, request):
        form = IndexForm(request.POST)
        if form.is_valid():
            search_txt = form.cleaned_data['search']
            names = Namebasics.objects.filter(primaryname__contains=search_txt)
            form = IndexForm()
            args = {'form':form, 'result': names}
        else:
            args = {'form':form}

        return render(request, self.template_name, args)

class QueryAView(TemplateView):
    template_name = 'querya.html'
    def get(self, request):
        rows = LegacySQLViews.queryA()
        args = {'result':rows}
        return render(request, self.template_name, args)

class QueryBView(TemplateView):
    template_name = 'querya.html'
    def get(self, request):
        rows = LegacySQLViews.queryB()
        args = {'result':rows}
        return render(request, self.template_name, args)

class QueryCView(TemplateView):
    template_name = 'querya.html'
    def get(self, request):
        rows = LegacySQLViews.queryC()
        args = {'result':rows}
        return render(request, self.template_name, args)

class QueryDView(TemplateView):
    template_name = 'querya.html'
    def get(self, request):
        rows = LegacySQLViews.queryD()
        args = {'result':rows}
        return render(request, self.template_name, args)

class QueryEView(TemplateView):
    template_name = 'querya.html'
    def get(self, request):
        rows = LegacySQLViews.queryE()
        args = {'result':rows}
        return render(request, self.template_name, args)

class QueryFView(TemplateView):
    template_name = 'querya.html'
    def get(self, request):
        rows = LegacySQLViews.queryF()
        args = {'result':rows}
        return render(request, self.template_name, args)

class QueryGView(TemplateView):
    template_name = 'querya.html'
    def get(self, request):
        rows = LegacySQLViews.queryG()
        args = {'result':rows}
        return render(request, self.template_name, args)

class QueryHView(TemplateView):
    template_name = 'querya.html'
    def get(self, request):
        rows = LegacySQLViews.queryH()
        args = {'result':rows}
        return render(request, self.template_name, args)

class QueryIView(TemplateView):
    template_name = 'querya.html'
    def get(self, request):
        rows = LegacySQLViews.queryI()
        args = {'result':rows}
        return render(request, self.template_name, args)
