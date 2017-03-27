from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Fieldset, HTML, MultiField, Submit
from django.core.mail import send_mail
from django.db import models
from django.forms import ModelForm
from django.urls import reverse
from django.utils import timezone

from avaliacao.helpers.crispy.ModelFormWithHelper import ModelFormWithHelper
from avaliacao.helpers.crispy.SliderFormHelper import SliderFormHelper
from . import fields


class Email:
    def __init__(self, *args, **kwargs):
        self.email = []
        self.estrategia(*args)

    def estrategia(self, questionario):
        if questionario.html >= 7 or questionario.css >= 7 or questionario.javascript > 7:
            self.email.append(
                'Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador Front-End entraremos em contato.')
        if questionario.python >= 7 or questionario.django >= 7:
            self.email.append(
                'Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador Back-End entraremos em contato.')
        if questionario.ios >= 7 or questionario.android >= 7:
            self.email.append(
                'Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador Front-End entraremos em contato.')
        if not self.email:
            self.email.append(
                'Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador entraremos em contato.')

    def enviar(self):
        for e in self.email:
            send_mail('Obrigado por se candidatar', e, 'avaliacao@questionario.com', )


class Candidato(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    create_at = models.DateTimeField('data_criado', auto_now_add=True)


class CandidatoForm(ModelForm):
    class Meta:
        model = Candidato
        exclude = ['create_at']

    def __init__(self, *args, **kwargs):
        super(CandidatoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = ''
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', 'Cadastrar', css_class='btn btn-success pull-right'))


class Questionario(models.Model):
    models.OneToOneField(
        Candidato,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    create_at = models.DateTimeField('data_criado', auto_now_add=True)
    html = fields.IntegerRangeField(min_value=0, max_value=10)
    css = fields.IntegerRangeField(min_value=0, max_value=10)
    javascript = fields.IntegerRangeField(min_value=0, max_value=10)
    python = fields.IntegerRangeField(min_value=0, max_value=10)
    django = fields.IntegerRangeField(min_value=0, max_value=10)
    ios = fields.IntegerRangeField(min_value=0, max_value=10)
    android = fields.IntegerRangeField(min_value=0, max_value=10)


class QuestionarioForm(ModelForm):
    class Meta:
        model = Questionario
        exclude = ['create_at']

    def __init__(self, *args, **kwargs):
        super(QuestionarioForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = 'novo'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', 'Enviar', css_class='btn btn-success pull-right'))
