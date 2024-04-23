from rest_framework import serializers

from .models import Notebook
class NotebookSerializers(serializers.ModelSerializer):
    class Meta:
        model=Notebook
        fields = '__all__'
