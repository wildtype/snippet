#!/usr/bin/env python
q='''#!/usr/bin/env python
q=%
sq=chr(39)
p=chr(37)
s=''
for i in range(len(q)):
	if q[i]!=p:
		s+=q[i]
	else:
		s+=sq+sq+sq+q+sq+sq+sq
print(s)'''
sq=chr(39)
p=chr(37)
s=''
for i in range(len(q)):
	if q[i]!=p:
		s+q[i]
	else:
		s+=sq+sq+sq+q+sq+sq+sq
print(s)
