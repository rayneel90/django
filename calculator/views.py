from django.views.generic.edit import FormView
from django.shortcuts import render
from .classes import Calculator
import pandas as pd
import pickle
from .forms import TLForm, ODCCForm
from django.forms.models import model_to_dict

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def myview(request):
    tlform = TLForm(auto_id='TL%s')
    odccform = ODCCForm(auto_id='ODCC%s')
    if request.method == 'POST':
        typ = request.POST.get('typ')
        if typ == "TL":
            tlform = TLForm(request.POST, auto_id='TL%s')
            dat = tlform.save(commit=False)
            dat.typ = 'TL'
        else:
            odccform = ODCCForm(request.POST, auto_id='ODCC%s')
            dat = odccform.save(commit=False)
            dat.typ = 'ODCC'
        dat.ip = get_client_ip(request)
        dat.save()
        calc = Calculator(**model_to_dict(dat))
        details =  pd.DataFrame.from_dict({
                'Cost/Income (%)': calc.cost_income_ratio * 100,
                'ROA (%)': calc.roa * 100,
                'ROE (%)': calc.roe * 100
            }, orient='index')
        details.columns = ['Year ' + str(i + 1) for i in details.columns]
        if details.shape[1]>10:
            details = details.iloc[:,0:10]
        details = details.round(2).to_html(border=0, classes='table')
        ret = {
            'details': details,
            'total_profit': round(calc.net_profit.sum(), 2),
            'net_roe': round(calc.net_profit.sum() / calc.capital_req.sum() * 100, 2),
            'emi': calc.emi,
            'typ': typ,
            'tlform': tlform,
            'odccform': odccform,
            'ApplNo': request.POST.get('ApplNo')
        }
        return render(request, 'response.html', ret)
    return render(request, 'calculator.html', {'tlform': tlform, 'odccform': odccform})

def abc(request):
    tlform = TLForm(auto_id='TL%s')
    odccform = ODCCForm(auto_id='ODCC%s')
    return render(request, 'temp.html', {'tlform': tlform, 'odccform': odccform})