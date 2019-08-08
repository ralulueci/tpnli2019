#!/usr/bin/env python
import argparse
import json
import csv
import fasttext

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('sentences')
    ap.add_argument('model', nargs='?')

    args = ap.parse_args()

    sentence_data = open(args.sentences, 'r')
    model = fasttext.load_model(args.model+".bin")
    for sentence in it_sentences(sentence_data):
        # Tenemos una oración en sentence
        print(model.predict(sentence)[0][0]) ##.replace("__label__","",1)
        pass

def it_sentences(sentence_data):
    for line in sentence_data:
        example = json.loads(line)
        yield example['sentence2']

main()
