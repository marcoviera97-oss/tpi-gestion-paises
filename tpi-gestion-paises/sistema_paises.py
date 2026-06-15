import csv

# =====================================================================
# 1. FUNCIONES DE ARCHIVOS (PERSISTENCIA Y CARGA)
# =====================================================================

def leer_datos_csv(ruta_archivo):
    """Lee el archivo CSV y devuelve una lista de diccionarios de países."""
    paises = []
    try:
        with open(ruta_archivo, mode="r", encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
                    }
                    paises.append(pais)
                except (ValueError, KeyError):
                    continue
        print("¡Dataset cargado con éxito desde el archivo CSV!")
    except FileNotFoundError:
        print(f"Advertencia: No se encontró '{ruta_archivo}'. Se iniciará con un dataset vacío.")
    return paises

def guardar_datos_csv(ruta_archivo, paises):
    """Guarda la lista actual de países de vuelta en el archivo CSV."""
    try:
        with open(ruta_archivo, mode="w", encoding="utf-8", newline="") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for pais in paises:
                escritor.writerow(pais)
        print("¡Cambios guardados permanentemente en el archivo CSV!")
    except PermissionError:
        print("Error: No se pudo escribir en el archivo. Asegúrese de que no esté abierto en Excel.")

# =====================================================================
# 2. FUNCIONES DE GESTIÓN (AGREGAR, ACTUALIZAR, BUSCAR)
# =====================================================================

def agregar_pais(paises, nombre, poblacion, superficie, continente):
    """Agrega un nuevo país validando que no exista previamente."""
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print("Error: El país ya existe del sistema.")
            return False
            
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    paises.append(nuevo_pais)
    print(f"¡País '{nombre}' agregado exitosamente!")
    return True

def actualizar_pais(paises, nombre, nueva_pob, nueva_sup):
    """Actualiza los datos numéricos de un país buscando coincidencia exacta."""
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            pais["poblacion"] = nueva_pob
            pais["superficie"] = nueva_sup
            print(f"¡Datos de '{pais['nombre']}' actualizados correctamente!")
            return True
    print("Error: No se encontró ningún país con ese nombre exacto.")
    return False

def buscar_por_nombre(paises, busqueda):
    """Busca países por coincidencia parcial en el nombre."""
    resultados = []
    for pais in paises:
        if busqueda.lower() in pais["nombre"].lower():
            resultados.append(pais)
    return resultados

# =====================================================================
# 3. FUNCIONES DE FILTRADO
# =====================================================================

def filtrar_por_continente(paises, continente):
    resultados = []
    for pais in paises:
        if pais["continente"].lower() == continente.lower():
            resultados.append(pais)
    return resultados

def filtrar_por_rango_poblacion(paises, minimo, maximo):
    resultados = []
    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            resultados.append(pais)
    return resultados

def filtrar_por_rango_superficie(paises, minimo, maximo):
    resultados = []
    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            resultados.append(pais)
    return resultados

# =====================================================================
# 4. FUNCIONES DE ORDENAMIENTO (ALGORITMO BURBUJA NATIVO)
# =====================================================================

def ordenar_paises(paises, criterio, ascendente=True):
    """Ordena una copia del dataset mediante el método Burbuja."""
    lista_ordenada = paises.copy()
    n = len(lista_ordenada)
    for i in range(n):
        for j in range(0, n - i - 1):
            val1 = lista_ordenada[j][criterio]
            val2 = lista_ordenada[j + 1][criterio]
            
            if ascendente:
                intercambiar = val1 > val2
            else:
                intercambiar = val1 < val2
                
            if intercambiar:
                lista_ordenada[j], lista_ordenada[j+1] = lista_ordenada[j+1], lista_ordenada[j]
    return lista_ordenada


# =====================================================================
# 5. FUNCIONES ESTADÍSTICAS
# =====================================================================

def obtener_poblacion_extrema(paises, mayor=True):
    """Devuelve el país con mayor o menor población."""
    if not paises:
        return None
    extremo = paises[0]
    for pais in paises:
        if mayor:
            if pais["poblacion"] > extremo["poblacion"]:
                extremo = pais
        else:
            if pais["poblacion"] < extremo["poblacion"]:
                extremo = pais
    return extremo

def calcular_promedios(paises):
    """Calcula el promedio de población y superficie del dataset."""
    if not paises:
        return 0, 0
    total_pob = 0
    total_sup = 0
    for pais in paises:
        total_pob += pais["poblacion"]
        total_sup += pais["superficie"]
    return total_pob / len(paises), total_sup / len(paises)

def cantidad_por_continente(paises):
    """Devuelve un diccionario con el conteo de países por continente."""
    conteo = {}
    for pais in paises:
        cont = pais["continente"]
        conteo[cont] = conteo.get(cont, 0) + 1
    return conteo

# =====================================================================
# 6. INTERFAZ EN CONSOLA Y VALIDACIONES DE ENTRADA
# =====================================================================

