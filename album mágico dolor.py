import random
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox

class CloudTa:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("CloudTA")
        self.ventana.geometry("900x600")
        ventana.resizable(False, True)  # --> Permiso de modificación o deformación de ventana (x,y)
        ventana.iconbitmap #--> Colocar un icono en el sector superior de la ventana
        ventana.attributes("-alpha", 0.98) # --> Configura el nivel de transparecncia 

        self.ventana.withdraw()

        self.u_btn = None  

        self.v_usuario() 

    def desplazable(self): # --> fracaso de barra desplazable
        self.de_barra = tk.Scale(self.ventana, bg="#A3BCB7", width=50, height=600)
        self.de_barra.pack(side="rigth", fill="y")


    def v_usuario(self): # --> ventana de usuario
        self.u_ventana = tk.Toplevel(self.ventana) # --> Lo lleva al frente
        self.u_ventana.title("¿Qué tal? Pediremos tu nombre de usuario para continuar")
        self.u_ventana.geometry("600x200") 
        
        self.lbl_ventanau = tk.Label(self.u_ventana, text="Piensa en un nombre de usuario y escríbelo a continuación:", font=("Arial", 14))
        self.lbl_ventanau.pack(pady=20)
        
        self.entrada_usuario = ttk.Entry(self.u_ventana, font=("Rodoni MT", 12))
        self.entrada_usuario.pack(pady=10)
        self.entrada_usuario.focus()
        
        self.btn_usuario = tk.Button(self.u_ventana, text="Listo", font=("Rodoni MT", 12), command=self.usuario)
        self.btn_usuario.pack(pady=10)
    
    def usuario(self): # --> sector de creación de usuario
        nom_usuario = self.entrada_usuario.get().strip()
        if nom_usuario:
            self.nombre = nom_usuario
            self.u_ventana.destroy()  # --> Cierra la ventana de usuario
            self.ventanaprincipal()  # --> ejecuta o muestra la ventana principal
        else:
            messagebox.showwarning("Al parecer no has colocado ningún nombre", "Intenta colocarlo nuevamente")
            messagebox.iconbitmap 
    
    def ventanaprincipal(self): # --> detalles de la ventana principal (gestor de contenido)
        self.iz_barra = tk.Frame(self.ventana, bg="#A3BCB7", width=200, height=600)
        self.iz_barra.pack(side="left", fill="y")

        self.sectortitulo = tk.Label(self.iz_barra, text="Álbum de Fotos", fg="white", bg="#A3BCB7", font=("Rodoni MT", 14, "bold"))
        self.sectortitulo.pack(pady=10)

        self.menu = ["Subir Imagen", "Crear Álbum", "Álbumes Creados", "Archivos", "Eliminar Imagen", "Historial"]
        for item in self.menu:
            self.crear_boton_menu(item)

        self.sup_barra = tk.Frame(self.ventana, bg="#A3BCB7", height=50)
        self.sup_barra.pack(side="top", fill="x")

        self.buscador = ttk.Entry(self.sup_barra, width=40)
        self.buscador.pack(side="left", padx=20, pady=10)
        self.buscador.bind("<Return>", self.buscar_album)  

       
        if self.u_btn is None:  # --> Crear el botón de usuario en la barra superior si no es existente.
            self.u_btn = tk.Button(self.sup_barra, text="Usuario", fg="white", bg="#444", relief="flat", font=("Rodoni MT", 12), command=self.mostrar_usuario)
            self.u_btn.pack(side="right", padx=20)

        self.cuadro = tk.Frame(self.ventana, bg="#f4f4f4")
        self.cuadro.pack(expand=True, fill="both")

        self.lbl_album = tk.Label(self.cuadro, text="Tus Álbumes", font=("Rodoni MT", 16, "bold"), bg="#f4f4f4")
        self.lbl_album.pack(pady=20)

        self.cuadro_imagenes = tk.Frame(self.cuadro, bg="#f4f4f4")
        self.cuadro_imagenes.pack()

        self.albums = {}
        self.history = []

        self.ventana.deiconify()

    def mostrar_usuario(self):
        messagebox.showinfo("Usuario", f"Bienvenido, {self.nombre}")
        messagebox.iconbitmap 
        self.u_btn.config(text=f"Bienvenido, {self.nombre}")

    def codigo(self):
        return str(random.randint(100000, 999999))

    def lista_historial(self, action):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append(f"{timestamp} - {action}")

    def menu(self, action):
        if action == "Crear Álbum":
            self.crear_album()
        elif action == "Subir Imagen":
            self.subirimg()
        elif action == "Álbumes Creados":
            self.mostrar_albumes()
        elif action == "Historial":
            self.historial()
        elif action == "Archivos":
            self.mostrar_archivos()
        elif action == "Eliminar Imagen":
            self.eliminar_imagen()

    def crear_boton_menu(self, item):
        if item == "Subir Imagen":
            accion = self.subirimg
        elif item == "Crear Álbum":
            accion = self.crear_album
        elif item == "Álbumes Creados":
            accion = self.mostrar_albumes
        elif item == "Historial":
            accion = self.historial
        elif item == "Archivos":
            accion = self.mostrar_archivos
        elif item == "Eliminar Imagen":
            accion = self.eliminar_imagen
        else:
            accion = self.nana

        btn = tk.Button(self.iz_barra, text=item, fg="white", bg="#444", relief="flat", font=("Rodoni MT", 16), width=20,
                       command=accion)
        btn.pack(pady=5, padx=10)

    def nana(self):
        messagebox.showinfo("nana de nana", "nada en particular.")
    
    def crear_album(self):
        nom_album = simpledialog.askstring("Nombre", "Crea tu álbum! Piensa creativamente y añade su nombre:")
        if nom_album is None: 
            return  
        if nom_album in self.albums:
            messagebox.showerror("No es posible crear el álbum", "Ya existe un álbum con este nombre.")
        else:
            self.albums[nom_album] = [] 
            self.lista_historial(f"Álbum '{nom_album}' se ha creado.")
            self.mostrar_albumes()  

    def subirimg(self):
        nombre = simpledialog.askstring("Subir imagen", "Crea un nombre y escríbelo:")
        if nombre is None:  
            return  
        album = simpledialog.askstring("Subir imagen", "Escribe el álbum al cual deseas subirlo:")
        if album is None:  
            return  
        comment = simpledialog.askstring("Subir imagen", "Escribe un comentario o salta este sector:")
        if comment is None: 
            comment = "" 

        if album == "":
            album = "Archivos"  

        if album not in self.albums:
            self.albums[album] = []

        if nombre and any(image["nombre"] == nombre for image in self.albums[album]):
            messagebox.showerror("El nombre es existente ", "Existe una imagen con este nombre.")
            return

        code = self.codigo() if not nombre else None  
        if not nombre:
            nombre = code  

        image_details = {
            "code": code,
            "nombre": nombre,
            "comment": comment,
            "upload_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), #--> hora exacta del dispositivo
            "album": album
        }
        self.albums[album].append(image_details)
        self.lista_historial(f"Imagen '{nombre}' subida al álbum '{album}' con código '{code}'.")
        messagebox.showinfo("Perfecto", f"Imagen '{nombre}' subida correctamente a '{album}'.")

    def mostrar_albumes(self):
        for widget in self.cuadro_imagenes.winfo_children():
            widget.destroy()

        for i, nom_album in enumerate(self.albums):
            doc_btn = tk.Button(self.cuadro_imagenes, text=nom_album, width=20, height=2, bg="white", relief="ridge",
                                command=lambda nom_album=nom_album: self.mostrar_imagenes(nom_album))
            doc_btn.grid(row=i // 3, column=i % 3, padx=10, pady=10)

    def mostrar_imagenes(self, nom_album):
        for widget in self.cuadro_imagenes.winfo_children(): 
            widget.destroy()

        for i, image in enumerate(self.albums.get(nom_album, [])):
            btn = tk.Button(self.cuadro_imagenes, text=image["nombre"], width=20, height=2, bg="white", relief="ridge",
                           command=lambda image=image: self.mostrar_detalles(image))
            btn.grid(row=i // 3, column=i % 3, padx=10, pady=10)

    def mostrar_detalles(self, image):
        detalles_ventana = tk.Toplevel(self.ventana)
        detalles_ventana.title("Detalles de la imagen")
        detalles_ventana.geometry("400x300")

        tk.Label(detalles_ventana, text=f"Título: {image['nombre']}", font=("ARodoni MTrial", 12)).pack(pady=10)
        tk.Label(detalles_ventana, text=f"Comentario: {image['comment']}", font=("Rodoni MT", 12)).pack(pady=10)
        tk.Label(detalles_ventana, text=f"Código: {image['code']}", font=("Rodoni MT", 12)).pack(pady=10)

        modificar_btn = tk.Button(detalles_ventana, text="Modificar", command=lambda: self.modificar_detalles(image))
        modificar_btn.pack(pady=10)

        mover_btn = tk.Button(detalles_ventana, text="Trasladar", command=lambda: self.mover_imagen(image))
        mover_btn.pack(pady=10)

        eliminar_btn = tk.Button(detalles_ventana, text="Eliminar", command=lambda: self.eliminar_imagen_confirmada(image))
        eliminar_btn.pack(pady=10)

    def modificar_detalles(self, image):
        nuevo_titulo = simpledialog.askstring("Modificar Imagen", "Cambio de nombre:")
        nuevo_comentario = simpledialog.askstring("Modificar Imagen", "Comentario nuevo:")

        if nuevo_titulo:
            image["nombre"] = nuevo_titulo
        if nuevo_comentario:
            image["comentario"] = nuevo_comentario

        self.lista_historial(f"Detalles de la imagen con código '{image['code']}' modificados.")
        messagebox.showinfo("perfecto", "Se han cambiado los detalles de la imagen.")

    def mover_imagen(self, image):
        album_actual = simpledialog.askstring("Mover Imagen", "Introduce el álbum de destino:")
        if album_actual not in self.albums:
            self.albums[album_actual] = []

        self.albums[album_actual].append(image)
        self.albums[image["album"]].remove(image)
        self.lista_historial(f"Imagen con código '{image['code']}' movida al álbum '{album_actual}'.")
        messagebox.showinfo("Éxito", f"Imagen movida al álbum '{album_actual}' con éxito.")

    def eliminar_imagen(self):
        nombre = simpledialog.askstring("Eliminar Imagen", "Escribe el nombre de la imagen que deseas eliminar:")
        if nombre:
            found = False
            for album in self.albums.values():
                for image in album:
                    if image["nombre"].lower() == nombre.lower():
                        album.remove(image)
                        self.lista_historial(f"Imagen '{nombre}' eliminada.")
                        found = True
                        messagebox.showinfo("Éxito", f"Imagen '{nombre}' eliminada correctamente.")
                        return
            if not found:
                messagebox.showwarning("No encontrada", "No se encontró ninguna imagen con ese nombre.")

    def mostrar_archivos(self):
        for widget in self.cuadro_imagenes.winfo_children():
            widget.destroy()

        for i, nom_album in enumerate(self.albums):
            if nom_album == "Archivos":
                for image in self.albums[nom_album]:
                    btn = tk.Button(self.cuadro_imagenes, text=image["nombre"], width=20, height=2, bg="white", relief="ridge",
                                   command=lambda image=image: self.mostrar_detalles(image))
                    btn.grid(row=i // 3, column=i % 3, padx=10, pady=10)

    def historial(self):
        ventanah = tk.Toplevel(self.ventana)
        ventanah.title("Historial")
        ventanah.geometry("400x300")

        for activity in self.history:
            tk.Label(ventanah, text=activity).pack()

    def buscar_album(self, event=None):
        consulta = self.buscador.get().lower()  
        self.cuadro_imagenes.destroy()
        self.cuadro_imagenes = tk.Frame(self.cuadro, bg="#f4f4f4")
        self.cuadro_imagenes.pack()

        for i, nom_album in enumerate(self.albums):
            if consulta in nom_album.lower():
                doc_btn = tk.Button(self.cuadro_imagenes, text=nom_album, width=20, height=2, bg="white", relief="ridge",
                                    command=lambda nom_album=nom_album: self.mostrar_imagenes(nom_album))
                doc_btn.grid(row=i // 3, column=i % 3, padx=10, pady=10)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = CloudTa(ventana)
    ventana.mainloop()
