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

class ModificarRestaurantes(forms.Form):
	name = forms.CharField(
	label='Nombre',
	max_length=60,
	strip=True,
	widget=forms.TextInput(
	attrs={ 'size':30,
	'placeholder':'Nombre',})
	)
	restaurant_id= forms.CharField(
	label='id',
	max_length=60,
	strip=True,
	widget=forms.HiddenInput(
	attrs={ 'size':30,
	'placeholder':'Nombre', 'visibility':'hidden',})
	)
	cuisine = forms.CharField(
	label='Cocina',
	max_length=80,
	required=False,
	widget = forms.Select(
	choices=COCINA,
	 )
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
	label='Cocina',
	max_length=80,
	required=False,
	widget = forms.Select(
	choices=COCINA,
	 )
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
    attrs={'id':'borough', 'name':'borough','style':'visibility:hidden',}
    )
    )
    porcocina = forms.CharField(
    label='Tipo de cocina',
    widget= forms.Select(
    choices=COCINA,
    attrs={
    'id':'cuisine','name':'cuisine','style':'visibility:hidden',}
    )
    )
