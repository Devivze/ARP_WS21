from sklearn.model_selection import train_test_split
# Separate dataset into training and validation data
def separate_data(df, flag):
        cols_to_use = ['cell_id','percentageCentreUsers', 'centre_power_factor', 'ECB', 'antenna_downtilt']
        X = df[cols_to_use]  # Select subset of predictors and target
        if flag == 'CCO':
            y = df.cell_RSRP
            X_train, X_valid, y_train, y_valid = train_test_split(X, y)
            
        elif flag == 'ICIC':
            y = df.averageInterferenceCreated
            X_train, X_valid, y_train, y_valid = train_test_split(X, y)
            
        elif flag == 'KPI':
            alpha = 0.6
            KPI = (alpha*df.cell_RSRP)-((1-alpha)*df.averageInterferenceCreated)
            df.loc[:,'KPI'] = KPI
            y = KPI
            X_train, X_valid, y_train, y_valid = train_test_split(X, y)
        return X_train, X_valid, y_train, y_valid, df