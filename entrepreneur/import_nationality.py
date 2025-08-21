import json
from entrepreneur.models import Nationality


with open('curiexplore-payes.json', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    code = item.get["iso3"]  # adapte selon la structure
    libelle = item["name_fr"]
    Nationality.objects.get_or_create(code=code, libelle=libelle)
