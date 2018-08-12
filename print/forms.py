from django import forms
from calculator.models import Query
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Div, Submit, Hidden
from crispy_forms.bootstrap import AppendedText, PrependedText


class PrintForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(
                    Div(
                        HTML(
                            """<div class="card-header p-0" id="BasicHeader">
                                <h5 class="m-0">
                                    <button class="btn w-100 text-left btn-link" data-toggle="collapse" data-target="#BasicBody" 
                                    type="button">
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
                                Div(
                                    Div('product', css_class="col-sm-8"),
                                    Div('typ', css_class='col-sm-4'),
                                    css_class='row'
                                ),
                                css_class="card-body"
                            ),
                            css_id='BasicBody', css_class="collapse show active"
                        ),
                        css_class="card mx-2 shadow my-1 border-0"
                    ),
                    css_class='col-6'
                ),
                Div(
                    Div(
                        HTML(
                            """
                            <div class="card-header p-0" id="FinancialHeader">
                                <h5 class="m-0">
                                    <button class="btn w-100 text-left btn-link " data-toggle="collapse" data-target="#FinancialBody" type="button">
                                        Financial Details <i class="fa fa-lg fa-caret-up float-right" aria-hidden="true"></i>
                                    </button>
                                </h5>
                            </div>
                            """
                        ),
                        Div(
                            Div(
                                Div(
                                    Div(PrependedText('sanction_amt', '&#8377'), css_id="magicdiv1", css_class="col-sm-7"),
                                    Div(AppendedText('roi', '%'), css_id="magicdiv2", css_class="col-sm-5"),
                                    Div(AppendedText('tenure', '%'), css_id="magicdiv3", css_class="col-sm-6"),
                                    Div(AppendedText('utilisation', '%'), css_id="magicdiv4", css_class="col-sm-6"),
                                    Div('rating', css_id="magicdiv5", css_class="col-sm-6"),
                                    Div(AppendedText('ltv', '%'), css_id="magicdiv6", css_class="col-sm-6"),
                                    css_class='row'
                                ),
                                css_class="card-body"
                            ),
                            css_id="FinancialBody", css_class='collapse show active'
                        ),
                        css_class="card mx-2 shadow my-1 border-0"
                    ),
                    css_class='col-6'
                ),
                Div(
                    Div(
                        HTML(
                            """
                            <div class="card-header p-0" id="FeeIncomeHeader">
                                <h5 class="mb-0">
                                    <button class="btn btn-link w-100 text-left " type="button" data-toggle="collapse" data-target="#FeeIncomeBody" 
                                    aria-expanded="false" aria-controls="collapseTwo">
                                        Fees and Incomes <i class="fa fa-lg fa-caret-up float-right" aria-hidden="true"></i>
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
                                    css_class="row"
                                ),
                                css_class="card-body"
                            ),
                            css_class="collapse show active", css_id="FeeIncomeBody"
                        ),
                        css_class="card mx-2 shadow my-1 border-0"
                    ),
                    css_class='col-6'
                ),
                Div(
                    Div(
                        HTML(
                            """
                            <div class="card-header p-0" id="PLSheader">
                              <h5 class="mb-0">
                                <button class="btn btn-link w-100 text-left" type="button" data-toggle="collapse"
                                 data-target="#PSLBody" aria-expanded="false" aria-controls="collapseThree">
                                      PSL Status <i class="fa fa-lg fa-caret-up float-right" aria-hidden="true"></i>
                                </button>
                              </h5>
                            </div>
                            """),
                        Div(
                            Div(
                                'recurr',
                                'psl',
                                'agri_psl',
                                'rrp',
                                css_class='card-body'),
                            css_class="collapse show active", css_id="PSLBody"),
                        css_class="card mx-2 shadow my-1 border-0"),
                    css_class='col-6'
                ),
                css_class='row'
            )
        )
        super(PrintForm, self).__init__(*args, **kwargs)