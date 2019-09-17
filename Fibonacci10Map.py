#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fibonacci(i):
	if i==0: return 0
	if i==1: return 1
	return fibonacci(i-1)+fibonacci(i-2)

if __name__ == "__main__":
	print map(fibonacci, range(10))