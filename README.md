# TallerFinal
Taller Final Topicos Avanzados en IA

Este proyecto busca evaluar el proceso completo de MLOPS, empezando por la recolecci´on y procesamiento de datos, para generar una fuente de informaci´on lista para el entrenamiento de modelos
de Machine Learning. El modelo de mejor desempeno debe usarse para realizar inferencia mediante un API, la cual se consume mediante una interfaz grafica


Instrucciones: 
1. Ejecutar el docker_compose e Ingresar a http://10.43.102.113:8005/, y ejecutar la función /process_data (FAST API).
2. Se puede verificar que haya cargado bien la data en la base de datos local, ejecutando la función /Show Data (FAST API).
3. Ingresar a http://10.43.102.113:8888/, que cargará Jupyter. Ingresar con el password 123456
4. Ejecutar todo el cuaderno, que generará el procesamiento y la experimentación, en sincronía con MLflow.
5. Ingresar a http://10.43.102.113:5000/, donde se podrá acceder a la plataforma MLflow. user: admin, pass: supersecret
6. Generar la experimentación, la cual será cargada a Minio.
7. Ingresar a http://10.43.102.113:8501/, donde se encuentra una App que pedirá cargar un archivo CSV, que deberá contener una fila de data en el formato requerido por el modelo, que ejecutará el modelo en producción en MLflow.
8. El aplicativo generará la predicción. 

Nota: se cuenta con video explicativo del procedimiento en el siguiente link:
https://youtu.be/Er2ljl37ZCs
