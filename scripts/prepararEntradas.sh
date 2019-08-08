#!/bin/bash
python get_formato_entrada_fasstext.py "../Files Kaggle/snli_1.0_train_filtered.jsonl" "../Files Kaggle/snli_1.0_train_gold_labels.csv" > entradas/trainInputFt.txt
python get_formato_entrada_fasstext.py "../Files Kaggle/snli_1.0_dev_filtered.jsonl" "../Files Kaggle/snli_1.0_dev_gold_labels.csv" > entradas/devInputFt.txt

