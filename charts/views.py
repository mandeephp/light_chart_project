from datetime import date, timedelta
import random
from django.shortcuts import render

from charts.models import ChartData


def chart_view(request):
    # start_date = date(2024, 8, 1)  # Adjust the year if necessary
    # end_date = date(2024, 8, 31)
    # delta = timedelta(days=1)
    #
    # while start_date <= end_date:
    #     ChartData.objects.create(
    #         date=start_date,
    #         value1=random.randint(0, 100),
    #         value2=random.randint(0, 100),
    #         value3=random.randint(0, 100)
    #     )
    #     start_date += delta

    august_data = ChartData.objects.filter(date__month=8, date__year=2024).order_by('date')

    # Prepare data for the chart
    chart_data = {
        'value1': [{'time': data.date.strftime('%Y-%m-%d'), 'value': data.value1} for data in august_data],
        'value2': [{'time': data.date.strftime('%Y-%m-%d'), 'value': data.value2} for data in august_data],
        'value3': [{'time': data.date.strftime('%Y-%m-%d'), 'value': data.value3} for data in august_data],
    }

    return render(request, 'chart_template.html', {'chart_data': chart_data})