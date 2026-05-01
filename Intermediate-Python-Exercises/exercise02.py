def exercise2(dict_a: dict[str,int], dict_b: dict[str,int]) -> dict[str,int]:
    return {k: dict_a.get(k, 0) + dict_b.get(k, 0) \
            for k in set(dict_a) | set(dict_b)}
    #for k,v in dict_b.items():
    #    dict_a[k] = dict_a.get(k, 0) + v
    #else:
    #    return dict_a
if __name__ == "__main__":
    print(exercise2({'a': 10, 'b': 20},{'b': 5, 'c': 15}))
