import pickle

model_file = "./ridge_auto_mse-3.293.bin"

dv_file = "./dv.bin"

with open(model_file, "rb") as f_in:
    model = pickle.load(f_in)

with open(dv_file, "rb") as f_in:
    dv = pickle.load(f_in)


def lambda_handler(event, context):
    data = event["url"]
    data = dv.transform(data)
    y_pred = model.predict(data)
    print(y_pred)
    result = {"predicted_mpg": float(y_pred)} 
    return result