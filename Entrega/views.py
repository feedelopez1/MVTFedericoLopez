from django.http import HttpResponse
from django.template import Context,Template
from App.models import Integrante

def saludo(request):
   return HttpResponse('Hola')

#Asi aprendí a usar template

    
padre=Integrante('Ricardo','Padre',55,'08/12')
madre=Integrante('Claudia','Madre',54,'27/11')
hermana=Integrante('Paula','Hermana',26,'13/07')

def padrehtml(self):

   miHtml= open('D:/Users/Fedee/Django/Proyectos/Entrega/Plantillas/template1.html')
   diccionario={'nombre':padre.nombre,'relacion':padre.relacion,'edad':padre.edad,'fecha':padre.fecha}
   plantilla = Template(miHtml.read()) 
   miHtml.close()
   miContexto=Context(diccionario)
   documento=plantilla.render(miContexto)
   
   return HttpResponse(documento)



def madrehtml(self):

   miHtml= open('D:/Users/Fedee/Django/Proyectos/Entrega/Plantillas/template1.html')
   diccionario={'nombre':madre.nombre,'relacion':madre.relacion,'edad':madre.edad,'fecha':madre.fecha}
   plantilla = Template(miHtml.read()) 
   miHtml.close()
   miContexto=Context(diccionario)
   documento=plantilla.render(miContexto)
  
   return HttpResponse(documento)



def hermanahtml(self):
   
   miHtml= open('D:/Users/Fedee/Django/Proyectos/Entrega/Plantillas/template1.html')
   diccionario={'nombre':hermana.nombre,'relacion':hermana.relacion,'edad':hermana.edad,'fecha':hermana.fecha}
   plantilla = Template(miHtml.read()) 
   miHtml.close()
   miContexto=Context(diccionario)
   documento=plantilla.render(miContexto)

   return HttpResponse(documento)