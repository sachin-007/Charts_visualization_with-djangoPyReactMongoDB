from dataclasses import field
from rest_framework import serializers;
from assignment.models import jsondatas

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=jsondatas
        fields=('assid','end_year','intensity','sector','topic','insight','url','region','start_year','impact','added','published','country','relevance','pestle','source','title','likelihood')