def mostrar_tabla(lista_paises):
    """Muestra de forma tabular cualquier lista de países."""
    if not lista_paises:
        print("\n--> No se encontraron registros para mostrar.")
        return
    print(f"\n{'NOMBRE':<20} | {'POBLACIÓN':<12} | {'SUPERFICIE (km²)':<16} | {'CONTINENTE':<15}")
    print("-" * 72)
    for p in lista_paises:
        print(f"{p['nombre']:<20} | {p['poblacion']:<12,} | {p['superficie']:<16,} | {p['continente']:<15}")

def solicitar_entero_positivo(mensaje):
    """Fuerza al usuario a ingresar un entero válido mayor a 0."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= 0:
                return valor
            print("Error: El número debe ser mayor o igual a 0.")
        except ValueError:
            print("Error: Ingrese un número entero válido.")

def main():
    archivo_csv = "paises.csv"
    dataset = leer_datos_csv(archivo_csv)
    
    while True:
        print("\n" + "="*50)
        print("          SISTEMA INTERACTIVO DE PAÍSES UTN          ")
        print("="*50)
        print("1. Agregar un país")
        print("2. Actualizar Población y Superficie de un país")
        print("3. Buscar un país por nombre")
        print("4. Filtrar países")
        print("5. Ordenar países")
        print("6. Mostrar estadísticas generales")
        print("0. Salir y Guardar cambios")
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            print("\n--- AGREGAR NUEVO PAÍS ---")
            nom = input("Nombre: ").strip()
            if nom == "":
                print("Error: El nombre no puede estar vacío.")
                continue
            pob = solicitar_entero_positivo("Población: ")
            sup = solicitar_entero_positivo("Superficie (km²): ")
            cont = input("Continente: ").strip()
            if cont == "":
                print("Error: El continente no puede estar vacío.")
                continue
            agregar_pais(dataset, nom, pob, sup, cont)
            
        elif opcion == "2":
            print("\n--- ACTUALIZAR DATOS ---")
            nom = input("Ingrese el nombre exacto del país a modificar: ").strip()
            pob = solicitar_entero_positivo("Nueva población: ")
            sup = solicitar_entero_positivo("Nueva superficie (km²): ")
            actualizar_pais(dataset, nom, pob, sup)
            
        elif opcion == "3":
            bus = input("\nIngrese el nombre (o parte del nombre) a buscar: ").strip()
            res = buscar_por_nombre(dataset, bus)
            mostrar_tabla(res)
            
        elif opcion == "4":
            print("\nFiltrar por:\n1. Continente\n2. Rango de población\n3. Rango de superficie")
            sub_op = input("Opción: ").strip()
            if sub_op == "1":
                c = input("Ingrese el continente: ").strip()
                mostrar_tabla(filtrar_por_continente(dataset, c))
            elif sub_op == "2":
                mini = solicitar_entero_positivo("Población mínima: ")
                maxi = solicitar_entero_positivo("Población máxima: ")
                mostrar_tabla(filtrar_por_rango_poblacion(dataset, mini, maxi))
            elif sub_op == "3":
                mini = solicitar_entero_positivo("Superficie mínima: ")
                maxi = solicitar_entero_positivo("Superficie máxima: ")
                mostrar_tabla(filtrar_por_rango_superficie(dataset, mini, maxi))
                
        elif opcion == "5":
            print("\nOrdenar por:\n1. Nombre\n2. Población\n3. Superficie")
            c_op = input("Criterio: ").strip()
            criterios = {"1": "nombre", "2": "poblacion", "3": "superficie"}
            if c_op in criterios:
                sentido = input("1. Ascendente\n2. Descendente\nOpción: ").strip()
                asc = sentido == "1"
                lista_ord = ordenar_paises(dataset, criterios[c_op], asc)
                mostrar_tabla(lista_ord)
            else:
                print("Criterio inválido.")
                
        elif opcion == "6":
            if not dataset:
                print("\nNo hay datos para calcular estadísticas.")
                continue
            print("\n" + "-"*40)
            print("         ESTADÍSTICAS GENERALES         ")
            print("-"*40)
            p_max = obtener_poblacion_extrema(dataset, mayor=True)
            p_min = obtener_poblacion_extrema(dataset, mayor=False)
            prom_pob, prom_sup = calcular_promedios(dataset)
            conteos = cantidad_por_continente(dataset)
            
            print(f"País con MAYOR población: {p_max['nombre']} ({p_max['poblacion']:,} hab.)")
            print(f"País con MENOR población: {p_min['nombre']} ({p_min['poblacion']:,} hab.)")
            print(f"Promedio de población global: {prom_pob:,.2f} habitantes")
            print(f"Promedio de superficie global: {prom_sup:,.2f} km²")
            print("\nCantidad de países por continente:")
            for continente, cantidad in conteos.items():
                print(f" - {continente}: {cantidad}")
                
        elif opcion == "0":
            guardar_datos_csv(archivo_csv, dataset)
            print("\n¡Gracias por utilizar el sistema! Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    main()
