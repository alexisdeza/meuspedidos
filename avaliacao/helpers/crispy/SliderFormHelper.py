from crispy_forms.helper import FormHelper

from crispy_forms.layout import Div, Layout, Field


class SliderFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        cancel_href = kwargs.pop('cancel_href', '#')
        super(SliderFormHelper, self).__init__(*args, **kwargs)
        self.form_class = 'form-horizontal'
        self.label_class = 'col-md-2'
        self.layout = Layout(
            Div(
                Field('col-md-8', css_class='col-md-8'),
                Div(
                    Field(css_class='form-control'),
                    Div(
                        Field('test', css_id='slider')
                    )
                )
            )
        )

        self.field_class = 'col-md-2'
