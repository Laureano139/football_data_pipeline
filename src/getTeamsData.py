import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

def selectCountry():
    countries = ["England", "Spain", "Italy", "Germany", "France", "Portugal"]
    
    print(">>> Select a country:\n")
    
    for i, country in enumerate(countries, 1):
        print(f"{i}. {country}")
        
    choice = int(input("Enter the number of your choice: \n>>> "))
    
    if 1 <= choice <= len(countries):
        return countries[choice - 1]
    else:
        print("Invalid choice! Choosing default country: Portugal...SIUUUUUUU\n")
        choice = "Portugal"
    return choice

def getRawData(userChoice):
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("\nAPI_KEY was not found!\n")

    url = f"https://v3.football.api-sports.io/teams?country={userChoice}"

    payload={}
    headers = {
        'x-rapidapi-host': 'v3.football.api-sports.io',
        'x-rapidapi-key': api_key,
        'x-apisports-key': api_key
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        print("\nRequest was successful!\n")
        data = response.json()
        jsonData = json.dumps(data, indent=4, ensure_ascii=False)
        with open(f"./data/raw/{userChoice}TeamsData.json", "w", encoding="utf-8") as jsonFile:
            jsonFile.write(jsonData)
    else:
        print(f"Error: {response.status_code}\n")

if __name__ == "__main__":
    userChoice = selectCountry()
    getRawData(userChoice)