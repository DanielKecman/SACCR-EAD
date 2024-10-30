from scipy.stats import norm
import numpy as np
from enum import Enum


class Currency(Enum):
    USD = 'USD'
    EUR = 'EUR'

class OptionType(Enum):
    NOT_OPTION = "NotOption"
    CALL = "Call"
    PUT = "Put"


class IRPosition:
    def __init__(self,
                 spot_price: float,
                 maturity: float,
                 currency: Currency,
                 notional: float,
                 market_value: float,
                 start_date: float,
                 end_date: float,
                 exercise_date: float,
                 paying_float: bool,
                 option_type: OptionType,
                 strike_price: float = -1
    ):
        self._spot_price = spot_price
        self._maturity = maturity
        self._currency = currency
        self._notional = notional
        self._market_value = market_value
        self._start_date = start_date
        self._end_date = end_date
        self._exercise_date = exercise_date
        self._paying_float = paying_float
        self._option_type = option_type
        self._strike_price = strike_price

    def _calculate_supervised_duration(self):
        return (np.exp(-0.05 * self._start_date) - np.exp(-0.05 * self._end_date)) / 0.05


    def _calculate_adjusted_notional(self):
        return self._notional * self._calculate_supervised_duration()

    def _calculate_supervisory_delta(self):
        sup_vol = 0.5
        if self._paying_float:
            if self._option_type == OptionType.NOT_OPTION:
                return -1
            else:
                return -1 * norm.cdf(np.log(self._spot_price / self._strike_price) + 0.5 * sup_vol ** 2 * self._maturity) / (sup_vol * np.sqrt(self._maturity))
        else:
            if self._option_type == OptionType.NOT_OPTION:
                return 1
            else:
                return norm.cdf(np.log(self._spot_price / self._strike_price) + 0.5 * sup_vol ** 2 * self._maturity) / (sup_vol * np.sqrt(self._maturity))


    def _assign_time_bucket(self):
        if self._maturity < 1:
            return 1
        elif self._maturity < 5:
            return 2
        else:
            return 3

