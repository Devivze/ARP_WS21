from Loading import DataLoad
#from Loading import model_load
from separate import separate_data
#import eli5
#from eli5.sklearn import PermutationImportance
#from matplotlib import pyplot as plt
#from pdpbox import pdp, get_dataset, info_plots


#Load the data
flags = ['CCO','ICIC','KPI']
data_load =  DataLoad()
data_load.load()
df = data_load.df
cols_to_use = ['cell_id','percentageCentreUsers', 'centre_power_factor', 'ECB', 'antenna_downtilt']

# Separate data into training and validation sets
X_train, X_valid, y_CCO_train_CCO, y_CCO_valid, df = separate_data(df, flags[0])
X_train, X_valid, y__ICIC_train, y_ICIC_valid, df = separate_data(df, flags[1])     
X_train, X_valid, y_train, y_valid, df = separate_data(df, flags[2])
#df.head()
df.describe()