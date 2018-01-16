from django import forms
from django.core.exceptions import ValidationError
from django.forms import IntegerField, CharField, ChoiceField

BARRIOS = (
	('Manhattan', "Manhattan"),
	('Brooklyn', "Brooklyn"),
	('Queens', "Queens"),
	('Staten Island', "Staten Island"),
	('Bronx', "Bronx")
	)
def valida_codigo_postal(value):
	if value <10000 or value > 99999:
		raise ValidationError('%s, no parece ser un código postal' % value)
class RestauranteForm(forms.Form):

	name = forms.CharField(
	label='Nombre',
	max_length=60,
	strip=True,
	widget=forms.TextInput(
	attrs={ 'size':30,
	'placeholder':'Nombre',})
	)
	cuisine = forms.CharField(
	label='cuisine',
	max_length=80,
	required=False,
	widget= forms.TextInput(
	attrs={
	'size':80,
	'placeholder':'Cocina',})
	)

	zipcode = forms.IntegerField(
	label='Codigo Postal',
	validators=[valida_codigo_postal]
	)

	borough = forms.CharField(
	label='Barrio',
	max_length=20,
	strip=True,
	widget = forms.Select(
	choices=BARRIOS,
	 )
	)
TIPOS = (
	('Cocina', 'Cocina'),
	('Barrio', 'Barrio'),
	('Nombre', 'Nombre'),

	)
class BuscarRestauranteForm(forms.Form):
	nombre = forms.CharField(
        label='Tipo de búsqueda',
        strip=True,
        widget = forms.Select(
        choices=TIPOS,
        )
    )
    ayuda = forms.CharField(
        label='etiqueta',
        widget = forms.Select(
            choices=BARRIOS,

        )
    )
