from django.shortcuts import render, redirect

from api import get_rates



def redirect_index(request):
    # Si l'URL de base est appelée sans paramètres, rediriger vers la page par défaut
    default_days = 7
    default_currencies = "USD,EUR,GBP"
    # Vérifier si des devises sont passées en paramètre de requête (ex: ?currencies=USD,JPY)
    if 'currencies' in request.GET:
        user_currencies = request.GET['currencies'].strip()
        if user_currencies:
            # Construire l'URL de redirection avec les devises fournies par l'utilisateur
            return redirect(f'/home/{default_days}/{user_currencies.upper()}')
    # Redirection par défaut
    return redirect(f'/home/{default_days}/{default_currencies}')


def dashboard(request, days_range, currencies):
    # 1. Préparer les paramètres
    days = int(days_range)  # s'assure que la période est un entier
    # Convertir la liste de devises séparées par des virgules en liste Python
    currency_list = [cur.strip().upper() for cur in currencies.split(',') if cur.strip()]

    # 2. Obtenir les données historiques via l'API
    days_labels, rates_data = get_rates(currency_list, days)
    if not days_labels or not rates_data:
        # Gérer le cas d'échec de l'API (on peut soit rediriger, soit passer un contexte vide)
        days_labels = []
        rates_data = {}

    # 3. Calculer les statistiques pour chaque devise
    stats = {}
    for curr, values in rates_data.items():
        if values and len(values) > 0:
            min_val = min(values)
            max_val = max(values)
            avg_val = sum(values) / len(values)
            first_val = values[0]
            last_val = values[-1]
            # Éviter division par zéro pour le calcul de variation
            if first_val != 0:
                percent_change = ((last_val - first_val) / first_val) * 100
            else:
                percent_change = 0.0
            # Arrondir les résultats (4 décimales pour min, max, moyenne; 1 décimale pour %)
            stats[curr] = {
                'min': round(min_val, 4),
                'max': round(max_val, 4),
                'moyenne': round(avg_val, 4),
                'variation': round(percent_change, 1)
            }
        else:
            # Si pas de données pour cette devise (liste vide ou None)
            stats[curr] = {'min': None, 'max': None, 'moyenne': None, 'variation': None}

    # 4. Déterminer le libellé de la période pour l'affichage
    if days == 7:
        page_label = "Semaine"
    elif days == 30:
        page_label = "Mois"
    elif days == 365:
        page_label = "Année"
    else:
        page_label = f"{days} jours"

    # 5. Construire le contexte pour le template
    context = {
        'page_label': page_label,
        'currencies': currency_list,
        'days_labels': days_labels,
        'data': rates_data,
        'stats': stats
    }
    return render(request, 'devise/index.html', context)
