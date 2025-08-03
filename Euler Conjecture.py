for a in range(1, 150):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                for e in range(d, 151):
                    if e ** 5 > a ** 5 + b ** 5 + c ** 5 + d ** 5:
                        break
                    if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                        print(a, b, c, d, e, "=", a+b+c+d+e)