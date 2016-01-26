import string
import json
import os
import re

abspath = os.path.abspath(os.path.dirname(__file__))
odmfile = os.path.join(abspath, 'odm_ccd.json')
mapfile = os.path.join(abspath, 'mapillary_ccd.json')


def check_mapi_ccd(odm_key):
    for key in map_ccd:
        return (all(map(lambda x: x in odm_key, re.findall(r"[\w']+", key)))) or \
               (all(map(lambda x: x in key, re.findall(r"[\w']+", odm_key))))


if __name__ == '__main__':
    # Open both files and convert to lowercase
    with open(odmfile, 'rb') as odmf:
        odm_ccd = json.loads(odmf.read())
    odm_ccd = dict(zip(map(string.lower, odm_ccd.keys()), odm_ccd.values()))

    with open(mapfile, 'rb') as mapf:
        map_ccd = json.loads(mapf.read())
    map_ccd = dict(zip(map(string.lower, map_ccd.keys()), map_ccd.values()))

    # Pass through each key in odm_ccd
    # check if it matches with any key in map_ccd
    list_of_trues = list(map(check_mapi_ccd, odm_ccd))

    true_keys = dict(map(None, odm_ccd.keys(), list_of_trues))
    print "These sensor definitions are not found in Mapillary's sensor file:"
    print dict((k, v) for k, v in true_keys.iteritems() if v is True)
