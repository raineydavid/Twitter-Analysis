# El trabajo consiste en un analisis del sentimiento de los tweet de la red de un usuario de twitter

## Se pretende entender el discurso politico mediante el sentimiento de los tweets de la red de los principales dirigentes politicos 

Para ello se ha realizado un RandomForestClassifier con un Dataset proporcionado por SEPLN el cual consta de tweets previamente etiquetados. Tras obtener una matriz de contexto de los Tweet y su posterior entrenamiento obteniendo los parametros mediante cross-validation, se obtuvo un accuracy del 57% por lo que se procedio a un analisis mediante una Red Neuronal de Keras.

La Red Neuronal reportó un acuraccy del 70%, por lo cual se uso este modelo para hacer las predicciones de la red de seguidores de twitter.

 La Red de seguidores se grafico mediante la libreria  PYVIS concretamente el modulo network, en la cual el usuario seleccionado para la extracción de la red se mostrará de color verde y sus seguidores seguirán el siguiente patron: 
 
Si el sentimiento es negativo: color = rojo                                                                                        

Si el sentimiento es positivo: color = azul                                                                                      

De esta forma se prentende estudiar la conexiones de los usuarios y la dispersión del sentimiento. Obteniendo asi la obtención de la posible influencia que puedan realizar los distintos seguidores en la red.

## Descripcion de los archivos 
1. [open_xlm_files](https://github.com/SergioMedBron/-TFM-Analisis-del-discurso-politico-en-Twitter/blob/master/open_xlm_files.ipynb): Obtencion del data set de entrenamiento desde la pagina web 

2. [Data_frame_entrenamiento](https://github.com/SergioMedBron/-TFM-Analisis-del-discurso-politico-en-Twitter/blob/master/Data_frame_entrenamiento.ipynb): Extracción de la matriz de sentimiento de los tweets a traves de un word embeddings pre-entrenado obtenido en  [dccuchile](https://github.com/dccuchile/spanish-word-embeddings) 

3. [Decisiontreeclassifier](https://github.com/SergioMedBron/-TFM-Analisis-del-discurso-politico-en-Twitter/blob/master/decisiontreeclasifier.ipynb): entrenamiento de DecisionTreeClassifier, acc= 54% y el RandomForestClassifier acc= 57%

4. [Neural_network_keras](https://github.com/SergioMedBron/-TFM-Analisis-del-discurso-politico-en-Twitter/blob/master/Neural_network_keras.ipynb): Entrenamiento red Neuronal usando la libreria Keras y con obteniendo el Embeddings de [dccuchile](https://github.com/dccuchile/spanish-word-embeddings) acc= 71% , el modelo se guardo para realizar con el las posteriores prediciones de la red

5. [Grid_of_followers_00](https://github.com/SergioMedBron/-TFM-Analisis-del-discurso-politico-en-Twitter/blob/master/Grid_of_followers_00.ipynb): Creación de la función de obtencion de los followers mediante el id del usuario de Twitter, se crea un archivo* csv con los id de los usuarios. 

6. [Funcion_peticion_tweets](https://github.com/SergioMedBron/-TFM-Analisis-del-discurso-politico-en-Twitter/blob/master/Funcion_peticion_de_tweets.ipynb): Realiza la extracción de los tweets del usuario y los guarda en un archivo* csv.

7. [Predictions](https://github.com/SergioMedBron/-TFM-Analisis-del-discurso-politico-en-Twitter/blob/master/Predictions.ipynb):
Contiene la funcion que prepara los tweets obtenidos y guardados en un archivo csv, para realizar las predicciones con la red neuronal previamente guardada.

8. [Visualization](https://github.com/SergioMedBron/-TFM-Analisis-del-discurso-politico-en-Twitter/blob/master/Visualization.ipynb): Contiene la funcion que creará el archivo HTML interactivo de la red del usuario [Carlos0520683grahp.html](https://github.com/SergioMedBron/-TFM-Analisis-del-discurso-politico-en-Twitter/blob/master/Carlos0520683grahp.html)

9. [Complet](https://github.com/SergioMedBron/-TFM-Analisis-del-discurso-politico-en-Twitter/blob/master/Complet.ipynb): Unifica las funciones creadas anteriormente, y añade la función de que perfila los distintos nodos en función del sentimiento** y devuelve la visualización en un archivo html interactivo.










###### Los archivos que se muestran como ejemplos en el codigo los podeis encontrar [aqui](https://drive.google.com/drive/folders/1sb_kMnyRKRgByDTUeUdGHD6k58ae7sK1?usp=sharing)

###### *Se ha determinado que se creen ficheros adicionales ya que de otro modo puede colapsar la memoria, es necesario tener más de 8 gb de ram para poder crear la red de sentimiento de los seguidores

###### **Actualmente twitter bloquea las peticiones de la api durante 15 min cada vez que se superan las 75.000 extracciones por lo que se por lo que se avisa que de ejecutar todo el proceso este se demorará horas e incluso días en funcion del número de seguidores del usuario que se quiera analizar. 

######  Agradecimientos a la comunidad de desarrolladores de internet y en particular a la comunidad de la tan socorrida y util llamada Stackoverflow y A los profesores del master de Kschool: en especial a Daniel Mateos y a Sebastien Perez los cuales no han tenido ningun reparo en poner a nuestra disposición todos sus conocimientos.
