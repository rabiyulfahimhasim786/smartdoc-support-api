from rest_framework import serializers
from .models import Pdf, Outputtext

class Pdfserializers(serializers.ModelSerializer):
    class Meta:
        model = Pdf
        fields = '__all__'

class Outputtextserializers(serializers.ModelSerializer):
    class Meta:
        model = Outputtext
        fields = '__all__'