#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import datetime

def charParaInt(ch):
  try :
    digit = int(ch)
    if digit > 9 or digit < 0:
      raise Exception(ch)
  except ValueError:
    raise Exception(ch)
  
  return digit

def function1():
  number=[]
  while True:
    try:
      ch=input()
      digit=charParaInt(ch)
    except Exception as inst:
      x = inst.args[0]
      if x == "-" :
        break

      print(x +" is not a valid digit.")
      continue

    number.append(str(digit))

  number.sort(reverse=True)
  print (''.join(number))

class Data:
  def __init__(self, dia, mes, ano):
    try :
        datetime.datetime(int(ano),int(mes),int(dia))
    except ValueError :
        raise Exception("A data está inválida!")
    
    self.dia = dia
    self.mes = mes
    self.ano = ano

# function1()
Data(29,2,2018)
