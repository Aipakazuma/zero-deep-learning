# -*- cording: utf-8 -*-

import numpy as np


def AND(x1, x2):
  '''
  パーセプトロン
  x -> 入力
  w -> 重み
  theta -> 閾値

  入力２つに重みを掛けた和が閾値を超えたら1、そうでなければ0
  '''
  w1, w2, theta = 0.5, 0.5, 0.7
  tmp = x1 * w1 + x2 * w2
  if tmp <= theta:
    return 0
  elif tmp > theta:
    return 1


def AND_b(x1, x2):
  '''
  重みとバイアス方式
  バイアスは発火のしやすさ
  bが-0.1であれば、和が0.1を上回れば良い
  bが-20.0であれば、和は20.0を上回らなければいけない
  バイアスの値によって、発火のしやすさが決まる

  またバイアスは「ゲタはき」という意味がある。
  入力が何もないときに、出力にどれだけゲタを履かせるかということを意味するらしい。
  '''
  x = np.array([x1, x2]) # 入力
  w = np.array([0.5, 0.5]) # 重み
  b = -0.7 # バイアス
  tmp = np.sum(w * x) + b
  if tmp <= 0:
    return 0
  else:
    return 1


def NAND(x1, x2):
  '''
  NAND gate (not and)
  '''
  x = np.array([x1, x2])
  w = np.array([-0.5, -0.5]) # 重みがANDと違う
  b = 0.7 # バイアスも違う
  tmp = np.sum(w * x) + b
  if tmp <= 0:
    return 0
  else:
    return 1


def OR(x1, x2):
  '''
  OR gate
  '''
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.2 # バイアスがANDと違う
  tmp = np.sum(w * x) + b
  if tmp <= 0:
    return 0
  else:
    return 1


def XOR(x1, x2):
    '''
    XOR gate
    '''
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    return AND(s1, s2)


if __name__ == '__main__':
  # print(AND(0, 0))
  # print(AND(1, 0))
  # print(AND(0, 1))
  # print(AND(1, 1))
  # print(AND_b(0, 1))
  # print(AND_b(0, 0))
  # print(NAND(0, 1))
  print(OR(1, 1))
