# coding=utf-8

from src.tk import TK
import argparse

parser = argparse.ArgumentParser()
parser.register('type', 'bool', (lambda x: x.lower() in ('True', "yes", "true", "t", "1")))
parser.add_argument('--mode', default='main', help='')
args = parser.parse_args()

if args.mode == 'main':
    window = TK()
    window.start()
elif args.mode == 'N_0_1':
    from src.N_0_1 import KO
    ko = KO()
    ko.solve()
elif args.mode == 'place':
    from src.place import KO
    ko = KO()
    ko.solve()
else:
    pass
