from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import Target


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['name', 'ra', 'dec']


class ListTargets(ListCreateAPIView):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer


class DetailTarget(RetrieveAPIView):
    lookup_field = 'name'
    queryset = Target.objects.all()
    serializer_class = TargetSerializer

    def get(self, request, *args, **kwargs):
        target = kwargs['name']
        try:
            Target.objects.get(name=target)
        except Target.DoesNotExist:
            from astroquery.simbad import Simbad
            table = Simbad.query_object(target)
            if table is not None:
                row = table[0]
                new_target = Target(name=target, ra=row['RA'], dec=row['DEC'])
                new_target.save()
        return super().get(request, *args, **kwargs)



