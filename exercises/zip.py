def zip(key: list[str], value: list[int]):
    key_dict: dict[str, int] = {}
    idx: int = 0

    if (len(key) != len(value) or key == False or value == False):
        return key_dict

    for k in key:
            key_dict[k] = value[idx]
            idx += 1

    return key_dict