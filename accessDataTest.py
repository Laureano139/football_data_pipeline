import json

file_path = "data/processed/PortugalTeamsData.json"

with open(file_path, "r", encoding="utf-8") as json_file:
    teamsList = json.load(json_file)

for team in teamsList:
    print(f"Nome da Equipa: {team['Team_Name']}")
    print(f"País: {team['Country']}")
    print(f"Fundado em: {team['Founded']}")
    print(f"Estádio: {team['Stadium']}")
    print(f"Capacidade do Estádio: {team['Stadium_Capacity']}")
    print("-" * 20)