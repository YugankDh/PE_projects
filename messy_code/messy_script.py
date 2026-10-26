# Messy student grade calculation script (Original unrefactored version)
import os, sys, math, random

s1 = [85, 92, 78, 64, 89]
s2 = [70, 75, 80, 85, 90]
s3 = [55, 60, 58, 62, 65]

def f(x):
    t = 0
    for i in range(len(x)):
        t = t + x[i]
    a = t / len(x)
    return a

a1 = f(s1)
a2 = f(s2)
a3 = f(s3)

# repeated calculation and string concatenation
all_s = s1 + s2 + s3
tot = 0
for k in range(len(all_s)):
    tot = tot + all_s[k]
ovr_avg = tot / 15

print("Student 1 Avg: " + str(round(a1, 2)) + " / 100")
print("Student 2 Avg: " + str(round(a2, 2)) + " / 100")
print("Student 3 Avg: " + str(round(a3, 2)) + " / 100")
print("Overall Batch Avg: " + str(round(ovr_avg, 2)) + " / 100")
