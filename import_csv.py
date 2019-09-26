import csv
import json

with open('mo_list.csv', 'r', encoding='utf-8') as organizations:
    fields = [
        'region_name',
        'year',
        'org_code',
        'full_name',
        'short_name',
        'org_form',
        'zip',
        'adress',
        'head_surename',
        'head_name',
        'head_second_name',
        'phone',
        'fax',
        'email',
        'license_number',
        'license_issue_date',
        'license_expiry_date',
        'activity_form',
        'registration_date',
    ]
    csv_reader = csv.DictReader(organizations, fields, delimiter=';')
    with open('new_json.json', 'w') as export:
        for row in csv_reader:
            json.dump(row, export, ensure_ascii=False, indent=2)
