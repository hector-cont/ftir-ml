\# FTIR-OH Coníferas: PCA + 2D-COS + Deconvolución (Python)



Este repositorio contiene scripts y módulos en Python para el análisis reproducible de espectros FTIR de maderas de coníferas, con enfoque en la región de estiramiento O–H (típicamente 3700–3000 cm⁻¹) mediante una secuencia metodológica:



1\) Conversión de archivos (PerkinElmer `.sp` y/o JCAMP-DX `.jdx/.dx`) a CSV  

2\) Pretratamiento (recorte de rango, SNV y/o transformaciones según corresponda)  

3\) Análisis de Componentes Principales (PCA) y extracción de contribuciones por número de onda  

4\) Correlación bidimensional (2D-COS) sincrónica y asincrónica  

5\) Deconvolución espectral (cuando aplique al flujo de trabajo)



> Nota: el repositorio está diseñado para ser usado como \*\*flujo de trabajo\*\* (scripts) y como \*\*código reutilizable\*\* (módulos en `src/`).



---



\## Requisitos



\- Python (recomendado: 3.10+ o 3.12)

\- Paquetes principales: `numpy`, `pandas`, `matplotlib`, `scikit-learn`

\- Lectura de espectros:

&nbsp; - PerkinElmer `.sp`: requiere una librería de lectura compatible (según su entorno)

&nbsp; - JCAMP-DX: lector compatible (`.jdx/.dx`)



Las dependencias se documentan en:

\- `environment/conda-env.yml` (recomendado)

\- `environment/requirements.txt` (alternativa)



---



\## Instalación (conda)



```bash

conda env create -f environment/conda-env.yml

conda activate ftir-oh



