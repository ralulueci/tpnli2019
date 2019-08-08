#!/bin/bash
pathOraciones=$1
pathModelo=$2
pathResultados=$3
python ejecutar_modelo.py "$pathOraciones" "$pathModelo" > "$pathResultados"