#!/usr/bin/python3
import copy

spam=(list('Hello'))

cheese= copy.copy(spam)
cheese[1]=42
print(spam,cheese)
