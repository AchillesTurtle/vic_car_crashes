import pandas as pd
from pathlib import Path

# Class to load data
class CrashDataLoader():
    def __init__(self, path_list = ["./data/2000 to 2005 ACCIDENT","./data/ACCIDENT"]):
        # all functions will be dependant on path_list order
        self.path_list = path_list
        print("Loading data from: \n{}".format("\n".join(path_list)))
        
    def load_file(self, file_name):
        # append file from different sources without preprocessing
        df_list = [pd.read_csv(Path(folder_path) / file_name) for folder_path in self.path_list]
        data_df = pd.concat(df_list).reset_index(drop=True)
        data_df.columns = data_df.columns.str.lower()
        
        return data_df


    def load_severity_features(self):
        # [Not used]
        # Load features 
        accident_df = self.load_file("ACCIDENT.csv")
        location_df = self.load_file("ACCIDENT_LOCATION.csv")
        atmospheric_df = self.load_file("ATMOSPHERIC_COND.csv")
        node_df = self.load_file("NODE.csv")
        person_df = self.load_file("PERSON.csv")
        road_surface_cond = self.load_file("ROAD_SURFACE_COND.csv")
        vehicle = self.load_file("VEHICLE.csv")

        
        accident_df = accident_df.fillna({"accidenttime":"00.00.00"})	

        time_format = "%d/%m/%Y_%H:%M:%S"
        accident_df["accident_datetime"] = pd.DatetimeIndex(
            pd.to_datetime((accident_df["accidentdate"]+"_"+accident_df["accidenttime"]).str.replace(".", ":").str.strip(),
                           format = time_format))
        accident_df = accident_df.set_index("accident_datetime", drop=True)
        accident_df = accident_df.sort_values(by = ["accident_datetime", "accident_no"])

        org_row_count = len(accident_df)
        accident_df = accident_df.drop_duplicates(subset=['accidentdate', 'accidenttime', 'node_id'], keep="last")
        print("Dropped {} duplicate rows".format(org_row_count - len(accident_df)))

        accident_df = accident_df[["accident_no","node_id","light_condition","road_geometry","severity","speed_zone"]]

        return accident_df
        