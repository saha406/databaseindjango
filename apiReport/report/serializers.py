from rest_framework import serializers

from report.models import Customers, Agents

 
 
class CustomersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customers
        fields = ['name']

class AgentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agents
        fields = ['agent_id', 'agent_state', 'agent_reason_code_text', 'station_dn']