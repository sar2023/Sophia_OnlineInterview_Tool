from django.urls import path
from administration.views import * 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',staffLogin,name='staffLogin'),
    path('dashboard/',dashboard,name='dashboard'),
    path('allAnswer/',allAnswer,name='allAnswer'),
    path('searchbar/',searchbar,name='searchbar'),
    path('dashboard/Add',Add_assessment,name='Add'),
    path('dashboard/assessment/<int:ass_id>/',view_assessments,name='view'),
    path('allAnswer/<int:ansId>/',view_analysis,name='view_analysis'),
    path('allAnswer/generate_tras/<int:ansId>/',generate_tras,name='generate_tras'),
    path('addquestion/',Add_question,name='Addquestion'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)