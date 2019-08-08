# ECI 2019 - NLP
## TP del curso "Procesamiento del lenguaje natural mediante redes neuronales"

# Author
* Lucia Maité Vázquez
* Lucas Ponce de León

# USO

## Descargar el repo y realizar lo siguiente

### Dar permiso a los script disparadores

```
chmod u+x tpnli2019/scripts/crearModelo.sh
chmod u+x tpnli2019/scripts/ejecutarModelo.sh
chmod u+x tpnli2019/scripts/prepararEntradas.sh
chmod u+x tpnli2019/scripts/probarModelos.sh
```

### Crear una carpeta llamada entradas dentro de scripts
```
mkdir entradas
```

***NOTA DESDE ESTE MOMENTO TODOS LOS PARAMETROS ENTRE COMILLAS***

### Descargar de kaggle snli_1.0_train_filtered.jsonl y pegarlo en Files Kaggle

### Preparar las entradas para fasttext
esto lo hacen solo la primera vez. Entrar a script y ejecutar

```
./prepararEntradas.sh
```

verificar que en la carpeta entradas esten los dos archivos necesarios para fasttext

### Obtener el modelo
aca jueguen con los valores de la linea 9 de crear_modelo.py
```
./crearModelo.sh <nombre del modelo sin .bin>
```

### Probar el modelo
con esto obtienen los porcentajes
```
./probarModelo.sh <nombre del modelo con .bin>
```

### Ejecutar modelo

```
./ejecutarModelo.sh <nombre del archivo de direcciones> <modelo sin .bin> <nombre del archivo de resultados>
```


