"""Synthetic Eastern Range sensor-quality and rolling-exceedance summaries."""
import argparse, csv, math
from datetime import datetime, timedelta

def summarize(source, destination):
    valid = []; rejected = 0; seen = set()
    with open(source, newline='') as stream:
        for record in csv.DictReader(stream):
            try:
                timestamp = datetime.fromisoformat(record['timestamp'])
                readings = [float(record[column]) for column in ('wind_shear_mps_km','ceiling_m','electric_field_kvm')]
                if timestamp.tzinfo is None or timestamp in seen or not all(math.isfinite(v) for v in readings) or min(readings[:2]) < 0:
                    raise ValueError('Invalid sensor row')
                seen.add(timestamp)
                valid.append((timestamp, readings[0] > 12 or readings[1] < 1500 or abs(readings[2]) > 3))
            except (ValueError, KeyError):
                rejected += 1
    valid.sort()
    with open(destination, 'w', newline='') as stream:
        writer = csv.writer(stream); writer.writerow(['timestamp','window_observations','violations','rejected_total'])
        for timestamp, _ in valid:
            window = [violation for instant, violation in valid if timestamp-timedelta(minutes=15) < instant <= timestamp]
            writer.writerow([timestamp.isoformat(),len(window),sum(window),rejected])
    return len(valid), rejected

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source'); parser.add_argument('destination')
    arguments = parser.parse_args(); summarize(arguments.source, arguments.destination)
