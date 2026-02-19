def is_isomorphic(s: str, t: str) -> bool:
    """Проверяет, являются ли строки s и t изоморфными"""
    if len(s) != len(t):
        return False
    # Словари для отслеживания соответствий s -> t и t -> s
    map_st = {}
    map_ts = {}
    for cs, ct in zip(s, t):
        # Проверка прямого отображения
        if cs in map_st:
            if map_st[cs] != ct:
                return False
        else:
            map_st[cs] = ct
        # Проверка обратного отображения (гарантия уникальности)
        if ct in map_ts:
            if map_ts[ct] != cs:
                return False
        else:
            map_ts[ct] = cs
    return True

s = 'paper'
t = 'title'
print(is_isomorphic(s, t))