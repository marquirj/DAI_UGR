from django import forms
from django.core.exceptions import ValidationError
from django.forms import IntegerField, CharField, ChoiceField

BARRIOS = (
	('Eligeuno', 'Elige uno'),
	('Manhattan', "Manhattan"),
	('Brooklyn', "Brooklyn"),
	('Queens', "Queens"),
	('Staten Island', "Staten Island"),
	('Bronx', "Bronx")
	)
COCINA = (
	('Eligeuno', 'Elige uno'),
	('Italian', "Italian"),
	('Chinese', "Chinese"),
	('Hamburgers', "Hamburgers"),
	('American', "American"),
	('Irish', "Irish")
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
	('Eligeuno', 'Elige uno'),
	('cuisine', 'Cocina'),
	('borough', 'Barrio'),
	('name', 'Nombre'),

	)
class BuscarRestauranteForm(forms.Form):
    tipo = forms.CharField(
    label = 'Búsqueda:',
    max_length = 20,
    strip=True,
    widget = forms.Select(
    choices=TIPOS,attrs={'id':'kk','css_class':'prueba','onchange':'cambiar()'},
    )
    )
    barriada = forms.CharField(
    label='Barrio',

    widget= forms.Select(
    choices=BARRIOS,
    attrs={'id':'borough', 'style':'visibility:hidden',}
    )
    )
    pornombre = forms.CharField(
    label='Introduce el nombre',
    max_length = 30,

    required=False,
    widget= forms.TextInput(
    attrs={
    'name':'name',
    'id':'name',
    'size':'30',
    'required':'False',
    'placeholder':'Nombre',
    'style':'visibility:hidden',
    }
    )
    )
    porcocina = forms.CharField(
    label='Tipo de cocina',
	required=True,

    widget= forms.Select(
    choices=COCINA,
    attrs={
    'id':'cuisine','name':'cuisine','style':'visibility:hidden',}
    )
    )
