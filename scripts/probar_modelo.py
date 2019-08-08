import argparse
import fasttext

def print_results(file,N, p, r):
    print("archivo:" + file,"\tcant_oraciones\t" + str(N), "Precision@{}\t{:.3f}".format(1, p), "Intentos@{}\t{:.3f}".format(1, r))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('input', nargs='?')
    ap.add_argument('model', nargs='?')
    args = ap.parse_args()
    model = fasttext.load_model(args.model)
    print_results(args.input,*model.test(args.input))

main()


