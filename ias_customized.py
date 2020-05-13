# Standard Library
import re


def preprocess_old(inputs, *args):
    def create_new_segs(seg):
        return re.split("\.", seg)

    output = {}

    new_segs = []

    for seg in inputs['seg']:
        new_segs.extend(create_new_segs(seg))

    output['seg'] = new_segs
    output['n_seg'] = len(new_segs)
    print(inputs)
    print(output)
    return output


def preprocess(inputs, *args):

    output = {}

    new_segs = []

    for seg in inputs['seg']:
        new_segs.append(seg.replace('\\n', ' . '))

    output['seg'] = new_segs
    output['n_seg'] = len(new_segs)
    print(inputs)
    print(output)
    return output


def preprocess_minimal(inputs, *args):
    print(inputs)
    return inputs


def tokenize(inputs, *args):
    print(inputs)
    return inputs
