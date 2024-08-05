# pilotlog/importer.py

import json
from pathlib import Path
from .models import Aircraft
from pilotlog.models import Aircraft, Flight

def import_data(file_path):
    with open(file_path, 'r') as file:
        # Read the entire file content as a string
        file_content = file.read()
        
        # Clean the JSON string if necessary
        cleaned_content = file_content.replace(r'\"', '"')
        
        # Parse the JSON string into Python objects
        data = json.loads(cleaned_content)
    
    aircraft_list = []
    flight_list = []
    
    # Iterate over each entry in the list
    for entry in data:
        if 'meta' in entry:  # Assuming 'meta' indicates an Aircraft entry
            meta = entry['meta']
            aircraft = Aircraft(
                user_id=entry['user_id'],
                guid=entry['guid'],
                platform=entry['platform'],
                modified=entry['_modified'],
                fin=meta.get('Fin', ''),
                sea=meta.get('Sea', False),
                tmg=meta.get('TMG', False),
                efis=meta.get('Efis', False),
                fnpt=meta.get('FNPT', 0),
                make=meta.get('Make', ''),
                run2=meta.get('Run2', False),
                class_field=meta.get('Class', 0),
                model=meta.get('Model', ''),
                power=meta.get('Power', 1),
                seats=meta.get('Seats', 0),
                active=meta.get('Active', True),
                kg5700=meta.get('Kg5700', False),
                rating=meta.get('Rating', ''),
                company=meta.get('Company', ''),
                complex=meta.get('Complex', False),
                cond_log=meta.get('CondLog', 0),
                fav_list=meta.get('FavList', False),
                category=meta.get('Category', 0),
                high_perf=meta.get('HighPerf', False),
                sub_model=meta.get('SubModel', ''),
                aerobatic=meta.get('Aerobatic', False),
                ref_search=meta.get('RefSearch', ''),
                reference=meta.get('Reference', ''),
                tailwheel=meta.get('Tailwheel', False),
                default_app=meta.get('DefaultApp', 0),
                default_log=meta.get('DefaultLog', 0),
                default_ops=meta.get('DefaultOps', 0),
                device_code=meta.get('DeviceCode', 0),
                aircraft_code=meta.get('AircraftCode', ''),
                default_launch=meta.get('DefaultLaunch', 0),
                record_modified=meta.get('Record_Modified', 0),
            )
            aircraft_list.append(aircraft)
        
        elif 'flight_id' in entry:  # Assuming 'flight_id' indicates a Flight entry
            flight = Flight(
                flight_id=entry.get('flight_id', ''),
                aircraft_guid=entry.get('aircraft_guid', ''),
                departure_time=entry.get('departure_time', ''),
                arrival_time=entry.get('arrival_time', ''),
                origin=entry.get('origin', ''),
                destination=entry.get('destination', ''),
                pilot=entry.get('pilot', ''),
                duration=entry.get('duration', 0),
                remarks=entry.get('remarks', ''),
            )
            flight_list.append(flight)
    
    return aircraft_list, flight_list



        