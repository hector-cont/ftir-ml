# ftir-ml

Repositorio para análisis reproducible de espectros FTIR (maderas, región O–H) mediante una secuencia de trabajo basada en:

- Pretratamiento (recorte de rango, SNV y transformaciones asociadas)
- PCA (cargas, scores, contribuciones por número de onda y mapas de calor)
- 2D-COS (mapas sincrónicos y asincrónicos)
- Deconvolución (cuando aplique)

El repositorio está organizado en:
- `scripts/` para ejecutar el flujo de trabajo (programas “corribles”).
- `src/` para funciones reutilizables (módulos).
- `docs/` para notas metodológicas y documentación.
- `data/sample/` para datos mínimos de ejemplo (sin datos sensibles).
- `results/` para figuras/tablas generadas.

## Requisitos

Python 3.10+ (recomendado 3.12) y librerías típicas: `numpy`, `pandas`, `matplotlib`, `scikit-learn`.
Las dependencias quedan documentadas en `environment/` (se agregará conforme se estabilice el entorno).

## Uso general

1. Coloque datos (si aplica) en `data/raw/` (no versionado).
2. Ejecute scripts desde `scripts/` en el orden indicado por el flujo.
3. Los resultados se guardan en `results/`.

## Reproducibilidad

- Versiones fijas de dependencias.
- Salidas guardadas en rutas consistentes.
- Scripts deterministas cuando aplica.

## Citación

Use el archivo `CITATION.cff` para citar este repositorio.

## Autor

Héctor J. Contreras Q.
