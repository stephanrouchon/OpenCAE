from django.core.management.base import BaseCommand
import json
from entrepreneur.models import Nationality
from pathlib import Path


class Command(BaseCommand):
    help = 'Importe les nationalités depuis un\
        fichier JSON (curiexplore-pays.json)'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            default='curiexplore-pays.json',
            help='Chemin vers le fichier JSON à importer.'
        )

    def handle(self, *args, **options):
        file_path = options['file']
        file_path = Path(file_path)
        if not file_path.exists():
            self.stderr.write(self.style.ERROR(
                f"Fichier non trouvé: {file_path}"))
            return
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
        count = 0
        for item in data:
            code = item.get('iso3')
            libelle = item.get('name_fr')
            if code and libelle:
                _, created = Nationality.objects.get_or_create(
                    code=code, defaults={'libelle': libelle})
                if created:
                    count += 1
        self.stdout.write(self.style.SUCCESS(
            f"{count} nationalités importées."))
