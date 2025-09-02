import json
import pandas as pd

def processTeamsFile(filePath):
    with open(filePath, "r", encoding="utf-8") as jsonFile:
        data = json.load(jsonFile)
        
    # for i in data['response']:
    #     print(i['team']['name'])
        
    df = pd.json_normalize(
        data['response'],
        sep='.',
        meta=['team', 'venue']
    )

    df = df[['team.name', 
             'team.country', 
             'team.founded', 
             'venue.name', 
             'venue.city', 
             'venue.capacity', 
             'venue.surface']]
    
    df.rename(columns={"team.name": "Team_Name", 
                       "team.country": "Country",
                       "team.founded": "Founded", 
                       "venue.name": "Stadium", 
                       "venue.city": "City", 
                       "venue.capacity": "Stadium_Capacity", 
                       "venue.surface": "TypeOfSurface"},
                    inplace=True)

    df = df.fillna("No information available.")
    # print(df.head())
    
    return df

def df2json(df, outputPath):
    df.to_json(outputPath, orient="records", indent=4, force_ascii=False)

# if __name__ == "__main__":
#     df_filtered = processTeamsFile("./data/raw/PortugalTeamsData.json")
#     df2json(df_filtered, "./data/processed/PortugalTeamsData.json")