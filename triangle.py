#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    test1 = cmp(a, 0) + cmp(b, 0) + cmp(c, 0)
    test2 = max(a,b,c) < ((a+b+c) - max(a,b,c))
    test3 = set([a,b,c])
    if test1 == 3:
        if test2 == True:
            if len(test3) == 2:
                return "isosceles"
            elif len(test3) == 1:
                return "equilateral"
            elif len(test3) == 3:
                return "scalene"
        else:
            raise StandardError('Your triangle has a innie !')
    else:
        raise StandardError('Your triangle has a outie !')      

# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    try:
        triangle
    except StandardError, ex:
        raise StandardError(ex)
    
