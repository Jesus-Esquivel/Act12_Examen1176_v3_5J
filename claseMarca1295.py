class Marca1295 :

    def Diccionario_clientes_1295(self):
        diccionario = {
            "id_cliente: " : 111,
            "nombre: " : "jose manuel perez",
            "edad: " : 35,
            "correo electronico: " : "manupepe35@gmail.com",
            "telefono: " : 6569320122,
            "direccion: " : "Colonia Info. Aeropuerto, Calle Dirigible 9363",
            "forma de pago: " : "efectivo"
        }
        for a,b in diccionario.items():
                print(a,b)

    def Diccionario_juguetes_1295(self):
        print("\n")
        diccionario = {
            "id_juguete: " : 1131,
            "nombre: " : "Figura de accion Ironman",
            "fecha de fabricacion: " : "15 agosto del 2024",
            "marca: " : "Marvel",
            "precio: " : 150,
            "proveedor: " : "Jugueteria 2",
            "clasificacion: " : "mayores de 5 años"
        }
        for a,b in diccionario.items():
                print(a,b)

    def Diccionario_marcas_1295(self):
        print("\n")
        diccionario = {
            "id_marca: " : 999,
            "nombre: " : "Mattel",
            "sucursal" : "Planta 3, Calle Acueducto 3434",
            "correo electronico: " : "mattel@gmail.com",
            "telefono: " : 5518001210,
            "distribuidor: " : "Distribuidora Lozano",
            "tipo de producto: " : "juguetes para niño"
        }
        for a,b in diccionario.items():
                print(a,b)
                
    def Diccionario_proveedores_1295(self):
        print("\n")
        diccionario = {
            "id_proveedor: " : 4,
            "nombre: " : "Empresa Mattel 4",
            "direccion" : "Calle Aeronave 3434",
            "telefono: " : 6142348576,
            "correo electronico: " : "mattelsuc4@gmail.com",
            "vehiculo: " : "Camion de carga",
            "horario: " : "Lunes a viernes de 6:00 a.m a 6:00 p.m"
        }
        for a,b in diccionario.items():
                print(a,b)

objeto1295 = Marca1295()
objeto1295.Diccionario_clientes_1295()
objeto1295.Diccionario_juguetes_1295()
objeto1295.Diccionario_marcas_1295()
objeto1295.Diccionario_proveedores_1295()
