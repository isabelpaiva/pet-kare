from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .serializers import PetsSerializer
from groups.models import Group
from traits.models import Trait
from pets.models import Pet

class PetViews(APIView, PageNumberPagination):
    def post(self, request):
        serializer = PetsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        group = serializer.validated_data.pop("group")
        traits = serializer.validated_data.pop("traits")

        group_objeto = Group.objects.filter(scientific_name__iexact=group["scientific_name"]).first()
        if not group_objeto:
            new_group = Group.objects.create(**group)
            pet = Pet.objects.create(**serializer.validated_data, group=new_group)
        else:
            pet = Pet.objects.create(**serializer.validated_data, group=group_objeto)
        

        for trait in traits:
            trait_object = Trait.objects.filter(name__iexact=trait["name"]).first()
            if not trait_object:
                trait_object = Trait.objects.create(**trait)
            pet.traits.add(trait_object)
        
        serializer = PetsSerializer(pet)
        return Response(serializer.data, status=201)

    def get(self, request):
        pets = Pet.objects.all()
        trait = request.query_params.get("trait", None)
        if trait:
            pets_filter = Pet.objects.filter(traits__name=trait)
            result_page = self.paginate_queryset(pets_filter, request, view=self)
            serializer = PetsSerializer(result_page, many=True)
            return self.get_paginated_response(serializer.data)
        
        result_page = self.paginate_queryset(pets, request, view=self)
        serializer = PetsSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

  
        

        

