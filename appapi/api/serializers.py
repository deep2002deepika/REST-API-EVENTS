from rest_framework import serializers
from api.models import app

#create serializers here

class AppSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model=app
        fields=( 'name','files','tagline','schedule','description','moderator','category','sub_category','rigor_rank' )
