# added
from rest_framework import serializers
from .models import Fieldworker
class FieldworkerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    function = serializers.CharField(required=False,default='Other')
    class Meta:
        model = Fieldworker
        #fields = ('first_name','id','last_name','function','created_at')
        fields = ('first_name','id','last_name','function')
