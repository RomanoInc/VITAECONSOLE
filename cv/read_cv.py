import json


# Open and read the JSON file
def read_db():
    try:
        with open("db.json", "r", encoding="utf-8") as file:
            json_data = json.load(file)

            # Print the data
        return json_data["cvs"]    

    except FileNotFoundError:
        print("The JSON file was not found.")

    except json.JSONDecodeError:
        print("The JSON file is not valid.")
