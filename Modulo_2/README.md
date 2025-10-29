# 📚 Módulo 2 – Libros & Bytes

Este proyecto corresponde al **Módulo 2 del Bootcamp de Ciencia de Datos**.  
El objetivo fue implementar un sistema para una pequeña cadena de librerías llamada *Libros & Bytes*, donde se desarrolla la lógica de gestión de inventario y simulación de compras en línea.  
El foco está en la **programación en Python**, sin interfaz visual, cumpliendo los requerimientos de control de flujo, funciones, condiciones, descuentos y facturación.

---

## 📂 Contenido
- `Libros & Bytes consolidado2.py`: Script en Python con la lógica del sistema.  
- `M2_Consolidado.rar`: Carpeta comprimida con los archivos del módulo.  

---

## 🛠️ Tecnologías usadas
- Python 3  
- Librerías: manejo nativo de listas y diccionarios  
- Estructuras de control (`if`, `for`, `while`)  
- Jupyter Notebook para pruebas y ejecución  

---

## 📋 Requerimientos implementados
1. **📑 Definición de variables básicas y tipos de datos**  
   - Lista de diccionarios con al menos 5 libros (`título`, `autor`, `precio`, `stock`).  

2. **🔄 Control de flujo**  
   - Función `mostrar_libros_disponibles()` que muestra los libros con stock disponible.  

3. **⚖️ Condiciones y operadores**  
   - Filtrado de libros según rango de precios ingresado por el usuario.  

4. **🛒 Función personalizada para compras**  
   - `comprar_libros(título, cantidad)` verifica existencia, stock y calcula el monto total.  

5. **♻️ Bucle while interactivo**  
   - Permite múltiples compras hasta que el usuario decida salir.  

6. **💸 Gestión de descuentos**  
   - Descuentos según título (ejemplo: 10% en *Introducción a Python*, 20% en *El señor de los anillos*, etc.).  
   - Muestra total sin descuento, monto descontado y total final.  

7. **🧾 Simulación de factura**  
   - Resumen final con: libros comprados, total sin descuento, descuento aplicado y monto total.  

---

## 🎯 Resultados principales
- Sistema funcional que permite:  
  - Consultar disponibilidad de libros.  
  - Filtrar por precio.  
  - Comprar libros con descuentos.  
  - Generar facturas de compra.  
- Simulación realista de un sistema de librería.  

---

✍️ *Autor: Liroy Cataldo*
