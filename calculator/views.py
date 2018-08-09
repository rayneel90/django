from django.views.generic import TemplateView
from django.shortcuts import render
from .classes import Calculator
import pandas as pd
import pickle
from .forms import QueryForm

def temp(request):
    form = QueryForm()
    return render(request, 'temp.html', {'form': form})


class CalculatorView(TemplateView):
    template_name = "calculator.html"

    def post(self, request):
        # print('\n'*10, request.POST.dict(), '\n'*10)

        typ = request.POST.get('typ')
        print(typ)
        product = request.POST.get('product')
        sanction_amt = int(request.POST.get('sanction_amt'))
        roi = float(request.POST.get('roi'))
        profee = float(request.POST.get('profee'))
        conpay = float(request.POST.get('conpay'))
        other = int(request.POST.get('other',0))
        insur = int(request.POST.get('insur',0))
        recurr = int(request.POST.get('recurr', 0))
        psl = int(request.POST.get('psl', 0))
        agri_psl = int(request.POST.get('agri_psl', 0))
        ltv  = request.POST.get('ltv',0)
        print(ltv)
        if ltv == '':
            ltv = 0
        ltv = float(ltv)
        rating = request.POST.get('rating')
        tenure = int(request.POST.get('tenure', 60))
        if tenure == '':
            tenure = 60
        utilisation = float(request.POST.get('utilisation', .70))
        print(tenure, utilisation, ltv)
        rrp = request.POST.get('rrp')
        if rrp:
            rating = 'RRP'
        # print('\n'*10, typ,
        #     product,
        #     sanction_amt,
        #     roi,
        #     profee,
        #     conpay,
        #     other,
        #     insur,
        #     recurr,
        #     psl,
        #     agri_psl,
        #     ltv ,
        #     rating,
        #     tenure,
        #     utilisation,
        #     '\n'*10)
        print(typ)
        calc = Calculator(typ=typ, product=product, sanction_amt=sanction_amt,
                          roi = roi/100, profee=profee/100, conpay=conpay/100, other=other,
                          insur=insur, recurr=recurr, psl=psl, agri_psl=agri_psl,
                          ltv=ltv/100, tenure=tenure, utilisation=utilisation/100,
                          rating=rating)
        temp =  pd.DataFrame.from_dict({
                'Cost/Income (%)': calc.cost_income_ratio * 100,
                'ROA (%)': calc.roa * 100,
                'ROE (%)': calc.roe * 100
            }, orient='index')
        temp.columns = ['Year ' + str(i + 1) for i in temp.columns]
        if temp.shape[1]>10:
            temp = temp.iloc[:,0:10]
        print(temp)
        temp = temp.round(2).to_html(border=0, classes='table')

        ret = {
            'details':temp,
            'total_profit': round(calc.net_profit.sum(),2) ,
            'net_roe': round(calc.net_profit.sum() / calc.capital_req.sum() * 100,2),
            'emi': calc.emi,
            'typ': typ,
        }
        ret.update(request.POST.dict())
        print(request.POST.dict())
        print('\n'*10, ret, '\n'*10)
        return render(request, 'response.html', ret)
