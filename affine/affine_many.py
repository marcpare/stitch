#
# from the project root:
#
# python affine/affine_many.py books/*
#
#

import argparse as ap
import affine
import correspond
import json

if __name__ == "__main__":
    parser = ap.ArgumentParser()
    parser.add_argument('images', nargs='+')
    parser.add_argument('-a', '--algorithm', 
                      help='feature detection algorithm',
                      choices=['SURF', 'SIFT'],
                      default='SURF')

    args = parser.parse_args()
    
    images = args.images
    algorithm = args.algorithm
    
    translations = []
    image_pairs = zip(images[:-1], images[1:])
    for (fn1, fn2) in image_pairs:
        print fn1 + " " + fn2
        (points1, points2) = correspond.correspond(fn1, fn2)
        
        (S, Tx, Ty, M) = affine.estimate_translation(points1, points2)
        
        translations.append({
            "first": fn1,
            "second": fn2,
            "S": S,
            "Tx": Tx,
            "Ty": Ty,
        })
    
    print json.dumps(translations)