from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from calculator.models import Query
from django.forms.models import model_to_dict
from calculator.classes import Calculator
from .forms import PrintForm
import pandas as pd


def print(request):
    if request.method == 'POST':
        ApplNo = request.POST.get('ApplNo')
        dat = model_to_dict(Query.objects.filter(ApplNo=ApplNo).latest('created'))
        form = PrintForm(dat, auto_id="%s")
        calc = Calculator(**dat)
        details = pd.DataFrame.from_dict({
            'Cost/Income (%)': calc.cost_income_ratio * 100,
            'ROA (%)': calc.roa * 100,
            'ROE (%)': calc.roe * 100
        })
        details.index = ['Year ' + str(i + 1) for i in details.index]
        if details.shape[0] > 10:
            details = details.iloc[:10, :]
        details = details.round(2).to_html(border=0, classes='table')
        ret = {
            'details': details,
            'total_profit': round(calc.net_profit.sum(), 2),
            'net_roe': round(calc.net_profit.sum() / calc.capital_req.sum() * 100, 2),
            'emi': calc.emi,
            'form': form,
        }
        return render(request, 'print.html', ret)
    return HttpResponseNotFound('<h1>Page not found</h1>')