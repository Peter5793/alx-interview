#!/usr/bin/python3
""" Print Pascal triangle """


def pascal_triangle(n):
  """ print triangel"""
  list_1 = []
  if n > 0:
    for i in range(1, n + 1):
      list_2 = []
      last_num = 1
      for j in range(1, i + 1):
        list_2.append(last_num)
        """ place binomial coeffiecient"""
        last_num = last_num * (i - j ) // j
      list_1.append(list_2)
  return list_1