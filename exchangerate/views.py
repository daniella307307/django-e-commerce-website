from django.shortcuts import render

# Create your views here.
def get_exchange_rate(request):
      try:
          response = request.get("https://open.er-api.com/v6/latest/USD")
          response.raise_for_status()
          data = response.json()
          
          rates = data.get('rates')
          base_code = data.get('base_code')
          last_update = data.get('time_last_update_utc','')
          next_update = data.get('time_next_update_utc','')
          
          return render(request, 'data_display.html',{
              'rates': rates,
              'base_code': base_code,
              'last_update': last_update,
              'next_update': next_update
          })
          
      except request.exceptions.RequestException as e:
          return render(request, 'error_message.html', {'error_message': str(e)})