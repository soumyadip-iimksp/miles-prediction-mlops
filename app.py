from flask import Flask
from flask import request as rq
from flask import jsonify
import pickle
import numpy as np

model_file = "./ridge_auto_mse-3.293.bin"

dv_file = "./dv.bin"

with open(model_file, "rb") as f_in:
    model = pickle.load(f_in)

with open(dv_file, "rb") as f_in:
    dv = pickle.load(f_in)


app = Flask("mile_predict")

@app.route("/predict", methods=["POST"])
def get_inference():
    data = rq.get_json()
    data = dv.transform(data)
#    data = np.array(data.values()).reshape(-1, 1).astype(float)
#    print(data)
#    print([y for x, y in data.items()])
    y_pred = model.predict(data)
    print(y_pred)
    result = {"predicted_mpg": float(y_pred)} 

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)