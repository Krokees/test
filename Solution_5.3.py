"""
Solution_5.3.py

Author:  Spiro Karantzalis(spiro@nyu.edu)
Last revised: 2/18/2024 16:01 hrs

    A sorting helper function that helps sorted() to
    sort a list of dicts by each dict's mean_temp:
    opening and loading the file weny_lod_tiny.json,
    please sort the dicts in this list by the mean_temp
    value. Loop through and print each dict.

Notes:  I hard-coded the key in the function, using the same assumption
        from Solution_5.2.py.

        I also experimented with a lambda, and it produced the correct
        results. Would that have also been an acceptable solution?

"""
import json

def by_mean_temp(arg):
    return(int(arg['mean_temp']))

fh = open('../weny_lod_tiny.json')
lod = json.load(fh)

sorted_dicts = sorted(lod, key = by_mean_temp)

for idict in sorted_dicts:
    print(idict)