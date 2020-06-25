from django.db import models

# Create your models here.

class Client(models.Model):
    date_of_birth = models.DateField()
    first_name = models.CharField(max_length=255)
    IIN = models.CharField(max_length=12, null=False)
    last_name = models.CharField(max_length = 255)
    Latin_First_Name = models.CharField(max_length = 255)
    Latin_Last_Name = models.CharField(max_length = 255)
    middle_name = models.CharField(max_length = 255)
    place_of_birth = models.CharField(max_length = 255)

    def __str__(self):
            return '{}'.format(self.id)

class Address(models.Model):
    city = models.CharField(max_length = 255)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    flat = models.CharField(max_length = 255)
    house = models.CharField(max_length = 255)
    region = models.CharField(max_length = 255)
    request_id = models.CharField(max_length = 255)
    def __str__(self):
                return '{}'.format(self.id)



class BankAccount(models.Model):
    account_number = models.CharField(max_length = 255)
    bank_name = models.CharField(max_length = 255)
    BIC = models.CharField(max_length = 255)
    BIN = models.CharField(max_length = 255)
    client_id = models.ForeignKey(Client, on_delete= models.CASCADE)

    def __str__(self):
                return '{}'.format(self.id)

class Employment(models.Model):
    client_id = models.ForeignKey(Client, on_delete= models.CASCADE)
    income_amount = models.CharField(max_length = 255)
    income_type = models.CharField(max_length = 255)
    request_id = models.CharField(max_length = 255)

    def __str__(self):
                return '{}'.format(self.id)

class Document(models.Model):
    client_id = models.ForeignKey(Client, on_delete= models.CASCADE)
    doc_number = models.CharField(max_length = 255)
    doc_type = models.CharField(max_length = 255)
    issuer = models.CharField(max_length = 255)
    valid_from = models.DateField()
    valid_to = models.DateField()
    def __str__(self):
                return '{}'.format(self.id)

class Application(models.Model):
    client_id = models.ForeignKey(Client, on_delete= models.CASCADE)
    created_by = models.CharField(max_length = 255)
    created_date = models.DateField()
    credit_amount = models.CharField(max_length=255)
    document_id = models.ForeignKey(Document, on_delete=models.CASCADE)
    monthly_payment = models.CharField(max_length=255)
    signed_by = models.CharField(max_length=255)
    signed_date = models.DateField()
    sms_code = models.CharField(max_length = 4, default=1111)
    def __str__(self):
                return '{}'.format(self.id)

class Request(models.Model):
    client_id = models.ForeignKey(Client, on_delete= models.CASCADE)
    request_body = models.CharField(max_length=255)
    request_date = models.DateField()
    request_status = models.CharField(max_length=255)
    request_type = models.CharField(max_length=255)
    response_body = models.CharField(max_length=255)
    def __str__(self):
                return '{}'.format(self.id)

class Offer(models.Model):
    application_id = models.ForeignKey(Application, on_delete= models.CASCADE)
    chosen = models.CharField(max_length=255)
    created_date = models.DateField(max_length=255)
    offer_amount = models.CharField(max_length=255)
    offered_monthly_payment = models.CharField(max_length=255)
    valid_from = models.DateField()
    valid_to = models.DateField()
    def __str__(self):
                return '{}'.format(self.id)

class Terrorist(models.Model):
    IIN = models.CharField(max_length=12, null=False)
    def __str__(self):
        return '{}'.format(self.id)

class BlackList(models.Model):
    IIN = models.CharField(max_length=12, null=False)
    def __str__(self):
        return '{}'.format(self.id)

class Gbdfl_Data_Table(models.Model):
    IIN = models.CharField(max_length=12, null=False)
    date_of_birth = models.DateField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length = 255)
    middle_name = models.CharField(max_length = 255)
    place_of_birth = models.CharField(max_length = 255)
    region = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    street = models.CharField(max_length = 255)
    house = models.CharField(max_length = 255)
    flat = models.CharField(max_length = 255)
    marital_status = models.CharField(max_length = 255)
    def __str__(self):
        return '{}'.format(self.id)

class Cb_Data_Table(models.Model):
    IIN = models.CharField(max_length=12, null=False)
    monthly_payment = models.IntegerField()
    actual_dpd = models.IntegerField()
    historical_dpd = models.IntegerField()
    external_contract_number = models.CharField(max_length = 25, default='0')
    def __str__(self):
        return '{}'.format(self.id)

class Gcvp_Data_Table(models.Model):
    IIN = models.CharField(max_length=12, null=False)
    monthly_income = models.IntegerField()
    def __str__(self):
        return '{}'.format(self.id)


class Regional_Gcvp_Table(models.Model):
    region = models.CharField(max_length=30)
    avg_income = models.IntegerField()
