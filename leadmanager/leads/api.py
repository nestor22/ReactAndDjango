from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

#lead view set 
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        #por ahora no hay autenticacion
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer

