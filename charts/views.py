from datetime import date, timedelta
import random
from django.shortcuts import render

from charts.models import ChartData


from django.shortcuts import render
from .models import ChartData

def chart_view(request):
    # Query the ChartData model for data, ordering by date and time
    chart_data = ChartData.objects.all().order_by('date', 'time')

    # Prepare data for the chart
    chart_data_list = []
    for data in chart_data:
        chart_data_list.append({
            'time': f'{data.date}T{data.time.strftime("%H:%M:%S")}Z',
            'open': float(data.open),
            'high': float(data.high),
            'low': float(data.low),
            'close': float(data.close)
        })

    context = {
        'chart_data': chart_data_list
    }

    return render(request, 'chart_template.html', context=context)