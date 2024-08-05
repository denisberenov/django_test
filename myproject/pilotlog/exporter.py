import csv

def export_logbook_to_csv(file_path, aircraft_data, flight_data):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)

        # ForeFlight Logbook Import Header
        writer.writerow(['ForeFlight Logbook Import'] + [''] * 64)
        writer.writerow([''] * 64)

        # Aircraft Table
        writer.writerow(['Aircraft Table'] + [''] * 64)
        writer.writerow(['Text', 'Text', 'Text', 'YYYY', 'Text', 'Text', 'Text', 'Text', 'Text', 'Text', 'Boolean', 'Boolean', 'Boolean', 'Boolean'] + [''] * 50)
        writer.writerow(['AircraftID', 'EquipmentType', 'TypeCode', 'Year', 'Make', 'Model', 'Category', 'Class', 'GearType', 'EngineType', 'Complex', 'HighPerformance', 'Pressurized', 'TAA'] + [''] * 50)
        writer.writerow([''] * 64)
        writer.writerow([''] * 64)
        writer.writerow([''] * 64)
        writer.writerow([''] * 64)
        writer.writerow([''] * 64)
        writer.writerow([''] * 64)
        writer.writerow([''] * 64)

        # Write Aircraft Data
        for aircraft in aircraft_data:
            writer.writerow([
                aircraft.guid, aircraft.platform, aircraft.aircraft_code, aircraft.make, aircraft.model,
                aircraft.category, aircraft.class_field, aircraft.run2, aircraft.power, aircraft.seats,
                aircraft.complex, aircraft.high_perf, aircraft.tailwheel, aircraft.tmg
            ] + [''] * 50)

        # Blank lines between sections
        writer.writerow([''] * 64)
        writer.writerow([''] * 64)
        writer.writerow([''] * 64)
        writer.writerow([''] * 64)
        writer.writerow([''] * 64)
        writer.writerow([''] * 64)

        # Flights Table
        writer.writerow(['Flights Table'] + [''] * 32 + ['#;type;runway;airport;comments'] + [''] * 24 + ['name;role;email'] + [''] * 11)
        writer.writerow(['Date', 'Text', 'Text', 'Text', 'Text', 'hhmm', 'hhmm', 'hhmm', 'hhmm', 'hhmm', 'hhmm', 'Decimal', 'Decimal', 'Decimal', 'Decimal', 'Decimal', 'Decimal', 'Decimal', 'Number', 'Decimal', 'Number', 'Number', 'Number', 'Number', 'Number', 'Decimal', 'Decimal', 'Decimal', 'Decimal', 'Decimal', 'Decimal', 'Number', 'Packed Detail', 'Packed Detail', 'Packed Detail', 'Packed Detail', 'Packed Detail', 'Packed Detail', 'Decimal', 'Decimal', 'Decimal', 'Decimal', 'Text', 'Text', 'Packed Detail', 'Packed Detail', 'Packed Detail', 'Packed Detail', 'Packed Detail', 'Packed Detail', 'Boolean', 'Boolean', 'Boolean', 'Boolean', 'Boolean', '[Text]CustomFieldName', '[Numeric]CustomFieldName', '[Hours]CustomFieldName', '[Counter]CustomFieldName', '[Date]CustomFieldName', '[DateTime]CustomFieldName', '[Toggle]CustomFieldName', 'PilotComments'])

        # Write Flight Data
        for flight in flight_data:
            writer.writerow(flight)

