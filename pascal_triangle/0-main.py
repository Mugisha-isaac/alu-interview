#!/usr/bin/python3
"""
Main file for testing
"""
pascalTriangle = __import__("0-pascal_triangle").pascal_triangle

result = pascalTriangle(5)
for row in result:
    print(row)
