import csv
from django.shortcuts import render
from django.http import HttpResponse

# This renders your index.html (The Login Page)
def index_view(request):
    return render(request, 'index.html')

# This renders your dashboard.html (The App)
def dashboard_view(request):
    # Simulated data for the demo
    context = {
        'original': {'male_rate': 80, 'female_rate': 20, 'ratio': 0.25, 'is_biased': True},
        'fixed': {'male_rate': 50, 'female_rate': 50, 'ratio': 1.0}
    }
    return render(request, 'dashboard.html', context)

def download_csv(request):
    import csv
    from django.http import HttpResponse
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sanitized_loans.csv"'
    writer = csv.writer(response)
    writer.writerow(['Applicant_ID', 'Gender', 'Approved_Status'])
    writer.writerow(['1001', 'Female', 'True'])
    return response