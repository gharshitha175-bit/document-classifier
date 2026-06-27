
a machine learning project that classifies documents into difference categories using python and scikit-learn
# Document Classifier

## Overview

This project is a Machine Learning-based Document Classifier built using Python. It classifies a document into one of the following categories:

* Resume
* Invoice
* News
* Research Paper

## Features

* Reads document text from user input.
* Converts text into numerical features using **TF-IDF Vectorizer**.
* Uses the **Multinomial Naive Bayes** algorithm for classification.
* Predicts the category of a document.

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Joblib

## Project Files

* `app.py` – Main application.
* `data.csv` – Training dataset.
* `requirements.txt` – Required Python libraries.
* `README.md` – Project documentation.

## How to Run

1. Install the required libraries:

   ```
   pip install -r requirements.txt
   ```

2. Run the project:

   ```
   python app.py
   ```

3. Enter a document when prompted.

### Example

**Input:**

```
Invoice number 67890
```

**Output:**

```
Category: Invoice
```

## Author

Harshitha Gowda
