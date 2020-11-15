#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 11:20:13 2020

@author: alex
"""
from multiprocessing import Process

num_pasos = 10000000
def  calcula_pi(num_pasos):
    pi=0.0
    paso = 1.0 /num_pasos
    x=0
    sum = 0.0
    for i in range(num_pasos):
        x = (i + 0.5) * paso
        sum = sum + 4.0 / (1.0 + x * x)
    pi = paso*sum
    print("El valor de pi es ", pi)


if __name__ == '__main__':
    p = Process(target=calcula_pi, args=(num_pasos,))
    p.start()
    p.join()


