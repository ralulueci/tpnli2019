#!/usr/bin/env python
import argparse
import json
import csv
import fasttext

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('sentences')
    ap.add_argument('labels', nargs='?')

    args = ap.parse_args()

    sentence_data = open(args.sentences, 'r')
    if args.labels:
        label_data = open(args.labels, 'r')
        for sentence, label in zip(it_sentences(sentence_data), it_labels(label_data)):
            # Tenemos la oración en sentence con su categoría en label
            print("__label__"+label,",", sentence)
            pass
    else:

        model = fasttext.load_model("model_filename.bin")
        for sentence in it_sentences(sentence_data):
            # Tenemos una oración en sentence

            print(model.predict(sentence)[0][0]) ##.replace("__label__","",1)

            pass
    

def it_sentences(sentence_data):
    for line in sentence_data:
        example = json.loads(line)
        yield example['sentence2']

def it_labels(label_data):
    label_data_reader = csv.DictReader(label_data)
    for example in label_data_reader:
        yield example['gold_label']

main()
