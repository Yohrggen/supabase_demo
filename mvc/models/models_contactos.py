import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

class ModelContactos:
    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL", ""),
                os.environ.get("SUPABASE_KEY", "")
            )
        except Exception as error: 
            print(f"ERROR 100: {error.args[0]}")

    def obtenerContactos(self):
        # SELECT * FROM contactos;
        response = self.supabase.table("contactos").select("*").execute()
        return response.data

    def buscarContacto(self, id_contacto:int):
        response = self.supabase.table("contactos").select("*").eq("id_contacto", id_contacto).execute()
        return response.data

    def crearContacto(self, nombre, email, telefono):
        # INsERT INTO contactos (nombre, emaul, telefono) VALUES ('?', '?', '?');
        data = {
            "nombre": nombre,
            "email": email,
            "telefono": telefono
        }
        response = self.supabase.table("contactos").insert({data}).execute()
        return response.data

    def borrarContacto(self, id_contacto):
        # DELETE FROM contactos WHERE id_contacto = ?;
        response = self.supabase.table("contactos").delete().eq("id_contacto", id_contacto).execute()
        return response.data

    def actualizarContacto(self, id_contacto, nombre, email, telefono):
        # UPDATE contactos SET nombre = ?, email = ?, telefono = ? WHERE id_contacto = ?;
        dato = {
            "nombre": nombre,
            "email": email,
            "telefono": telefono
        }
        response = self.supabase.table("contactos").update(dato).eq("id_contacto", id_contacto).execute()
        return response.data
                       

if __name__ == "__main__":
    model_contactos = ModelContactos()
    #print(model_contactos.obtenerContactos())
    #print(model_contactos.crearContacto("Juan", "juan@gmail.com", "123456789"))
    #model_contactos.borrarContacto(3)
    #model_contactos.actualizarContacto(4, "Carlos", "carlos@hotmail.com", "9876543211")
    
