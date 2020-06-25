from django.shortcuts import render
import json
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from .models import Client, Terrorist, Application, BlackList, Gbdfl_Data_Table, Gcvp_Data_Table, Cb_Data_Table, Regional_Gcvp_Table
from rest_framework import generics
from django.views.generic import TemplateView, View
from .serializers import TerroristSerializer, ClientSerializer, ApplicationSerializer, BlackListSerializer, GbdflSerializer, GcvpSerializer, CbSerializer
# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        terrorists = Terrorist.objects.all()
        blacklists = BlackList.objects.all()
        applications = Application.objects.all()
        gbdfl_data = Gbdfl_Data_Table.objects.all()
        gcvp_data = Gcvp_Data_Table.objects.all()
        cb_data = Cb_Data_Table.objects.all()
        regional_gcvp_data = Regional_Gcvp_Table.objects.all()
        array_terrorists_IIN = [] 
        array_blacklists = [] 
        array_applications = []
        
        for terr in terrorists:
            array_terrorists_IIN.append(terr.IIN)
        for client in blacklists:
            array_blacklists.append(client.IIN)
        for app in applications:
            array_applications.append(app.client_id.IIN)
            array_applications.append(app.sms_code)
        
        clients_info_gbdfl = []
        client_info = {}
        for gbdfl in gbdfl_data:
            client_info = {
                "id": gbdfl.id,
                "IIN": gbdfl.IIN,
                "date_of_birth": gbdfl.date_of_birth,
                "first_name": gbdfl.first_name,
                "last_name": gbdfl.last_name,
                "middle_name": gbdfl.middle_name,
                "place_of_birth": gbdfl.place_of_birth,
                "region": gbdfl.region,
                "city": gbdfl.city,
                "street": gbdfl.street,
                "house": gbdfl.house,
                "flat": gbdfl.flat,
                "marital_status": gbdfl.marital_status
            }
            clients_info_gbdfl.append(client_info)
        
        clients_info_gcvp = []
        cl = {}
        for gcvp in gcvp_data:
            cl = {
                "id": gcvp.id,
                "IIN": gcvp.IIN,
                "monthly_income": gcvp.monthly_income
            }
            clients_info_gcvp.append(cl)
        clients_info_cb = []
        cli ={}
        for cb in cb_data:
            cli = {
                "id": cb.id,
                "IIN": cb.IIN,
                "monthly_payment": cb.monthly_payment,
                "actual_dpd": cb.actual_dpd,
                "historical_dpd": cb.historical_dpd
            }
            clients_info_cb.append(cli)
        regi = {}
        clients_info_reg = []
        for reg in regional_gcvp_data:
            regi = {
                "region": reg.region,
                "avg_income": reg.avg_income
            }
            clients_info_reg.append(regi)
        
        return render(request, "index.html", {'terrorists_IIN': array_terrorists_IIN, 'blacklists_IIN': array_blacklists, 'applications': array_applications, 'clients_info_gbdfl': clients_info_gbdfl, 'clients_info_gcvp': clients_info_gcvp, 'clients_info_cb': clients_info_cb, 'clients_info_reg': clients_info_reg})
        