n1 = input('Digite uma sequência de (),{},[] e descubra se é verdadeira:')
c_f= n1.count('[')
c_a= n1.count(']')

p_a= n1.count('()')
p_f= n1.count(')')

co_a= n1.count('{')
co_f= n1.count('}')

if c_f==c_a and p_a==p_f and co_a==co_f:print('1')
else:print('0')