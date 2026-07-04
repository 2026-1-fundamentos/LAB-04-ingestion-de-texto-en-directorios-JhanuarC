# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    import pandas as pd
    from pathlib import Path
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```
    """
    ruta_base = Path(r"files\input")
    ruta_test = ruta_base / "test"
    ruta_train = ruta_base / "train"

    phrase_test = []
    target_test = []

    for archivo in ruta_test.rglob("*.txt"):#recorre todos los archivos txt en carpetas y subcarpetas
        contenido = archivo.read_text()
        phrase_test.append(contenido)
        target_test.append(archivo.parts[3])
    
    df_test = {"phrase": phrase_test,
               "target": target_test}#dataframe de test
    
    df_test = pd.DataFrame(df_test)


    #La misma logica para train
    
    phrase_train = []
    target_train= []

    for archivo in ruta_train.rglob("*.txt"):#recorre todos los archivos txt en carpetas y subcarpetas
        contenido = archivo.read_text()
        phrase_train.append(contenido)
        target_train.append(archivo.parts[3])

    df_train = {"phrase": phrase_train,
               "target": target_train}#dataframe de test
    
    df_train = pd.DataFrame(df_train)
    
    #Guardado de los csv
    carpeta_destino = Path(r"files\output")
    carpeta_destino.mkdir(parents=True, exist_ok=True)

    train_csv = carpeta_destino / "train_dataset.csv"
    test_csv = carpeta_destino / "test_dataset.csv"

    df_train.to_csv(train_csv, index=False )
    df_test.to_csv(test_csv, index=False )