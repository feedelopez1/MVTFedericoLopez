from django.http import HttpResponse
from django.template import Context,Template
from App.models import Integrante
from django.shortcuts import render

def familia(request):

   miHtml=open('D:/Users/Fedee/Django/Proyectos/MVTFederico/Plantillas/template1.html')

   padre=Integrante(nombre='Ricardo',relacion='Padre',edad=50,fecha='08/12')
   padre.save()
   diccionario={'pn':padre.nombre,'pr':padre.relacion,'pe':padre.edad,'pf':padre.fecha}

   madre=Integrante(nombre='Claudia',relacion='Madre',edad=49,fecha='27/11')
   madre.save()
   diccionario.update({'mn':madre.nombre,'mr':madre.relacion,'me':madre.edad,'mf':madre.fecha})

   hermana=Integrante(nombre='Paula',relacion='Hermana',edad=27,fecha='13/07')
   hermana.save()
   diccionario.update({'hn':hermana.nombre,'hr':hermana.relacion,'he':hermana.edad,'hf':hermana.fecha})

   plantilla = Template(miHtml.read())

   miHtml.close()

   miContexto=Context(diccionario)

   documento=plantilla.render(miContexto)
   return HttpResponse (documento)

'''
   padre=Integrante('Ricardo','Padre',55,'08/12')
   padre.save()
   diccionario={'pn':padre.nombre,'pr':padre.relacion,'p.e':padre.edad,'p.f':padre.fecha}

   madre=Integrante('Claudia','Madre',54,'27/11')
   madre.save()
   diccionario.update({'mn':madre.nombre,'mr':madre.relacion,'me':madre.edad,'mf':madre.fecha})

   hermana=Integrante('Paula','Hermana',26,'13/07')
   hermana.save()
   diccionario.update({'hn':hermana.nombre,'hr':hermana.relacion,'he':hermana.edad,'hf':hermana.fecha})
   
'''
