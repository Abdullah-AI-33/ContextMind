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
v = np.array([3,4])
s = np.array([5,1])

magnitude_of_v = np.linalg.norm(v)
magnitude_of_s = np.linalg.norm(s)
the_scalar_projection = np.matmul(v,s) / magnitude_of_v
print(the_scalar_projection)
the_angel  = np.arccos(np.matmul(v,s) /( magnitude_of_v * magnitude_of_s))
the_vector_projection = (the_scalar_projection * v )/ magnitude_of_v

print(the_vector_projection)
