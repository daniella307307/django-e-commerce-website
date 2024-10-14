from django.shortcuts import render
import requests  # Import the requests library to handle external HTTP requests

def get_exchange_rate(request):
    try:
        response = requests.get("https://open.er-api.com/v6/latest/USD")  # Use requests.get, not request.get
        response.raise_for_status()
        data = response.json()
        
        rates = data.get('rates')
        base_code = data.get('base_code')
        last_update = data.get('time_last_update_utc', '')
        next_update = data.get('time_next_update_utc', '')
        
        return render(request, 'data_display.html', {
            'rates': rates,
            'base_code': base_code,
            'last_update': last_update,
            'next_update': next_update
        })
        
    except requests.exceptions.RequestException as e:  # Correct way to handle exceptions from requests
        return render(request, 'error_message.html', {'error_message': str(e)})
