#!/usr/bin/env python3

def main():

  a, b = input().split()

  listc = []
  for char in a: # cycles through the characters and creates a list that contains the characters found in both words
      if char in b:
          listc.append(char)

  char_index = b.rindex(listc[len(listc) - 1]) # storing the index of the last matching char in b
  hori_print = a.rindex(listc[len(listc) - 1]) # storing which line the horizontal word needs to be printed on

  for i in range(len(a)):
    if i != hori_print:
      print("." * char_index + a[i] + "." * (len(b) - char_index - 1)) # prints the vertical word, one character at a time
    elif i == hori_print: # prints the horizontal word on the desired line
      print(b)

if __name__ == "__main__":
    main()
