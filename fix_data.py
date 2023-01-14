import pandas as pd
import numpy as np
from sklearn.feature_extraction import DictVectorizer
import pickle

class FixDatafarme:
    
    def __init__(self, path:str):
         self.path = path
         self.df = pd.read_csv(path)

    def remove_columns(self, col_names:list):
        self.df = self.df.drop(col_names, axis=1)
        return self.df

    def fix_col_names(self):
        cols = []
        for col in list(self.df.columns):
            cols.append(col.lower().replace(" ", "_"))
        self.df.columns = cols
        return self.df

    def impute_missing(self):
        self.cols = self.df.columns
        self.df = self.df[self.cols]
        self.df[self.cols] = self.df[self.cols].apply(pd.to_numeric, errors='coerce')
        for col in self.cols:
            if self.df[col].dtype != "object":
                #self.df[col] = self.df[col].apply(pd.to_numeric, errors='coerce')
                self.df[col].fillna(self.df[col].median(), inplace=True)
        return self.df

    def return_df(self):
        self.X = self.df.drop(["mpg"], axis=1)
        self.y = self.df["mpg"].values
        self.X = self.X.to_dict(orient="records")
        self.dv = DictVectorizer(sparse=False)
        self.dv.fit(self.X)
        self.X = self.dv.transform(self.X)
        with open(f"dv.bin", "wb") as f_out:
            pickle.dump(self.dv, f_out)
        return self.X, self.y


if __name__ == "__main__":
    fd = FixDatafarme("./auto-mpg.csv")
    fd.remove_columns(["Unnamed: 9", "car name"])
    fd.fix_col_names()
    fd.impute_missing()
    df = fd.return_df()
    print(df.head())