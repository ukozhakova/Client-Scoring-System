from rest_framework import serializers
from .models import Client, Address, Document, Employment, BankAccount, Application, Request, Offer, Terrorist, BlackList, Gbdfl_Data_Table, Cb_Data_Table, Gcvp_Data_Table, Regional_Gcvp_Table

class ClientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Client
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Address
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Document
        fields = '__all__'

class BankAccountSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = BankAccount
        fields = '__all__'

class EmploymentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Employment
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Application
        fields = '__all__'

class RequestSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Request
        fields = '__all__'

class TerroristSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Terrorist
        fields = '__all__'

class BlackListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = BlackList
        fields = '__all__'

class GbdflSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Gbdfl_Data_Table
        fields = '__all__'

class CbSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Cb_Data_Table
        fields = '__all__'

class GcvpSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Gcvp_Data_Table
        fields = '__all__'

class Regional_Gcvp_TableSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Regional_Gcvp_Table
        fields = '__all__'