from django.forms.widgets import Input


class Html5EmailInput(Input):
    input_type = 'email'


class Html5NumberInput(Input):
    input_type = 'number'
