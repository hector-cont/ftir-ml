"""
01_grafica_espectros_ftir_sp.py
================================

Este programa:

  * Busca todos los archivos con extensión .sp en la carpeta indicada.
  * Lee cada archivo usando la librería 'specio-py310'.
  * Grafica todos los espectros superpuestos en una sola figura.

NOTAS
-----

  * Se asume que cada archivo .sp contiene un único espectro.
  * El eje X se muestra en número de onda (cm⁻1) y se invierte
    (forma típica de FTIR: 4000 → 700 cm⁻1, por ejemplo).

Autor: Héctor J. Contreras Q.
Repositorio: https://github.com/hector-cont/ftir-ml
Diciembre de 2025.
"""

#*********************** IMPORTACIÓN DE LIBRERÍAS *****************************

import os
import glob

import matplotlib.pyplot as plt
from specio_py310 import specread

#********************** PARÁMETROS DEL USUARIO ********************************

# Carpeta donde se buscarán los archivos .sp
# Puede usar os.getcwd() para la carpeta actual
carpeta_trabajo = os.getcwd()                  # o escriba la ruta manualmente

# Patrón de búsqueda de archivos .sp
patron_archivos = "*.sp"

titulo_grafica = "Espectros FTIR"

#************************* LECTURA Y GRAFICACIÓN ******************************

def listar_archivos_sp(carpeta, patron="*.sp"):
    """
    Devuelve una lista ordenada de rutas a archivos .sp en la carpeta dada.
    """
    ruta_patron = os.path.join(carpeta, patron)
    archivos = sorted(glob.glob(ruta_patron))
    return archivos

def graficar_archivos_sp(carpeta, patron="*.sp", titulo=None):
    """
    Lee y grafica todos los archivos .sp encontrados en 'carpeta'
    que coincidan con 'patron'.
    """
    archivos = listar_archivos_sp(carpeta, patron)

    if not archivos:
        print("\nNo se encontraron archivos .sp en la carpeta:")
        print(carpeta)
        return

    plt.figure(figsize=(8, 5))

    for ruta in archivos:
        # Leer el espectro
        spec = specread(ruta)

        # En la mayoría de los casos amplitudes es 1D
        y = spec.amplitudes
        x = spec.wavelength

        nombre = os.path.splitext(os.path.basename(ruta))[0]
        plt.plot(x, y, linewidth=0.8, label=nombre)

    # Límites exactos del eje x (sin márgenes)
    plt.xlim(x.min(), x.max())

    # Formato típico FTIR: número de onda decreciente
    plt.gca().invert_xaxis()

    plt.xlabel("Número de onda (cm$^{-1}$)")
    plt.ylabel("Intensidad (u.a.)")

    if titulo:
        plt.title(titulo)

    # Mostrar leyenda solo si no hay demasiados espectros
    if len(archivos) <= 10:
        plt.legend(fontsize=8, loc="best")

    plt.tight_layout()
    plt.show()

    print(f"\nSe graficaron {len(archivos)} archivos .sp desde:")
    print(carpeta)

#***************************** PROGRAMA ***************************************

if __name__ == "__main__":
    graficar_archivos_sp(
        carpeta=carpeta_trabajo,
        patron=patron_archivos,
        titulo=titulo_grafica
    )

