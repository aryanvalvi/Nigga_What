# from flask import Flask, request, jsonify
# import xgboost as xgb
# import numpy as np
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)  # To allow cross-origin requests from the React frontend

# # Load the pre-trained XGBoost model
# model = xgb.XGBRegressor()
# model.load_model("model/xgboost_model2.json")  # Load your model here

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         data = request.get_json()

#         # Extract all required features from the request
#         feature1 = float(data['feature1'])
#         feature2 = float(data['feature2'])
#         feature3 = float(data['feature3'])
#         feature4 = float(data['feature4'])
#         feature5 = float(data.get('feature5', 0))  # Default value if feature not provided
#         feature6 = float(data.get('feature6', 0))
#         feature7 = float(data.get('feature7', 0))
#         feature8 = float(data.get('feature8', 0))
#         feature9 = float(data.get('feature9', 0))
#         feature10 = float(data.get('feature10', 0))
#         feature11 = float(data.get('feature11', 0))

#         # Prepare the input data for prediction
#         input_data = np.array([[feature1, feature2, feature3, feature4,
#                                  feature5, feature6, feature7, feature8,
#                                  feature9, feature10, feature11]])

#         # Get the prediction from the model
#         prediction = model.predict(input_data)

#         # Return the predicted value as a JSON response
#         return jsonify(predictedPrice=float(prediction[0]))

#     except Exception as e:
#         return jsonify(error=str(e)), 400

# if __name__ == '__main__':
#     app.run(debug=True, port=5001)

# from flask import Flask, request, jsonify
# import xgboost as xgb
# import numpy as np
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)  # To allow cross-origin requests from the React frontend

# # Load the pre-trained XGBoost model
# model = xgb.XGBRegressor()
# model.load_model("model/xgboost2_model.json")  # Load your model here

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         data = request.get_json()

#         # Extract all required features from the request (these are your actual features)
#         open_price = float(data['Open'])
#         high_price = float(data['High'])
#         low_price = float(data['Low'])
#         last_price = float(data['Last'])
#         close_price = float(data['Close'])
#         vwap = float(data['VWAP'])
#         volume = float(data.get('Volume', 0))  # Default to 0 if not provided
#         turnover = float(data.get('Turnover', 0))
#         trades = float(data.get('Trades', 0))
#         deliverable_volume = float(data.get('Deliverable Volume', 0))
#         percent_deliverable = float(data.get('%Deliverable', 0))

#         # Prepare the input data for prediction
#         input_data = np.array([[open_price, high_price, low_price, last_price,
#                                 close_price, vwap, volume, turnover,
#                                 trades, deliverable_volume, percent_deliverable]])

#         # Get the prediction from the model
#         prediction = model.predict(input_data)

#         # Return the predicted value as a JSON response
#         return jsonify(predictedPrice=float(prediction[0]))

#     except Exception as e:
#         return jsonify(error=str(e)), 400

# if __name__ == '__main__':
#     app.run(debug=True, port=5001)
from flask import Flask, request, jsonify
import xgboost as xgb
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # To allow cross-origin requests from the React frontend

# Load the pre-trained XGBoost model
model = xgb.XGBRegressor()
model.load_model("model/xgboost3_model.json")  # Load your model here

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Extract only the necessary features
        open_price = float(data['Open'])
        high_price = float(data['High'])
        low_price = float(data['Low'])
        close_price = float(data['Close'])
        volume = float(data['Volume'])

        # Prepare the input data for prediction
        input_data = np.array([[open_price, high_price, low_price, close_price, volume]])

        # Get the prediction from the model
        prediction = model.predict(input_data)

        # Return the predicted value as a JSON response
        return jsonify(predictedPrice=float(prediction[0]))

    except Exception as e:
        return jsonify(error=str(e)), 400

@app.route('/historicall/<symbol>', methods=['GET'])
def get_historical_data(symbol):
    # Implement your logic to fetch historical data for the given stock symbol
    # Return the data in JSON format
    pass  # Replace with your logic

if __name__ == '__main__':
    app.run(debug=True, port=5001) 


# from flask import Flask, request, jsonify
# import xgboost as xgb
# import numpy as np
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)  # To allow cross-origin requests from the React frontend

# # Load the pre-trained XGBoost model
# model = xgb.XGBRegressor()
# model.load_model("model/xgboost2_model.json")  # Load your model here

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         data = request.get_json()

#         # Extract only the required features from the request
#         open_price = float(data['Open'])
#         high_price = float(data['High'])
#         low_price = float(data['Low'])
#         last_price = float(data['Last'])
#         close_price = float(data['Close'])
#         volume = float(data['Volume'])  # Default to 0 if not provided

#         # Prepare the input data for prediction
#         input_data = np.array([[open_price, high_price, low_price, last_price,
#                                 close_price, volume]])

#         # Get the prediction from the model
#         prediction = model.predict(input_data)

#         # Return the predicted value as a JSON response
#         return jsonify(predictedPrice=float(prediction[0]))

#     except Exception as e:
#         return jsonify(error=str(e)), 400

# if __name__ == '__main__':
#     app.run(debug=True, port=5001)
