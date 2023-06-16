import pickle
import pandas as pd

__states = None
__model = None
__soil = None
__season = None

data = pd.read_csv("./artifacts/final_crops")
selected_state = {'Andaman and Nicobar Islands': 0,
                  'Andhra Pradesh': 1,
                  'Arunachal Pradesh': 2,
                  'Assam': 3,
                  'Bihar': 4,
                  'Chandigarh': 5,
                  'Chhattisgarh': 6,
                  'Dadra and Nagar Haveli': 7,
                  'Goa': 8,
                  'Gujarat': 9,
                  'Gujrat': 10,
                  'Haryana': 11,
                  'Himachal Pradesh': 12,
                  'Jammu and Kashmir':  13,
                  'Jharkhand': 14,
                  'Karnataka': 15,
                  'Kerala': 16,
                  'Madhya Pradesh': 17,
                  'Manipur': 18,
                  'Meghalaya': 19,
                  'Mizoram': 20,
                  'Nagaland': 21,
                  'Odisha': 22,
                  'Puducherry': 23,
                  'Punjab': 24,
                  'Rajasthan': 25,
                  'Sikkim': 26,
                  'Tamil Nadu': 27,
                  'Telangana': 28,
                  'Tripura': 29,
                  'Uttar Pradesh': 30,
                  'Uttarakhand': 31,
                  'West Bengal': 32}

selected_soil = {
 'ALL': 0,
 'Alluvial': 1,
 'Black': 2,
 'Clay': 3,
 'ClayLoamy': 4,
 'Coastalsandy': 5,
 'Gravel': 6,
 'Lateritic Loam': 7,
 'Lava': 8,
 'LightLoam': 9,
 'Loamtexture': 10,
 'Loamy': 11,
 'Notsandy': 12,
 'Peaty': 13,
 'Redclay': 14,
 'RedsandyLoam': 15,
 'Sandy': 16,
 'SandyLoamy': 17,
 'Sandyclay': 18,
 'Textured': 19
}
selected_season = {
    'Autumn': 0, 'Kharif': 1, 'Rabi': 2, 'Summer': 3, 'Whole Year': 4, 'Winter': 5}


def predict_crop(state, season, soil, rainfall):
    global __model
    with open("./artifacts/cp_model.pickle", 'rb') as f:
        __model = pickle.load(f)
        state_n = selected_state[state]
        soil_n = selected_soil[soil]
        season_n = selected_season[season]
        crop_names = set(data['Crop'])
        crop_list = [*crop_names, ]
        crop_list.sort()
        num_pred = __model.predict([[state_n, season_n, soil_n, rainfall]])
        pred = int(num_pred)
    return crop_list[pred]


def get_state_names():
    global __states
    s_names = set(data['State'])
    state_list = [*s_names, ]
    state_list.sort()
    __states = state_list
    return __states


def get_soil_type():
    global __soil
    s_names = set(data['Soil'])
    soil_list = [*s_names, ]
    soil_list.sort()
    __soil = soil_list
    return __soil


def get_season_name():
    global __season
    s_names = set(data['Season'])
    season_list = [*s_names, ]
    season_list.sort()
    __season = season_list
    return __season


if __name__ == "__main__":
    print(predict_crop('Rajasthan', 'Kharif', 'Redclay', 2800))
