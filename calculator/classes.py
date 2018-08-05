################################################################################
#                            Import Libraries                                  #
################################################################################

import numpy as np

################################################################################
#                             Class Definitions                                #
################################################################################


class Calculator:
    cost_of_funds = 0.0768
    basel_prop = 0.115
    tax_perc = 0.358
    psl_impact = [-0.0025, 0.0011]
    agri_psl_impact = (-0.0025, 0.0025)
    lifetime_slippage = {
        'HL': np.array([0.0107, 0.0348, 0.0510, 0.0501, 0.0501]),
        'LAP': np.array([0.0032, 0.0187, 0.0316, 0.0209, 0.0209]),
        'CV': np.array([0.0188, 0.0444, 0.0425, 0.0489, 0.0489]),
        'Tractor': np.array([0.0014, 0.0328, 0.0515, 0.0640, 0.0640]),
        'SME': np.array([0.0031, 0.0361, 0.0345, 0.0372, 0.0372]),
        'Corporate': {
            'AAA': np.arange(.001, .006, .001),
            'AA': np.arange(.001, .006, .001),
            'A': np.arange(.001, .006, .001),
            'BBB': np.arange(.001, .006, .001),
            'BB': np.arange(.001, .006, .001),
            'Unrated': np.arange(.001, .006, .001),
            'CM': np.arange(.001, .006, .001),
            'CRE': np.arange(.001, .006, .001),
            'CRE_RH': np.arange(.001, .006, .001),
            'RRE': np.arange(.001, .006, .001),
            'RRP': np.arange(.001, .006, .001),
            'NBFC': np.arange(.001, .006, .001),
        },
        'AIB': {
            'AAA': np.arange(.001, .006, .001),
            'AA': np.arange(.001, .006, .001),
            'A': np.arange(.001, .006, .001),
            'BBB': np.arange(.001, .006, .001),
            'BB': np.arange(.001, .006, .001),
            'Unrated': np.arange(.001, .006, .001),
            'CM': np.arange(.001, .006, .001),
            'CRE': np.arange(.001, .006, .001),
            'CRE_RH': np.arange(.001, .006, .001),
            'RRE': np.arange(.001, .006, .001),
            'RRP': np.arange(.001, .006, .001),
            'NBFC': np.arange(.001, .006, .001),
        },
    }
    risk_rating_map = {
        'AAA': .2,
        'AA': .3,
        'A': .5,
        'BBB': 1,
        'BB': 1.5,
        'Unrated': 1,
        'CM': 1,
        'CRE': 1,
        'CRE_RH': .75,
        'RRE': .75,
        'RRP': .75,
        'NBFC': 1,
    }
    lgd = {
        'HL': 0.20,
        'LAP': 0.20,
        'CV': 0.25,
        'Tractors': 0.71,
        'SME': .2,
        'Corporate': 1,
        'AIB': 1
    }
    costs = {
        'origination': {
            'HL': 39219,
            'LAP': 39219,
            'SME': 96053,
            'CV': 16152,
            'Tractor': 15648
        },
        'maintenance': {
            'HL': 4058,
            'LAP': 4058,
            'SME': 26810,
            'CV': 4189,
            'Tractor': None
        },
        'collection': {
            'HL': 3719,
            'LAP': 3719,
            'SME': 8903,
            'CV': 5003,
            'Tractor': 3000
        }
    }
    income_cost = {
        'Corporate': .25,
        'AIB': .4

    }
    insurance_income_perc = 0.25
    roe_objective = .14

    def __init__(self, typ: str, product: str, sanction_amt: int, roi: float,
                 profee: float, conpay: float, other: int, recurr: int,
                 insur: int, psl: int, agri_psl: int, ltv: float = None,
                 rating: str = None, tenure: int = 60, utilisation: float = 0.7):
        """

        :param product:
        :param sanction_amt:
        :param roi:
        :param tenure:
        :param profee:
        :param conpay:
        :param other:
        :param recurr:
        :param insur:
        :param psl:
        :param agri_psl:
        :param ltv:
        :param rating:
        :param utilisation:

        Note: In order to compute ODCC for years more than 5, default value of tenure should be changed accordingly.
        """
        self.__typ = typ
        self.__product = product
        self.__ltv = ltv
        self.__sanction_amt = sanction_amt
        self.__roi = roi
        if typ == 'ODCC':
            self.__tenure = 60
        self.__yrs = int(np.ceil(tenure / 12))
        self.__rating = rating
        self.__processing_perc = profee
        self.__connector_pay_perc = conpay
        self.__other_income = other
        self.__is_other_recurring = recurr
        self.__insurance = insur
        self.__is_psl = psl
        self.__is_agri_psl = agri_psl
        self.__utilisation = utilisation

        if self.typ == 'TL':
            self.__emi = self.emi_compute()
            self.__pos = self.compute_pos_TL()
        else:
            self.__pos = self.compute_pos_ODCC()
        self.__fund_cost = self.compute_fund_cost()
        self.__lsp = self.compute_lsp()
        self.__int_income = self.compute_int_income()

        self.__provision = self.compute_provision()
        self.__risk_perc = self.compute_risk_perc()
        self.__operational_risk = self.compute_operational_risk()

        self.__psl_benefit, self.__psl_agri_benefit = self.compute_benefits()
        self.__processing_charge = self.compute_processing_charge()
        self.__other_income = self.compute_other_income()
        (self.__origination_cost, self.__maintenance_cost,
         self.__collection_cost) = self.compute_other_costs()
        self.__sourcing_fee = self.compute_sourcing_fee()
        if self.product == 'TL':
            self.__capital_req = self.compute_capital_req_TL()
        else:
            self.__capital_req = self.compute_capital_req_ODCC()
        self.__nim = self.compute_nim()
        self.__nim_perc = self.compute_nim_perc()
        self.__total_income = self.compute_total_income()
        self.__total_cost = self.compute_total_cost()
        self.__net_profit = self.compute_net_profit()
        self.__cost_income_ratio = self.compute_cost_income_ratio()
        self.__roa = self.compute_roa()
        self.__roe = self.compute_roe()
        self.__roe_shortfall = self.compute_roe_shortfall()

    def emi_compute(self):
        p = self.sanction_amt
        r = self.roi / 12
        n = self.tenure
        return (p * r * (1 + r) ** n) / ((1 + r) ** n - 1)

    def compute_pos_TL(self):
        """
        computes pos for a class
        :return:
        """
        p = self.sanction_amt
        r = self.roi / 12
        n = self.tenure
        pos = []
        for i in range(n):
            pos.append(p)
            interest = p * r
            p = p - (self.emi - interest)
        pos = np.append(pos, np.repeat(0, np.ceil(n / 12) * 12 - n))
        pos = np.array(pos).reshape(len(pos) // 12, 12)
        pos = np.c_[pos, np.append(pos[:, 0][1:], 0)]
        return pos.sum(axis=1) / (pos > 0).sum(axis=1)

    def compute_pos_ODCC(self):
        return np.repeat(self.sanction_amt * self.utilisation, self.yrs)

    def compute_fund_cost(self):
        return self.pos * self.cost_of_funds

    def compute_lsp(self):
        lsp = self.lifetime_slippage[self.product]
        if self.product in ['Corporate', 'AIB']:
            lsp = lsp[self.rating]
        if len(lsp) >= self.yrs:
            lsp = lsp[:self.yrs]
        else:
            lsp = np.append(lsp, np.repeat(lsp[-1], self.yrs - len(lsp)))
        return lsp

    def compute_int_income(self):
        return self.pos * self.roi - \
               self.sanction_amt * self.roi * self.lsp * self.lgd[self.product]

    def compute_provision(self):
        return self.sanction_amt * np.append(self.lsp[0], np.diff(self.lsp)) * \
               self.lgd[self.product]

    def compute_risk_perc(self):
        if self.product == 'HL':
            if self.ltv <= 0.75 and self.sanction_amt <= 7500000:
                risk_perc = 0.35
            else:
                risk_perc = 0.5
        elif self.product == 'LAP':
            risk_perc = .75 if self.rating == 'RRP' else 1
        elif self.product in ['Corporate', 'SME', 'AIB']:
            risk_perc = self.risk_rating_map[self.rating]
        else:
            risk_perc = None
        return np.repeat(risk_perc, self.yrs)

    def compute_operational_risk(self):
        return np.append(.0025, np.repeat(0.1, self.yrs - 1))

    def compute_benefits(self):
        return self.psl_impact[self.is_psl] * self.pos, \
               self.agri_psl_impact[self.is_agri_psl] * self.pos

    def compute_processing_charge(self):
        return np.append(self.sanction_amt * self.processing_perc,
                         np.repeat(0, self.pos.shape[0] - 1))

    def compute_other_income(self):
        other = np.repeat(self.other_fee, self.pos.shape[0] - 1) if \
            self.is_other_recurring else np.repeat(0, self.pos.shape[0] - 1)
        other = np.append(
            self.other_income + self.insurance * self.insurance_income_perc, other
        )
        return other

    def compute_other_costs(self):
        if self.product in ['Corporate', 'AIB']:
            origination_cost = self.income_cost[self.product] * \
                               self.total_income
            maintenance_cost = np.repeat(0, self.pos.shape[0])
            collection_cost = np.repeat(0, self.pos.shape[0])
        else:
            origination_cost = np.append(self.costs['origination'][self.product],
                                         0 * self.__pos[1:])
            maintenance_cost = np.repeat([self.costs['maintenance'][self.product]],
                                         self.pos.shape[0])
            collection_cost = np.append(self.costs['collection'][self.product] / 2,
                                        [self.costs['collection'][self.product]] *
                                        (self.pos.shape[0] - 1))
        return origination_cost, maintenance_cost, collection_cost

    def compute_sourcing_fee(self):
        return np.append(self.connector_pay_perc * self.sanction_amt * 1.1,
                         0 * self.pos[1:])

    def compute_capital_req_ODCC(self):
        total_risk = self.risk_perc + self.operational_risk
        return total_risk * self.basel_prop * (self.sanction_amt * .2 +
                                                      self.pos * .8)

    def compute_capital_req_TL(self):
        total_risk = self.risk_perc + self.operational_risk
        return total_risk * self.basel_prop * self.pos

    def compute_nim(self):
        return self.int_income + self.psl_agri_benefit + \
               self.psl_benefit - self.fund_cost

    def compute_nim_perc(self):
        return self.nim / self.pos

    def compute_total_income(self):
        return self.nim + self.processing_charge + self.other_income

    def compute_total_cost(self):
        return self.sourcing_fee + self.origination_cost + \
               self.maintenance_cost + self.collection_cost

    def compute_net_profit(self):
        operating_profit = self.total_income - self.total_cost
        pretax_profit = operating_profit - self.provision
        tax = pretax_profit * self.tax_perc
        return pretax_profit - tax

    def compute_cost_income_ratio(self):
        return self.total_cost / self.total_income

    def compute_roa(self):
        return self.net_profit / self.pos

    def compute_roe(self):
        return self.net_profit / self.capital_req

    def compute_roe_shortfall(self):
        return self.roe_objective * self.capital_req - self.net_profit

    #--------------------------  Getter Functions ---------------------------------#

    @property
    def typ(self):
        return self.__typ

    @property
    def product(self):
        return self.__product

    @property
    def ltv(self):
        return self.__ltv

    @property
    def sanction_amt(self):
        return self.__sanction_amt

    @property
    def roi(self):
        return self.__roi

    @property
    def tenure(self):
        return self.__tenure

    @property
    def yrs(self):
        return self.__yrs

    @property
    def rating(self):
        return self.__rating

    @property
    def processing_perc(self):
        return self.__processing_perc

    @property
    def connector_pay_perc(self):
        return self.__connector_pay_perc


    @property
    def other_income(self):
        return self.__other_income


    @property
    def is_other_recurring(self):
        return self.__is_other_recurring


    @property
    def insurance(self):
        return self.__insurance


    @property
    def is_psl(self):
        return self.__is_psl


    @property
    def is_agri_psl(self):
        return self.__is_agri_psl


    @property
    def utilisation(self):
        return self.__utilisation


    @property
    def emi(self):
        try:
            return self.__emi
        except:
            return None

    @property
    def pos(self):
        return self.__pos

    @property
    def fund_cost(self):
        return self.__fund_cost

    @property
    def lsp(self):
        return self.__lsp

    @property
    def int_income(self):
        return self.__int_income

    @property
    def provision(self):
        return self.__provision

    @property
    def risk_perc(self):
        return self.__risk_perc

    @property
    def operational_risk(self):
        return self.__operational_risk

    @property
    def psl_benefit(self):
        return self.__psl_benefit

    @property
    def psl_agri_benefit(self):
        return self.__psl_agri_benefit

    @property
    def processing_charge(self):
        return self.__processing_charge


    @property
    def total_other_income(self):
        return self.__other_income

    @property
    def origination_cost(self):
        return self.__origination_cost


    @property
    def maintenance_cost(self):
        return self.__maintenance_cost


    @property
    def collection_cost(self):
        return self.__collection_cost

    @property
    def sourcing_fee(self):
        return self.__sourcing_fee

    @property
    def capital_req(self):
        return self.__capital_req

    @property
    def nim(self):
        return self.__nim

    @property
    def nim_perc(self):
        return self.__nim_perc

    @property
    def total_income(self):
        return self.__total_income

    @property
    def total_cost(self):
        return self.__total_cost

    @property
    def net_profit(self):
        return self.__net_profit

    @property
    def cost_income_ratio(self):
        return self.__cost_income_ratio


    @property
    def roa(self):
        return self.__roa

    @property
    def roe(self):
        return self.__roe


    @property
    def roe_shortfall(self):
        return self.__roe_shortfall
