import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging
from .forms import *
from django.contrib.auth.decorators import login_required

info_logger = logging.getLogger('info_logger')
error_logger = logging.getLogger('error_logger')

# Create your views here.

@login_required(login_url='Login')
def RatesView(request):
    rate_instance, _ = Rates.objects.get_or_create()
    form = RatesForm(instance=rate_instance)
    if request.method == 'POST':
        form = RatesForm(
            request.POST, instance=rate_instance)
        if form.is_valid():
            form.save()
    return render(request, './CRUD/Create_view.html', {'form': form})


class TripCost(APIView):
    def post(self, request):
        try:
            response = {'data': [], 'message': 'API Failed', 'status': 'failed'}
            try:
                data = json.loads(request.body)
            except:
                data = request.data
            distance = data.get('distance')
            time = data.get('time')
            DBP=Rates.objects.all().first().dbp
            TBP = Rates.objects.all().first().tbp
            cost = str(float(distance)*DBP + (float(time)*TBP )) + "$"
            response['data']= cost
            response['message'] = 'Total Trip Cost Details fetched successfully.'
            response['status'] = 'success'

            return Response(response, status.HTTP_200_OK)
        except Exception as e:
            error_logger.error(e, exc_info=True)
            return Response(response, status=status.HTTP_204_NO_CONTENT)