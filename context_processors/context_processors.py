from about.models import Open_Close, Address, AboutModel
from doctor.models import Certificate, Doctor

def address(requset):
    return {'open': Open_Close.objects.all(), 'address': Address.objects.last(), 'about': AboutModel.objects.last(),
            'certificates': Certificate.objects.all(), 'doctor': Doctor.objects.all()}
