def media(*args):
    s = 0
    i = 0
    for n in args:
        s += n
        i += 1
    if i == 0:
        return 0
    return s / i

import pytest