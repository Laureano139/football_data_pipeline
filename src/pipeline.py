from getTeamsData import *
from teamsDataProcessing import *

def runPipeline():
    userChoice = selectCountry()
    
    print("Getting teams data...\n")
    print(f"Country: {userChoice}\n")
    
    rawDataJson = getRawData(userChoice)

    print("Processing teams data...\n")
    
    df_filtered = processTeamsFile(rawDataJson)
    df2json(df_filtered, f"./data/processed/{userChoice}TeamsData.json")
    
    print("Pipeline executed successfully!\n")
    
if __name__ == "__main__":
    runPipeline()