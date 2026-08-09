from flask import Flask, app, request, jsonify, render_template
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application 


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        # Some forms do not supply `math_score` because it's the target we predict.
        # Default to 0 when not provided so the pipeline receives a complete row.
        math_score_val = request.form.get('math_score')
        math_score_int = int(math_score_val) if math_score_val not in (None, '') else 0

        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('race_ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),    
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            math_score=math_score_int,
            reading_score=int(request.form.get('reading_score') or 0),
            writing_score=int(request.form.get('writing_score') or 0)
        )
        pred_df = data.get_data_as_dataframe()
        print(pred_df)
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        return render_template('home.html', prediction_text=f'Predicted Result: {results[0]}')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)