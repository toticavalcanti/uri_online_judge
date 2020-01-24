while True:
    ev1, ev2, at, d = [int(x) for x in input().split()]
    if ev1 == ev2 == at == d == 0:
        break
    aux, ev1 = ev1, 0
    while aux > 0:
        aux -= d
        ev1 += 1

    aux, ev2 = ev2, 0
    while aux > 0:
        aux -= d
        ev2 += 1

    if at == 3:
        ev1 = ev1 / (ev1 + ev2)
    else:
        p = (1 - (6 - at)/ 6)
        p = (1 - p) / p
        ev1 = (1 - p ** ev1) / (1 - p ** (ev1 + ev2))

    print('%.1f' % (ev1 * 100))
