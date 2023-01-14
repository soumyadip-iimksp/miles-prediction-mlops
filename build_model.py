import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

import pickle

class PredictionModel:
    
    def __init__(self, alpha):
        self.alpha = alpha

    def model_fit(self, X, y):
        self.model = Ridge(alpha=self.alpha)
        self.X_train = X
        self.Y_train = y
        self.model.fit(self.X_train, self.Y_train)
        self.pred_op = self.model.predict(self.X_train)

        self.mse = mean_squared_error(self.Y_train, self.pred_op, squared=False)

        with open(f"ridge_auto_mse-{np.round(self.mse, 3)}.bin", "wb") as f_out:
            pickle.dump(self.model, f_out)
        return self.mse


if __name__ == "__main__":
    from fix_data import FixDatafarme
    fd = FixDatafarme("./auto-mpg.csv")
    fd.remove_columns(["Unnamed: 9", "car name"])
    fd.fix_col_names()
    fd.impute_missing()
    X, y = fd.return_df()
    model = PredictionModel(0.5)
    model.model_fit(X, y)