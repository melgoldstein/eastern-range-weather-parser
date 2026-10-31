# Eastern Range weather parser
Synthetic Merritt Island / Cape Canaveral observations at one-minute cadence.
Run: `python parse_launch_weather.py sample_canaveral_met.csv summary.csv`.
Fields: timestamp, wind shear m/s/km, ceiling m and electric field kV/m.
Invalid observations are counted and excluded from numeric summaries.
The trailing 15-minute window reports exceedance counts and coverage.
Thresholds are educational proxies, not 45th Weather Squadron launch criteria.
Missing minutes remain visible through window coverage counts.
Check: `python -m unittest discover -s tests`. [Portfolio: melgoldstein.com](https://melgoldstein.com/)
