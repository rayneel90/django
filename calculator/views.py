from django.views.generic import TemplateView
from django.shortcuts import render
from .classes import Calculator
import pandas as pd
import pickle
class CalculatorView(TemplateView):
    template_name = "calculator.html"

    def post(self, request):
        # print('\n'*10, request.POST.dict(), '\n'*10)

        typ = request.POST.get('typ')
        product = request.POST.get('product')
        sanction_amt = int(request.POST.get('sanction_amt'))
        roi = float(request.POST.get('roi'))/100
        profee = float(request.POST.get('profee'))/100
        conpay = float(request.POST.get('conpay'))/100
        other = int(request.POST.get('other',0))
        insur = int(request.POST.get('insur'))
        recurr = int(request.POST.get('recurr', 0))
        psl = int(request.POST.get('psl', 0))
        agri_psl = int(request.POST.get('agri_psl', 0))
        ltv  = float(request.POST.get('ltv'))/100
        rating = request.POST.get('rating')
        tenure = int(request.POST.get('tenure', 60))
        utilisation = float(request.POST.get('utilisation', .70))/100
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
        calc = Calculator(typ=typ, product=product, sanction_amt=sanction_amt,
                          roi = roi, profee=profee, conpay=conpay, other=other,
                          insur=insur, recurr=recurr, psl=psl, agri_psl=agri_psl,
                          ltv=ltv, tenure=tenure, utilisation=utilisation,
                          rating=rating)
        temp =  pd.DataFrame.from_dict({
                'Cost/Income (%)': calc.cost_income_ratio * 100,
                'ROA (%)': calc.roa * 100,
                'ROE (%)': calc.roe * 100
            }, orient='index')
        temp.columns = ['Year ' + str(i + 1) for i in temp.columns]
        temp = temp.round(2).to_html()
        ret = {
            'details':temp,
            'total_profit': round(calc.net_profit.sum(),2) ,
            'net_roe': round(calc.net_profit.sum() / calc.capital_req.sum() * 100,2),
            'emi': calc.emi,
            'typ': typ,
            'product': product,
            'sanction_amt': sanction_amt,
            'roi': roi,
            'profee': profee,
            'conpay': conpay,
            'other': other,
            'insur': insur,
            'recurr': recurr,
            'psl': psl,
            'agri_psl': agri_psl,
            'ltv': ltv,
            'rating': rating,
            'tenure': tenure,
            'utilisation': utilisation,
            'calc': calc
        }
        # print('\n'*10, ret, '\n'*10)
        return render(request, 'response.html', ret)
