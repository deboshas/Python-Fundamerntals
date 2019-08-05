# Write
from math import sqrt


def mean(l):
    return float(sum(l))/len(l)


def var(l):
    m = mean(l)
    return sum([(x-m)**2 for x in l])/len(l)


def factor(l):
    return 1.96


def conf(l):
    interval = [mean(l)-(factor(l) * sqrt(var(l)/len(l))),
                mean(l)+(factor(l) * sqrt(var(l)/len(l)))]
    return interval


def test(samples, hypothesis):
    interval = conf(samples)
    if interval[0] <= ((float)hypothesis) <= interval[1]:
        print("Hypothesis is correct")
    else:
        print("Hypothesis is wrong")


samples = [199, 200, 201, 202, 203, 204]
hypothesis = 200


test(samples, hypothesis)
