import csv


class LocationResolver:

    @staticmethod
    def resolve_same_code_to_zone_id(same_code: str) -> str:
        if same_code.startswith('0'):
            same_code = same_code[1:]
        path_to_data = "../data/bp05mr24.dbx.txt"
        with open(path_to_data, 'r') as f:
            reader = csv.reader(f, delimiter='|')
            for row in reader:
                if row[6] == same_code:
                    return f"{row[0]}Z{row[1]}"
