import os
import json
import yaml

def load_config_and_mapping():
    with open('mapping.yml', 'r') as file:
        config_and_mapping = yaml.safe_load(file)
    return (
        config_and_mapping.get('input_file', 'input_file'),
        config_and_mapping.get('output_file', 'output_file'),
        {item['substring']: item['category'] for item in config_and_mapping.get('mapping', [])}
    )

def apply_category_mapping(data, mapping):
    for key, value in data.items():
        current_malware_name = value.get("malware_name", "")
        
        # Check for each case-sensitive substring and update "category" accordingly
        for substring, category in mapping.items():
            if substring.lower() in current_malware_name.lower():
                value["category"] = category
                break
        
        # Remove '\n' from the end of all string fields
        for field, field_value in value.items():
            if isinstance(field_value, str):
                value[field] = field_value.rstrip('\n')

def save_to_json(data, output_directory, input_filename):
    # Constructing the output file path with a new name
    output_filename = os.path.join(output_directory, f'new_{os.path.basename(input_filename)}')
    
    with open(output_filename, 'w') as file:
        json.dump(data, file, indent=2)

def process_file(input_file, output_directory, mapping):
    # Process a single input file
    if not os.path.isfile(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        return
    
    with open(input_file, 'r') as file:
        data = json.load(file)

    apply_category_mapping(data, mapping)
    save_to_json(data, output_directory, input_file)

def main():
    # Load configuration and mapping from YAML
    input_file, output_directory, substring_to_category_mapping = load_config_and_mapping()

    # Ensure that output_directory is a valid directory
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Process the input file
    process_file(input_file, output_directory, substring_to_category_mapping)

if __name__ == "__main__":
    main()