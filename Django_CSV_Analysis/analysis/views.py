from django.shortcuts import render, redirect
from .forms import CSVFileForm
from .models import CSVFile
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

def upload_file(request):
    if request.method == 'POST':
        form = CSVFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.save()
            return redirect('analysis:process_file', pk=csv_file.pk)
    else:
        form = CSVFileForm()
    return render(request, 'analysis/upload.html', {'form': form})

def process_file(request, pk):
    csv_file = CSVFile.objects.get(pk=pk)
    df = pd.read_csv(csv_file.file.path)

    first_rows = df.head().to_html()

    summary_stats = df.describe().to_html()

    df.fillna(df.mean(), inplace=True)
    missing_values = df.isnull().sum().to_frame(name='Missing Values').to_html()

    plots = []

    for column in df.select_dtypes(include=[np.number]).columns:
        plt.figure()
        sns.histplot(df[column], kde=True)
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        image_base64 = base64.b64encode(buf.read()).decode('utf-8')
        plots.append(image_base64)
        plt.close()

    context = {
        'first_rows': first_rows,
        'summary_stats': summary_stats,
        'missing_values': missing_values,
        'plots': plots,
    }

    return render(request, 'analysis/results.html', context)
