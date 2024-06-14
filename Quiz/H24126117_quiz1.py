Richter_scale=float(input('Please input a Richter scale value: '))
print('Richter scale value:',Richter_scale)
Equivalence=10**(1.5*Richter_scale+4.8)
TNT=Equivalence/(4.184*(10**9))
nutritious_lunch=Equivalence/2930200
print('Equivalence in Joules:',Equivalence)
print('Equivalence in tons of TNT:',TNT)
print('Equivalence in number of nutritious lunches:',nutritious_lunch)
