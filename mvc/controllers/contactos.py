import web
from mvc.models.models_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class Contactos:

    def GET(self):

        model_contactos = ModelContactos()
        datos = model_contactos.obtenerContactos()
        print(datos)

        return render.contactos(datos)