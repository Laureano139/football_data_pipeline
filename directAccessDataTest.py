import json
import os

processedDataFolder = "./data/processed/"

filesInDir = os.listdir(processedDataFolder)

for i, file in enumerate(filesInDir, 1):
    print(f"{i} : {file}")

pickedFile = int(input("Select a file by number: \n>>>"))

file_path = f"{processedDataFolder}{filesInDir[pickedFile - 1]}"

with open(file_path, "r", encoding="utf-8") as json_file:
    teamsList = json.load(json_file)

for team in teamsList:
    print(f"Nome da Equipa: {team['Team_Name']}")
    print(f"País: {team['Country']}")
    print(f"Fundado em: {team['Founded']}")
    print(f"Estádio: {team['Stadium']}")
    print(f"Capacidade do Estádio: {team['Stadium_Capacity']}")
    print("-" * 20)