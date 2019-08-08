#!/usr/bin/env python
import argparse
import fasttext
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('input')
    ap.add_argument('nameModel', nargs='?')
    args = ap.parse_args()
    model = fasttext.train_supervised(input=args.input, epoch=7, lr=0.01, 
    wordNgrams=3, verbose=20, minCount=3,loss="softmax")
    model.save_model(args.nameModel)
main()