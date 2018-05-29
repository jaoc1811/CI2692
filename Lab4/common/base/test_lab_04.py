#  Lab-01. Busqueda lineal y binaria. Ordenamiento por insercion. Experimentos. Analisis de resultados.

import sys
import time
import basic

def test_search(name, sizes, data, runs_per_each_size, func, verifier, sort):
    for size in sizes:
        sub_data = basic.sample_with_replacement_from_list(data, size)
        sub_sub_data = basic.sample_with_replacement_from_list(sub_data, max(1, size / 2))
        if sort: sub_sub_data.sort()
        for i in range(runs_per_each_size):
            x = sub_data[basic.lrand(0, size)] # there is 1/2 probability x is in sample
            start_time = time.clock()
            result = func(sub_sub_data, x)
            elapsed_time = time.clock() - start_time
            verification = verifier(sub_sub_data, x, result)
            print("search,%s,%d,%d,%f,%d" % (name, size, i, elapsed_time, int(verification)))
            sys.stdout.flush()


def test_sort_by_key(name, sizes, fractions, data, keys, runs_per_each_size_and_fraction, func, verifier):
    for size in sizes:
        j = 0
        for f in fractions:
            (sub_sub_data, sub_sub_keys) = basic.sample_with_replacement_from_lists(data, keys, max(1, int(size * f)))
            for i in range(runs_per_each_size_and_fraction):
                (sub_data, sub_keys) = basic.sample_with_replacement_from_lists(sub_sub_data, sub_sub_keys, size)
                sub_data_copy = list(sub_data)
                sub_keys_copy = list(sub_keys)
                start_time = time.clock()
                func(sub_data_copy, sub_keys_copy)
                elapsed_time = time.clock() - start_time
                verification = verifier(sub_keys, sub_keys_copy)
                #TO DO: Verify that each member in sub_keys_copy still maps to the right element in sub_data_copy
                print("sorting,%s,%d,%d,%f,%d" % (name, size, j * runs_per_each_size_and_fraction + i, elapsed_time, int(verification)))
                sys.stdout.flush()
            j = j + 1

