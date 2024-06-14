h=float(input('input the height of the 1st ball:'))
m1=float(input('input the mass of the 1st ball:'))
m2=float(input('input the mass of the 2nd ball:'))
u1=(2*9.8*h)**0.5
v1=(m1-m2)*u1/(m1+m2)
v2=2*m1*u1/(m1+m2)
print('The velocity of the 1st ball after slide=',u1)
print('The velocity of the 2nd ball after collision=',v2)