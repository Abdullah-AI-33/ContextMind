import numpy as np
#v= np.array([3,2])

#def magnitude(v):
#    return np.sqrt(v[0]**2 +v[1]**2)
#print(magnitude(v))

"""v_d = int(input('write the dimentions '))

values = []

for i in range(v_d):
    g = int(input("write you'r vector's values"))
    values.append(g)
    
print(values)

v1 = np.array(values)

v_s = 0

for g in range(v_d):
    v_s += v1[g]**2 

def mag(v1):
    return np.sqrt(v_s)

print(mag(v1))"""
"""v = np.array([3,4])
s = np.array([5,1])

magnitude_of_v = np.linalg.norm(v)
magnitude_of_s = np.linalg.norm(s)
the_scalar_projection = np.matmul(v,s) / magnitude_of_v
print(the_scalar_projection)
the_angel  = np.arccos(np.matmul(v,s) /( magnitude_of_v * magnitude_of_s))
the_vector_projection = (the_scalar_projection * v )/ magnitude_of_v

print(the_vector_projection)"""
r = np.array([3,4])
b1 = np.array([2,1])
b2 = np.array([-2,4])
verify = np.dot(b1,b2) 
if verify == 0 :
    print('the basis are orthagonal')
else :
    print('the basis are not orthagonal')

projection_of_r_on_b1 = np.dot(r,b1)/np.dot(b1,b1)
print(projection_of_r_on_b1)
projection_of_r_on_b2 = np.dot(r,b2)/np.dot(b2,b2)
print(projection_of_r_on_b2)

r_b = [projection_of_r_on_b1 , projection_of_r_on_b2]
print(r_b)

verify_v = projection_of_r_on_b1 * b1
print(verify_v)
verify_v2 = projection_of_r_on_b2 * b2
print(verify_v2)
v_verify = verify_v + verify_v2
print(v_verify)
