# Módulo 2 – Libros & Bytes

Este proyecto corresponde al **Módulo 2 del Bootcamp de Ciencia de Datos**.  
El objetivo fue implementar un sistema para una pequeña cadena de librerías llamada *Libros & Bytes*, donde se desarrolla la lógica de gestión de inventario y simulación de compras en línea.  
El foco está en la **programación en Python**, sin interfaz visual, cumpliendo los requerimientos de control de flujo, funciones, condiciones, descuentos y facturación.

---

## Contenido
- `Libros & Bytes consolidado2.py`: Script en Python con la lógica del sistema.  
- `M2_Consolidado.rar`: Carpeta comprimida con los archivos del módulo.  

---

## Tecnologías usadas
- Python 3  
- Librerías: manejo nativo de listas y diccionarios  
- Estructuras de control (`if`, `for`, `while`)  
- Jupyter Notebook para pruebas y ejecución  

---

## Requerimientos implementados
1. **Definición de variables básicas y tipos de datos**  
   - Se construyó una lista de diccionarios que contiene al menos 5 libros, cada uno con: `título`, `autor`, `precio` y `stock`.

2. **Control de flujo**  
   - Función `mostrar_libros_disponibles()` que recorre el inventario y muestra los libros con unidades en stock.

3. **Condiciones y operadores**  
   - El usuario ingresa un rango de precios, y el sistema filtra los libros disponibles dentro de ese rango.

4. **Función personalizada para simular compras**  
   - Función `comprar_libros(título, cantidad)` que:
     - Verifica la existencia del libro.  
     - Revisa si hay stock suficiente.  
     - Descuenta la cantidad comprada y calcula el total a pagar.  
     - Maneja errores cuando no hay suficiente stock.  

5. **Bucle while interactivo**  
   - Permite al usuario realizar varias compras hasta que decida salir del sistema.  

6. **Gestión de descuentos**  
   - Se implementó un sistema de descuentos por libro:  
     - Ejemplo: 10% en *Introducción a Python*, 20% en *El señor de los anillos*, etc.  
   - Se calcula el monto sin descuento, el descuento aplicado y el total final.  

7. **Simulación de factura**  
   - Al finalizar, se muestra un resumen con:  
     - Libros comprados.  
     - Monto total sin descuento.  
     - Descuento aplicado.  
     - Monto total con descuento.  

---

## Resultados principales
- Sistema funcional que permite:
  - Consultar disponibilidad de libros.  
  - Filtrar por precio.  
  - Comprar libros aplicando descuentos.  
  - Mostrar facturas de compra.  
- Se simula un entorno realista de compra para la librería *Libros & Bytes*.  

---

✍️ *Autor: Liroy Cataldo*
