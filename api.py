from datetime import timedelta, date
from pprint import pprint
import requests


def get_rates(currencies, days=30):
    end_date = date.today()
    start_date = end_date - timedelta(days=days)

    symbols = ','.join(currencies)
    requete = f"https://www.docstring.fr/api/rates/history/?start_at={start_date}&end_at={end_date}&symbols={symbols}"
    r = requests.get(requete)

    if not r or not r.json():
        return False, False

    api_rates = r.json().get("rates")
    all_rates = {currency: [] for currency in currencies}

    all_days = sorted(api_rates.keys())

    for each_day in all_days:
        # Vérifier si les données pour la journée sont un dictionnaire et contiennent des valeurs
        if isinstance(api_rates[each_day], dict):
            for currency, rate in api_rates[each_day].items():
                if currency in all_rates:
                    all_rates[currency].append(rate)
        else:
            print(f"Warning: Les données pour {each_day} sont mal formées ou vides.")


    return all_days, all_rates


if __name__ == '__main__':
    days, rates = get_rates(currencies=["USD", "CAD"])
    pprint(days)
    pprint(rates)
