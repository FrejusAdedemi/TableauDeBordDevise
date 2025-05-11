# 💱 Forex Monitor - Tableau de Bord des Devises

**Forex Monitor** est une application web interactive qui permet de suivre l’évolution des taux de change pour plusieurs devises mondiales. Elle propose une visualisation claire avec des graphiques, des statistiques dynamiques et un mode sombre/clair intégré.

## 🚀 Fonctionnalités

- 🔍 Sélection multiple de devises (ex : USD, EUR, JPY, XOF, etc.)
- 📊 Graphiques dynamiques sur 7 jours, 30 jours ou 1 an
- 📈 Indicateur de tendance (hausse, baisse, stable)
- 🌍 Interface responsive avec mode clair/sombre
- 📁 Export des données en CSV ou JSON
- 🔄 Actualisation manuelle des taux

## 🛠️ Stack technique

- **Backend** : Django 5.2.1 (Python 3.11)
- **Frontend** : HTML, Bootstrap 5, Chart.js
- **Déploiement** : Render.com (gratuit)

## 🧑‍💻 Installation locale

```bash
git clone https://github.com/FrejusAdedemi/TableauDeBordDevise.git
cd TableauDeBordDevise
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
