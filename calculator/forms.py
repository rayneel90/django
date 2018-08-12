from django import forms
from .models import Query
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Fieldset, MultiField, Div, ButtonHolder, Submit, Hidden
from crispy_forms.bootstrap import AppendedText, PrependedText

class TLForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ('ApplNo','RMName', 'HRMS', 'product', 'sanction_amt',
                  'roi', 'tenure', 'ltv', 'rating', 'profee',
                  'conpay', 'insur', 'other', 'recurr', 'psl', 'agri_psl', 'rrp')
        widgets = {
            'sanction_amt': forms.NumberInput(attrs={'min': 0, 'step': 1000}),
            'roi': forms.NumberInput(attrs={'min': 0}),
            'tenure': forms.NumberInput(attrs={'min': 0}),
            'ltv': forms.NumberInput(attrs={'min': 0}),
            'profee': forms.NumberInput(attrs={'min': 0}),
            'conpay': forms.NumberInput(attrs={'min': 0}),
            'insur': forms.NumberInput(attrs={'min': 0}),
            'other': forms.NumberInput(attrs={'min': 0}),
        }
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Hidden('typ','TL'),
                HTML(
                    """<div class="card-header p-0" id="TLBasicHeader">
                            <h5 class="m-0">
                                <button class="btn w-100 text-left btn-link" data-toggle="collapse" data-target="#TLBasicBody" type="button">
                                    Basic Loan Details <i class="fa fa-lg fa-caret-up float-right" aria-hidden="true"></i>
                                </button>
                            </h5>
                        </div> """
                ),
                Div(
                    Div(
                        "ApplNo",
                        Div(
                            Div('RMName', css_class="col-sm-8"),
                            Div('HRMS', css_class='col-sm-4'),
                            css_class='row'
                        ),
                        'product',
                        css_class="card-body"
                    ),
                    css_id='TLBasicBody', css_class="collapse show active"
                ),
                css_class="card mx-2 shadow my-1 border-0"
            ),
            Div(
                HTML(
                    """
                    <div class="card-header p-0" id="TLFinancialHeader">
                        <h5 class="m-0">
                            <button class="btn w-100 text-left btn-link collapsed" data-toggle="collapse" data-target="#TLFinancialBody" type="button">
                                Financial Details <i class="fa fa-lg fa-caret-down float-right" aria-hidden="true"></i>
                            </button>
                        </h5>
                    </div>
                    """
                ),
                Div(
                    Div(
                        Div(
                            Div(PrependedText('sanction_amt','&#8377'), css_id="magicdiv1", css_class="col-sm-7"),
                            Div(AppendedText('roi','%'), css_id="magicdiv2", css_class="col-sm-5"),
                            Div(AppendedText('tenure','months'), css_id="magicdiv3", css_class="col-sm-6"),
                            Div('rating', AppendedText('ltv','%'), css_id="magicdiv4", css_class="col-sm-6"),
                            css_class='row'
                        ),
                        css_class="card-body"
                    ),
                    css_id="TLFinancialBody", css_class='collapse'
                ),
                css_class="card mx-2 shadow my-1 border-0"
            ),
            Div(
                HTML(
                    """
                    <div class="card-header p-0" id="TLFeeIncomeHeader">
                        <h5 class="mb-0">
                            <button class="btn btn-link w-100 text-left collapsed" type="button" data-toggle="collapse" data-target="#TLFeeIncomeBody" 
                            aria-expanded="false" aria-controls="collapseTwo">
                                Fees and Incomes <i class="fa fa-lg fa-caret-down float-right" aria-hidden="true"></i>
                            </button>
                        </h5>
                    </div>
                    """
                ),
                Div(
                    Div(
                        Div(
                            Div(AppendedText('profee','%'),css_class="col-sm-6"),
                            Div(AppendedText('conpay','%'), css_class="col-sm-6"),
                            Div(PrependedText('insur','&#8377'), css_class="col-sm-6 pr-0"),
                            Div(PrependedText('other','&#8377'), css_class="col-sm-6"),
                            HTML(
                                """
                                <div class="m-2" id="TLrecurr">
                                  <fieldset class="toggle-check large verbal" tabindex="0">
                                    <label>
                                      {{tlform.recurr}}
                                      <span data-on="Yes" data-off="No">
                                        {{tlform.recurr.label_tag}}
                                      </span>
                                    </label>
                                  </fieldset>
                                </div>
                                """
                            ),
                            css_class="row"
                        ),
                        css_class="card-body"
                    ),
                    css_class="collapse", css_id="TLFeeIncomeBody"
                ),
                css_class="card mx-2 shadow my-1 border-0"
            ),
            HTML("""
             <div class="card mx-2 my-1 shadow border-0">
    <div class="card-header p-0" id="TLPLSheader">
      <h5 class="mb-0">
        <button class="btn btn-link w-100 text-left collapsed" type="button" data-toggle="collapse" data-target="#TLPSLBody"
                aria-expanded="false" aria-controls="collapseThree">
          PSL Status <i class="fa fa-lg fa-caret-down float-right" aria-hidden="true"></i>
        </button>
      </h5>
    </div>
    <div id="TLPSLBody" class="collapse" aria-labelledby="headingThree" >
      <div class="card-body">
        <h6 class="card-title">
          Check all that are applicable
        </h6>
        <div class="m-2" id="psl">
          <fieldset class="toggle-check large verbal" tabindex="0">
            <label>
              {{tlform.psl}}
              <span data-on="Yes" data-off="No">
                {{tlform.psl.label_tag}}
              </span>
            </label>
          </fieldset>
        </div>
        <div class="m-2" id="agri_psl">
          <fieldset class="toggle-check large verbal" tabindex="0">
            <label>
              {{tlform.agri_psl}}
              <span data-on="Yes" data-off="No">
                {{tlform.agri_psl.label_tag}}
              </span>
            </label>
          </fieldset>
        </div>
        <div class="m-2" id="rrp">
          <fieldset class="toggle-check large verbal" tabindex="0">
            <label>
              {{tlform.rrp}}
              <span data-on="Yes" data-off="No">
                {{tlform.rrp.label_tag}}
              </span>
            </label>
          </fieldset>
        </div>
      </div>
    </div>
  </div>"""),
            Div(
                Submit('submit','Calculate',css_class="btn btn-primary btn-block"),
                css_class="card mx-2 my-1 shadow border-0"
            )
        )
        super(TLForm, self).__init__(*args, **kwargs)


class ODCCForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ('ApplNo','RMName', 'HRMS', 'product', 'sanction_amt',
                  'roi', 'utilisation', 'ltv', 'rating', 'profee',
                  'conpay', 'insur', 'other', 'recurr', 'psl', 'agri_psl', 'rrp')
        widgets = {
            'sanction_amt': forms.NumberInput(attrs={'min': 0, 'step': 1000}),
            'roi': forms.NumberInput(attrs={'min': 0}),
            'utilisation': forms.NumberInput(attrs={'min': 0}),
            'ltv': forms.NumberInput(attrs={'min': 0}),
            'profee': forms.NumberInput(attrs={'min': 0}),
            'conpay': forms.NumberInput(attrs={'min': 0}),
            'insur': forms.NumberInput(attrs={'min': 0}),
            'other': forms.NumberInput(attrs={'min': 0}),
        }
    helper = FormHelper()
    helper.layout = Layout(
        AppendedText('roi', '%'),
        AppendedText('profee', '%'),
        AppendedText('conpay', '%'),
        AppendedText('utilisation', '%'),
        PrependedText('sanction_amt', '&#8377'),
        PrependedText('insur', '&#8377'),
        PrependedText('other', '&#8377'),
    )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Hidden('typ', 'ODCC'),
                HTML(
                    """<div class="card-header p-0" id="ODCCBasicHeader">
                            <h5 class="m-0">
                                <button class="btn w-100 text-left btn-link" data-toggle="collapse" data-target="#ODCCBasicBody" type="button">
                                    Basic Loan Details <i class="fa fa-lg fa-caret-up float-right" aria-hidden="true"></i>
                                </button>
                            </h5>
                        </div> """
                ),
                Div(
                    Div(
                        "ApplNo",
                        Div(
                            Div('RMName', css_class="col-sm-8"),
                            Div('HRMS', css_class='col-sm-4'),
                            css_class='row'
                        ),
                        'product',
                        css_class="card-body"
                    ),
                    css_id='ODCCBasicBody', css_class="collapse show active"
                ),
                css_class="card mx-2 shadow my-1 border-0"
            ),
            Div(
                HTML(
                    """
                    <div class="card-header p-0" id="ODCCFinancialHeader">
                        <h5 class="m-0">
                            <button class="btn w-100 text-left btn-link collapsed" data-toggle="collapse" data-target="#ODCCFinancialBody" type="button">
                                Financial Details <i class="fa fa-lg fa-caret-down float-right" aria-hidden="true"></i>
                            </button>
                        </h5>
                    </div>
                    """
                ),
                Div(
                    Div(
                        Div(
                            Div(PrependedText('sanction_amt', '&#8377'), css_id="odccmagicdiv1", css_class="col-sm-7"),
                            Div(AppendedText('roi', '%'), css_id="odccmagicdiv2", css_class="col-sm-5"),
                            Div(AppendedText('utilisation', '%'), css_id="odccmagicdiv3", css_class="col-sm-6"),
                            Div('rating', AppendedText('ltv', '%'), css_id="odccmagicdiv4", css_class="col-sm-6"),
                            css_class='row'
                        ),
                        css_class="card-body"
                    ),
                    css_id="ODCCFinancialBody", css_class='collapse'
                ),
                css_class="card mx-2 shadow my-1 border-0"
            ),
            Div(
                HTML(
                    """
                    <div class="card-header p-0" id="ODCCFeeIncomeHeader">
                        <h5 class="mb-0">
                            <button class="btn btn-link w-100 text-left collapsed" type="button" data-toggle="collapse" data-target="#ODCCFeeIncomeBody" 
                            aria-expanded="false" aria-controls="collapseTwo">
                                Fees and Incomes <i class="fa fa-lg fa-caret-down float-right" aria-hidden="true"></i>
                            </button>
                        </h5>
                    </div>
                    """
                ),
                Div(
                    Div(
                        Div(
                            Div(AppendedText('profee', '%'), css_class="col-sm-6"),
                            Div(AppendedText('conpay', '%'), css_class="col-sm-6"),
                            Div(PrependedText('insur', '&#8377'), css_class="col-sm-6 pr-0"),
                            Div(PrependedText('other', '&#8377'), css_class="col-sm-6"),
                            HTML(
                                """
                                <div class="m-2" id="ODCCrecurr">
                                  <fieldset class="toggle-check large verbal" tabindex="0">
                                    <label>
                                      {{odccform.recurr}}
                                      <span data-on="Yes" data-off="No">
                                        {{odccform.recurr.label_tag}}
                                      </span>
                                    </label>
                                  </fieldset>
                                </div>
                                """
                            ),
                            css_class="row"
                        ),
                        css_class="card-body"
                    ),
                    css_class="collapse", css_id="ODCCFeeIncomeBody"
                ),
                css_class="card mx-2 shadow my-1 border-0"
            ),
            HTML("""
               <div class="card mx-2 my-1 shadow border-0">
      <div class="card-header p-0" id="ODCCPLSheader">
        <h5 class="mb-0">
          <button class="btn btn-link w-100 text-left collapsed" type="button" data-toggle="collapse" data-target="#ODCCPSLBody"
                  aria-expanded="false" aria-controls="collapseThree">
            PSL Status <i class="fa fa-lg fa-caret-down float-right" aria-hidden="true"></i>
          </button>
        </h5>
      </div>
      <div id="ODCCPSLBody" class="collapse" aria-labelledby="headingThree" >
        <div class="card-body">
          <h6 class="card-title">
            Check all that are applicable
          </h6>
          <div class="m-2" id="psl">
            <fieldset class="toggle-check large verbal" tabindex="0">
              <label>
                {{odccform.psl}}
                <span data-on="Yes" data-off="No">
                  {{odccform.psl.label_tag}}
                </span>
              </label>
            </fieldset>
          </div>
          <div class="m-2" id="agri_psl">
            <fieldset class="toggle-check large verbal" tabindex="0">
              <label>
                {{odccform.agri_psl}}
                <span data-on="Yes" data-off="No">
                  {{odccform.agri_psl.label_tag}}
                </span>
              </label>
            </fieldset>
          </div>
          <div class="m-2" id="rrp">
            <fieldset class="toggle-check large verbal" tabindex="0">
              <label>
                {{odccform.rrp}}
                <span data-on="Yes" data-off="No">
                  {{odccform.rrp.label_tag}}
                </span>
              </label>
            </fieldset>
          </div>
        </div>
      </div>
    </div>"""),
            Div(
                Submit('submit', 'Calculate', css_class="btn btn-primary btn-block"),
                css_class="card mx-2 my-1 shadow border-0"
            )
        )
        super(ODCCForm, self).__init__(*args, **kwargs)
