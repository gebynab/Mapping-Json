# Introduction
This program can modify the category based on the malware_name in the provided file.json using a dictionary that we have created.

# Installation
1. Install the required packages:

        `pip install pyyaml`

2. Fill in the configuration file `mapping.yml` to specify the input directory where your JSON file is located and define the output directory for the modified JSON file. Then create a dictionary that maps keywords to their corresponding new categories for changing the data's classification.
3. run the program :

        `py .\mapping.py`
