
# Sistema de Gestión de Datos de Países - TPI Programación 1 (UTN)

## 📝 Descripción del Proyecto
Este proyecto es una aplicación de consola desarrollada en Python 3.x para la gestión, filtrado, ordenamiento y análisis de un dataset de países. El sistema permite interactuar dinámicamente con la información almacenada en un archivo de texto plano (CSV), garantizando la persistencia de los datos entre ejecuciones y aplicando de forma estricta los conceptos de modularización, estructuras repetitivas, condicionales, listas y diccionarios.

---

## 🛠️ Requisitos e Instalación
1. Asegúrese de tener instalado **Python 3.x** en su sistema.
2. Descargue o clone este repositorio en su máquina local:
   ```bash
   git clone https://github.com
   ```
3. Navegue a la carpeta del proyecto y ejecute el programa principal:
   ```bash
   py sistema_paises.py
   ```

---

## 🚀 Instrucciones de Uso
Al iniciar la aplicación, se desplegará un menú interactivo en la terminal con las siguientes opciones numéricas:
- **1. Agregar un país:** Permite registrar un nuevo país en el sistema ingresando nombre, población, superficie y continente. No se admiten campos vacíos ni duplicados.
- **2. Actualizar país:** Modifica la población y superficie de un país buscando por su coincidencia exacta.
- **3. Buscar un país por nombre:** Encuentra registros mediante búsquedas por coincidencia parcial.
- **4. Filtrar países:** Segmenta el dataset por continente o mediante rangos numéricos de población y superficie.
- **5. Ordenar países:** Organiza visualmente la información según el criterio seleccionado de manera ascendente o descendente mediante el algoritmo nativo de Ordenamiento Burbuja.
- **6. Mostrar estadísticas generales:** Despliega los valores máximos y mínimos, promedios globales y el conteo de países por continente.
- **0. Salir y Guardar cambios:** Vuelca la información actualizada en memoria RAM directamente dentro del archivo `paises.csv` y finaliza la ejecución.

---

## 📊 Ejemplos de Entradas y Salidas

### Ejemplo 1: Consulta de Estadísticas Generales (Opción 6)
**Entrada:** Selección de la opción `6` en el menú principal.
**Salida en consola:**
```text
----------------------------------------
         ESTADÍSTICAS GENERALES         
----------------------------------------
País con MAYOR población: Brasil (213,993,437 hab.)
País con MENOR población: Argentina (45,376,763 hab.)
Promedio de población global: 127,079,875.00 habitantes
Promedio de superficie global: 2,997,639.25 km²

Cantidad de países por continente:
 - América: 2
 - Asia: 1
 - Europa: 1
```

---

## 👥 Participación de los Integrantes
Este proyecto fue desarrollado por el siguiente alumno:

- **Integrante 1:** Viera, Marco — dni: `40830533` — [GitHub Profile](https://github.com/marcoviera97-oss)  
  *Responsabilidades:* Lógica de persistencia de archivos CSV, funciones de validación de entradas numéricas, menú interactivo y redacción de la documentación.
  
