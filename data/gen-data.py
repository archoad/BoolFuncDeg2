#! /usr/bin/env python
# -*- coding: utf-8 -*-

#source:	http://mathworld.wolfram.com/BooleanFunction.html
#			http://www.codecademy.com/fr/courses/python-intermediate-en-KE1UJ/0/1

maxIter = 24

def booleanFunction():
	f0 = open('bool_f0.dat', 'w')
	f1 = open('bool_f1.dat', 'w')
	f2 = open('bool_f2.dat', 'w')
	f3 = open('bool_f3.dat', 'w')
	f4 = open('bool_f4.dat', 'w')
	f5 = open('bool_f5.dat', 'w')
	f6 = open('bool_f6.dat', 'w')
	f7 = open('bool_f7.dat', 'w')
	f8 = open('bool_f8.dat', 'w')
	f9 = open('bool_f9.dat', 'w')
	f10 = open('bool_f10.dat', 'w')
	f11 = open('bool_f11.dat', 'w')
	f12 = open('bool_f12.dat', 'w')
	f13 = open('bool_f13.dat', 'w')
	f14 = open('bool_f14.dat', 'w')
	f15 = open('bool_f15.dat', 'w')
	for x in xrange(maxIter):
		for y in xrange(maxIter):
			# F0 false
			f0.write("%f %f %f\n" % ( x, y, 0 ))

			#F1 a and b
			f1.write("%f %f %f\n" % ( x, y, x&y ))

			#F2 a and not b
			f2.write("%f %f %f\n" % ( x, y, x&(~y) ))

			# F3 a
			f3.write("%f %f %f\n" % ( x, y, x ))

			# F4 not a and b
			f4.write("%f %f %f\n" % ( x, y, (~x) & y ))

			# F5 b
			f5.write("%f %f %f\n" % ( x, y, y ))

			# F6 a xor b
			f6.write("%f %f %f\n" % ( x, y, x^y ))

			# F7 a or b
			f7.write("%f %f %f\n" % ( x, y, x|y ))

			# F8 a nor b
			f8.write("%f %f %f\n" % ( x, y, ~(x|y) ))

			# F9 a xnor b
			f9.write("%f %f %f\n" % ( x, y, ~(x^y) ))

			# F10 not b
			f10.write("%f %f %f\n" % ( x, y, ~y ))

			# F11 a or not b
			f11.write("%f %f %f\n" % ( x, y, x|(~y) ))

			# F12 not a
			f12.write("%f %f %f\n" % ( x, y, ~x ))

			# F13 not a or b
			f13.write("%f %f %f\n" % ( x, y, (~x)|y ))

			# F14 a nand b
			f14.write("%f %f %f\n" % ( x, y, ~(x&y) ))

			# F15 true
			f15.write("%f %f %f\n" % ( x, y, 1 ))
	f0.close()
	f1.close()
	f2.close()
	f3.close()
	f4.close()
	f5.close()
	f6.close()
	f7.close()
	f8.close()
	f9.close()
	f10.close()
	f11.close()
	f12.close()
	f13.close()
	f14.close()
	f15.close()
if __name__ == '__main__':
	booleanFunction()






