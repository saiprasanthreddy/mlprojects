"""Helpful utility functions for the machine learning project.

This file works like a small toolbox.
It gives us helpers for saving trained objects and checking how well our model works.

Think of it like this:
- save_object helps us keep a trained tool for later use.
- evaluate_model helps us check how good the model is by comparing its answers
  with the real answers.
"""

import sys
import dill
import os
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.exception import CustomException
from src.logger import logging


def save_object(file_path, obj):
    """Save a Python object to a file so it can be reused later.

    This is commonly used to save a trained preprocessor or model.
    The object is stored in a file on disk, like putting a tool in a box for later.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_model(X_train, y_train, X_test, y_test, models, params):
    """Train each model and measure how good it is.

    The function checks the model on both the training data and the test data.
    A higher R-squared score means the model is making better predictions.
    """
    try:
        report = {}

        for i in range(len(models)):
            model = list(models.values())[i]
            param = params.get(list(models.keys())[i], {})
            gs = GridSearchCV(model, param, cv=3, scoring='r2', n_jobs=-1, error_score='raise')
            gs.fit(X_train, y_train)
            model.set_params(**gs.best_params_)

            model.fit(X_train, y_train)

            y_test_pred = model.predict(X_test)
            y_train_pred = model.predict(X_train)

            test_model_score = r2_score(y_test, y_test_pred)
            train_model_score = r2_score(y_train, y_train_pred)

            report[list(models.keys())[i]] = {"test_score": test_model_score, "train_score": train_model_score}

        return report

    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path):
    """Load a Python object from a file.

    This is commonly used to load a trained preprocessor or model that was saved earlier.
    """
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)    