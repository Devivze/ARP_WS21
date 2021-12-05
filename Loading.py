import pandas as pd
import pickle

class DataLoad():
    def __init__(self):
        self.data = None

    def load(self):
        column_names = ['cell_id', 'sim_time', 'centre_SINR_dB', 'edge_SINR_dB', 'centre_RSRP_dB', 'edge_RSRP_dB',
        'interference_level1', 'interference_level2', 'interference_level3', 'interference_level4',
        'Intial_Number_Of_UEs', 'percentageCentreUsers',' 1 ', 'centre_power_factor', 'ECB',
        'antenna_downtilt', '2', 'cell_RSRP', 'averageInterferenceCreated','3' , 'current_centre_SINR_dB',
        'current_edge_SINR_dB', 'current_centre_RSRP_dB', 'current_edge_RSRP_dB', 'current_interference_level1',
        'current_interference_level2', 'current_interference_level3', 'current_interference_level4',
        'current_Intial_Number_Of_UEs', 'current_percentageCentreUsers']
        
        self.df = pd.read_csv('Temp_ICIC_CCO_SON_Stats.txt', sep='\t', names=column_names, index_col=False)

#%% Load models
def model_load(flag):
    if flag == 'CCO':
        with open('CCO_model.pkl', 'rb') as f:
            CCO_model = pickle.load(f)
            return CCO_model
    elif flag == 'ICIC':
        with open('ICIC_model.pkl', 'rb') as f:
            ICIC_model = pickle.load(f)
            return ICIC_model
    elif flag == 'KPI':
        with open('ICIC_CCO_model.pkl', 'rb') as f:
            ICIC_CCO_model = pickle.load(f)
            return ICIC_CCO_model

