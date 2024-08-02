# Django CSV Analysis Web Application

This Django-based web application allows users to upload CSV files, perform data analysis using pandas and numpy, and display the results and visualizations on the web interface.

## Features

- **File Upload**: Users can upload CSV files.
- **Data Processing**:
  - Display the first few rows of the data.
  - Calculate summary statistics (mean, median, standard deviation) for numerical columns.
  - Identify and handle missing values.
- **Data Visualization**: Generate and display basic plots such as histograms for numerical columns.
- **User Interface**: Simple and user-friendly interface using Django templates.

## Setup and Installation

### Prerequisites

- Python 3.x
- Django 3.x or 4.x
- pandas
- numpy
- matplotlib
- seaborn

### Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/your-username/csv-analysis.git
    cd csv-analysis
    ```

2. **Create a virtual environment**:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

    Using Conda

     ```sh
     conda create -n env_name python==3.10 -y
     ```

4. **Install dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

5. **Apply migrations**:

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Run the development server**:

    ```sh
    python manage.py runserver
    ```

7. **Access the application**:

    Open a web browser and navigate to `http://127.0.0.1:8000/analysis/upload/`.

## Project Structure

```
csv_analysis/
├── analysis/
│ ├── migrations/
│ ├── templates/
│ │ └── analysis/
│ │ ├── upload.html
│ │ └── results.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── csv_analysis/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── manage.py
└── README.md
```

## Usage

1. **Upload CSV File**:
   - Navigate to the upload page (`http://127.0.0.1:8000/analysis/upload/`).
   - Upload a CSV file using the provided form.

2. **View Analysis Results**:
   - After uploading, the application will process the file and redirect to a results page displaying:
     - First few rows of the data.
     - Summary statistics for numerical columns.
     - Information on missing values.
     - Histograms for numerical columns.
