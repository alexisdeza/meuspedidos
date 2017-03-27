from django.conf.urls import url

from avaliacao.views import FinalizarView
from . import views

urlpatterns = [
    url(r'^$', views.candidato, name='candidato'),
    url(r'^questionario/$', views.questionario, name='questionario'),
    url(r'^questionario/novo$', views.questionario, name='questionario_novo'),
    url(r'^finalizado$', FinalizarView.as_view, name='finalizar'),
]
