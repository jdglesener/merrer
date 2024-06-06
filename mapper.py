#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys 
  
for line in sys.stdin: 
    line = line.strip() 
    words = line.split() 
    for word in words:
      w = ""
      for c in word:
        if c.upper() in "abcdefghijklmnopqrstuvwxyz":
          w += c.upper()
      print(w)
