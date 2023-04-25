```plaintext
8888888b.          d8b                        d8888 8888888b. 8888888 
888   Y88b         Y8P                       d88888 888   Y88b  888   
888    888                                  d88P888 888    888  888   
888   d88P 888d888 888  .d8888b .d88b.     d88P 888 888   d88P  888   
8888888P"  888P"   888 d88P"   d8P  Y8b   d88P  888 8888888P"   888   
888        888     888 888     88888888  d88P   888 888         888   
888        888     888 Y88b.   Y8b.     d8888888888 888         888   
888        888     888  "Y8888P "Y8888 d88P     888 888       8888888 

[*] Starting deploy...
[*] Deploy ready!
```

Proyecto orientado a la predicción de precios de la canasta básica, en función a los datos provenientes de la fuente pública del portal de **SEDECO** (México).

---

## Intro

Se dispone de los datos provenientes del portal de la Secretaría de Desarrollo Económico de la ciudad de México (<a href=https://www.sedeco.cdmx.gob.mx/servicios/servicio/seguimiento-de-precios-de-la-canasta-basica>SEDECO</a>), la cual publica periódicamente una lista de seguimiento de precios para los principales productos de la canasta básica. A través de esta información y mediante un análisis exploratorio se crea un dataset, que servirá como **base de conocimiento** para el desarrollo de un modelo de predicción diaria.


## Arquitectura

El pipeline implementado para este proyecto se basa en la siguiente arquitectura:

<a href="https://lh3.googleusercontent.com/drive-viewer/AFGJ81pGbwojd8YxPwRbZ1gdNb7phnrVggMmFi8d2RV7SB_QFDPVhuKxn-ELFZVNiz9OG1ZAeC0loRXVQTVSgYEEKZZM5d1k=s2560?source=screenshot.guru"> <img src="https://lh3.googleusercontent.com/drive-viewer/AFGJ81pGbwojd8YxPwRbZ1gdNb7phnrVggMmFi8d2RV7SB_QFDPVhuKxn-ELFZVNiz9OG1ZAeC0loRXVQTVSgYEEKZZM5d1k=s2560" /> </a>

## EDA (Exploratory Data Analysis)

+ El análisis exploratorio realizado así como el proceso ETL se realizó en base a los datos extraidos para la publicación de precios de todo el año 2022 y se puede oberservar <a href=https://github.com/v1c4r10us/pf_scrapper/blob/main/scraper.ipynb>Aquí</a>.

+ Para el caso del modelo de predicción debido a los recursos de disposición libre de la plataforma de despliegue, se ha optado por generar un objeto serializable (.pkl) con la libreria **pickle** de python en donde se realiza la compresión del modelo en un objeto serializable.

## Herramientas utilizadas

+ Python 3.8: Pandas, scikitLearn, skforecast, pickle

+ <a href=https://fastapi.tiangolo.com/>FastAPI</a>

+ Conda

+ <a href=https://www.uvicorn.org/>Uvicorn</a>

+ Git

+ <a href=https://railway.app/>Railway</a> 

+ AWS (Amazon Lex, AWS Lambda)


## Endpoints

**`About`**
```bash
curl -X 'GET' \
  'https://web-production-7526.up.railway.app/' \
  -H 'accept: application/json'
```

**`Predicción del precio para el día actual (Caso: "Arroz largo")`**
```bash
curl -X 'GET' \
  'https://web-production-7526.up.railway.app/get_actual_price' \
  -H 'accept: application/json'
```
## Deployment

<a href=https://web-production-7526.up.railway.app/>AQUÍ</a> se visualiza el deployment de la API Rest.

## Video demo

Enlace al video demostrativo <a href="https://youtu.be/QxeXjBa_K_M">AQUÍ</a>
Enlace al video de descripción del proyecto <a href="https://youtu.be/fhWzNFVrYj0">AQUÍ</>
