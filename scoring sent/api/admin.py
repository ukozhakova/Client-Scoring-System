from django.contrib import admin
from .models import Client, Address, Document, Employment, BankAccount, Application, Request, Offer, Terrorist, BlackList, Gbdfl_Data_Table, Gcvp_Data_Table, Cb_Data_Table, Regional_Gcvp_Table
# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id','date_of_birth', 'first_name',  'IIN', 'last_name', 'Latin_First_Name', 'Latin_Last_Name', 'middle_name', 'place_of_birth',)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'client_id', 'flat', 'house', 'region', 'request_id', )

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_id', 'doc_number', 'doc_type', 'issuer', 'valid_from', 'valid_to', )

@admin.register(Employment)
class EmploymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_id', 'income_amount', 'income_type', 'request_id', )

@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'account_number', 'bank_name', 'BIC', 'BIN', 'client_id', )

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_id', 'created_by', 'created_date', 'credit_amount', 'document_id', 'monthly_payment', 'signed_by', 'signed_date', 'sms_code')

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_id', 'request_body', 'request_date', 'request_status', 'request_type', 'response_body', )

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'application_id', 'chosen', 'created_date', 'offer_amount', 'offered_monthly_payment', 'valid_from', 'valid_to', )

@admin.register(Terrorist)
class TerroristAdmin(admin.ModelAdmin):
    list_display = ('id', 'IIN',)

@admin.register(BlackList)
class BlackListAdmin(admin.ModelAdmin):
    list_display = ('id', 'IIN',)

@admin.register(Gbdfl_Data_Table)
class Gbdfl_Data_TableAdmin(admin.ModelAdmin):
    list_display=('id', 'IIN', 'date_of_birth', 'first_name', 'last_name', 'middle_name', 'place_of_birth', 'region', 'city', 'street', 'house', 'flat', 'marital_status',)

@admin.register(Cb_Data_Table)
class Cb_Data_TableAdmin(admin.ModelAdmin):
    list_display=('id', 'IIN', 'actual_dpd', 'historical_dpd', 'external_contract_number', 'monthly_payment', )

@admin.register(Gcvp_Data_Table)
class Gcvp_Data_TableAdmin(admin.ModelAdmin):
    list_display=('id', 'IIN', 'monthly_income')

@admin.register(Regional_Gcvp_Table)
class Regional_Gcvp_TableAdmin(admin.ModelAdmin):
    list_display= ('id', 'region', 'avg_income')