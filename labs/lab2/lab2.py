def calc_mean():
    import math
    total_values = eval(input("Enter the values to be entered: "))
    acc = 0
    rms = 0
    hm = 0
    gm = 1
    for _ in range(total_values):
        acc = eval(input("Enter value: "))
        rms = rms + acc ** 2
        hm = hm + (1 / acc)
        gm = gm * acc
    gm = math.pow(gm, 1 / total_values)
    rms = math.sqrt(rms / total_values)
    hm = total_values / hm
    print("RMS =", rms)
    print("Harmonic Mean =", hm)
    print("Geometric Mean =", gm)







