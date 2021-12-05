import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor
import pickle

column_names = ['cell_id', 'sim_time', 'centre_SINR_dB', 'edge_SINR_dB', 'centre_RSRP_dB', 'edge_RSRP_dB',
'interference_level1', 'interference_level2', 'interference_level3', 'interference_level4',
'Intial_Number_Of_UEs', 'percentageCentreUsers',' 1 ', 'centre_power_factor', 'ECB',
'antenna_downtilt', '2', 'cell_RSRP', 'averageInterferenceCreated','3' , 'current_centre_SINR_dB',
'current_edge_SINR_dB', 'current_centre_RSRP_dB', 'current_edge_RSRP_dB', 'current_interference_level1',
'current_interference_level2', 'current_interference_level3', 'current_interference_level4',
'current_Intial_Number_Of_UEs', 'current_percentageCentreUsers']

#df2 = pd.read_csv('Temp_ICIC_CCO_SON_Stats.txt', sep='\t', names=column_names, index_col=False)


df = pd.read_csv('Temp_ICIC_CCO_SON_Stats.txt', sep='\t', names=column_names, index_col=False)
#df.to_csv('ICIC_CCO_with_KPI.txt', sep='\t', names=column_names, index_col=False)
#print(df[1:10])

# Select subset of predictors
cols_to_use = ['cell_id','percentageCentreUsers', 'centre_power_factor', 'ECB', 'antenna_downtilt']
X = df[cols_to_use]

# Select target
alpha = 0.6
KPI = (alpha*df.cell_RSRP)-((1-alpha)*df.averageInterferenceCreated)
df.loc[:,'KPI'] = KPI
y = KPI

# Separate data into training and validation sets
X_train, X_valid, y_train, y_valid = train_test_split(X, y)


#print("Mean Absolute Error: " + str(mean_absolute_error(predictions, y_valid)))

ICIC_CCO_model_new = XGBRegressor(n_estimators=1000, learning_rate=0.05, n_jobs=4)
ICIC_CCO_model_new.fit(X_train, y_train,
             early_stopping_rounds=5,
             eval_set=[(X_valid, y_valid)],
             verbose=False)

predictions_new = ICIC_CCO_model_new.predict(X_valid)
print("Mean Absolute Error: " + str(mean_absolute_error(predictions_new, y_valid)))

#print("Mean KPI: " + str(np.sum(df.KPI)/len(df.KPI)))
#print("Minimum KPI: " + str(np.min(df.KPI)))
#print("Maximum KPI: " + str(np.max(df.KPI)))

#%%save
with open('ICIC_CCO_model.pkl','wb') as f:
    pickle.dump(ICIC_CCO_model_new,f)

























