# pilotlog/management/commands/import_export.py
from django.core.management.base import BaseCommand
from pilotlog import importer, exporter
import os
from dotenv import load_dotenv

load_dotenv()

class Command(BaseCommand):
    help = 'Imports and exports logbook data'

    def handle(self, *args, **kwargs):
        # Assuming environment variables are set
        import_file = os.getenv('POLITLOG_MCC')
        export_file = os.getenv('LOGBOOK_TEMPLATE')

        if not import_file or not export_file:
            self.stdout.write(self.style.ERROR('Environment variables POLITLOG_MCC or LOGBOOK_TEMPLATE not set.'))
            return

        self.stdout.write('Importing data...')
        aircraft_data, flight_data = importer.import_data(import_file)

        self.stdout.write('Exporting data to CSV...')
        exporter.export_logbook_to_csv(export_file, aircraft_data, flight_data)

        self.stdout.write(self.style.SUCCESS('Data import/export completed successfully.'))
