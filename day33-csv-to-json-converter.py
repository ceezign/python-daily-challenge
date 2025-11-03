# CSV to JSON Converter

import json
import csv
import os


def csv_to_json(csv_file_path, json_file_path, delimiter=','):
    try:
        with open(csv_file_path, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=delimiter)
            rows = list(reader)

        for row in rows:
            for key, value in row.items():
                if value.lower() in ['true', 'false']:
                    row[key] = value.lower() == 'true'
                else:
                    try:
                        if '.' in value:
                            row[key] = float(value)
                        else:
                            row[key] - int(value)
                    except ValueError:
                        pass

        with open(json_file_path, "w", encoding="utf-8") as json_file:
            json.dump(rows, json_file, indent=4)

        csv_size = os.path.getsize(csv_file_path)
        json_size = os.path.getsize(json_file_path)
        print("Conversion complete")
        print(f"Rows converted: {len(rows)}")
        print(f"CSV file size: {csv_size} bytes")
        print(f"CSV file size: {json_size} bytes")
    except FileNotFoundError:
        print("CSV file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def batch_convert(folder_path, delimiter=','):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            csv_path = os.path.join(folder_path, file_name)
            json_path = os.path.join(folder_path, file_name.replace('.csv', '.json'))
            csv_to_json(csv_path, json_path, delimiter)

if __name__ == "main__":
    csv_to_json('sample.csv', 'output.json')
