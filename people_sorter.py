import json

# file reader function
def file_reader(filename):
    try:
        with open(filename) as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("FILE NOT FOUND")
        return []

def dictionary_filter(data):
    # takes file data and filters clean 'name' and 'email' and sorts by country and age
    # returns clean data
    cleaned_data = [person for person in data if person.get('name', '').strip() != '' and person.get('email', '').strip() != '']
    cleaned_data = sorted(cleaned_data, key=lambda x: (x['country'].lower(), x['age']))
    print(f"{len(cleaned_data)} valid records found. Writing country files...")
    return cleaned_data


def country_output(cleaned_data):
    # takes clean data and writes a new json file for each country
    groups = {}
   
    for person in cleaned_data:
        country = person.get('country', 'Unknown').lower()
        groups.setdefault(country, []).append(person)
    
    summary = []

    for country, people in groups.items():
        output_data = {
            'country': country,
            'count': len(people),
            'people': people
        }
        with open(f'{country}_people.json', 'w') as file_out:
            json.dump(output_data, file_out, indent=2)

        summary.append({
            'country': country,
            'count': len(people)
        })

    return summary

def summary_report(data, cleaned_data, summary, output_file):
    # total records in original file
    # how many were cleaned and kept
    # how many entries per country
    # writes txt file
    data_count = len(data)
    clean_count = len(cleaned_data)
    report = (
        f"Total records in input: {data_count}\n"
        f"Valid records kept: {clean_count}\n\n\n"
        f"--- Records by Country ---\n"
    )

    for item in summary:
        report = report + f"{item['country'].title()}: {item['count']}\n"

    with open(output_file, 'w') as file:
        file.write(report)
    
    print(f"Summary report saved to {output_file}")

def main():
    input_file = input("Enter file name (JSON format): ")
    output_file = input("Enter summary report output filename (will be .txt): ")
    data = file_reader(input_file)
    if data:
        cleaned_data = dictionary_filter(data)
        summary = country_output(cleaned_data)
        summary_report(data, cleaned_data, summary, output_file)

if __name__ == "__main__":
    main()
    