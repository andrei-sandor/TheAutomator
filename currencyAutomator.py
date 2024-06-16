from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
import seaborn
from datetime import date

def currencies_automator(in_currency, out_currency):
    c = CurrencyRates()
    result = c.convert(str(in_currency), str(out_currency), amount=1)
    return result

def get_bitcoins(in_currency):
    b = BtcConverter()
    result = b.get_latest_price(str(in_currency))
    return result

def get_conversion_rates(in_currency):
    c = CurrencyRates()
    dict_currency_rates_today = c.get_rates(str(in_currency), date.today())
    seaborn.scatterplot(dict_currency_rates_today,x="Currencies", y=("Value in" , str(in_currency)))



