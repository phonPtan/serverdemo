import django_filters
from .models import CarInfo
from django_filters import DateFilter, CharFilter, TimeFilter,ChoiceFilter
from django import forms

class CarFilter(django_filters.FilterSet):
    LANECHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('C12', 'C12'),
    )
    lane = ChoiceFilter(choices =LANECHOICES,widget=forms.Select(attrs={'class': 'form-control'}))

    uniqueNumber = CharFilter(widget=forms.TextInput(attrs={'class': 'form-control'}))

    start_date = DateFilter(field_name='date',
                            lookup_expr='gte',
                            widget=forms.DateInput(
                                attrs={'class':'form-control','type': 'date'}))
    end_date = DateFilter(field_name='date',
                        lookup_expr='lte',
                        widget=forms.DateInput(
                                attrs={'class':'form-control','type': 'date'}))
    start_time = TimeFilter(field_name='time',
                            lookup_expr='gte',
                            widget = forms.TimeInput(attrs={'class':'form-control','type': 'time'}))
    end_time = TimeFilter(field_name='time',
                            lookup_expr='lte',
                            widget = forms.TimeInput(attrs={'class':'form-control','type': 'time'}))

    front_license_number = CharFilter(widget=forms.TextInput(attrs={'class': 'form-control'}))
    end_license_number = CharFilter(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = CarInfo
        fields = ['lane','uniqueNumber','time','date','front_license_number','end_license_number']