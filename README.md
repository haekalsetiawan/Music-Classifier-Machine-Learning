# Music Classifier Machine Learning

## Description
This repository contains a comprehensive project focused on music classification using machine learning. The project involves various stages including data preprocessing, label creation, model training, and evaluation. It leverages a dataset of normalized songs to predict music categories.

## Key Features
- **Preprocessing**: Scripts for cleaning and preparing music data.
- **Label Creation**: Scripts to create and assign labels based on song features.
- **Model Training**: Implements a machine learning pipeline to train models on the dataset.
- **Evaluation**: Scripts to evaluate the performance of trained models and generate reports.

## Installation
Clone the repository and install the required dependencies:

git clone https://github.com/haekalsetiawan/Music-Classifier-Machine-Learning.git

cd Music_Classifier_Machine_Learning

pip install -r requirements.txt

Usage
Preprocess the data:

python preprocessing.py

Create labels:

python create_labels.py

Train the model:

python training.py

Evaluate the model:

python evaluation.py

Example Output
              precision    recall  f1-score   support
      Short       0.87      0.85      0.86       100
     Medium       0.78      0.80      0.79       150
       Long       0.90      0.92      0.91       200
   accuracy                           0.87       450
  macro avg       0.85      0.86      0.85       450
weighted avg       0.87      0.87      0.87       450

Contributors
Haekal Setiawan (@haekalsetiawan)

License
This project is licensed under the MIT License - see the LICENSE file for details.
