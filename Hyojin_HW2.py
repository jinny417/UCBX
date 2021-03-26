# %%
# 1.Include a section with your name<br>
# 2.Create matrix A with size (3,5) containing random numbers<br>
# 3.Find the size and length of matrix A<br>
# 4.Resize (crop/slice) matrix A to size (3,4)<br>
# 5.Find the transpose of matrix A and assign it to B<br>
# 6.Find the minimum value in column 1 of matrix B<br>
# 7.Find the minimum and maximum values for the entire matrix A<br>
# 8.Create vector X (an array) with 4 random numbers<br>
# 9.Create a function and pass vector X and matrix A in it<br>
# 10.In the new function multiply vector X with matrix A and assign the result to D (note:you may get an error! ... think why and fix it. Recall matric manipulation in class!)<br>
# 11.Create a complex number Z with absolute and real parts != 0<br>
# 12.Show its real and imaginary parts as well as it’s absolute value<br>
# 13.Multiply result D with the absolute value of Z and record it to C<br>
# 14.Convert matrix B from a matrix to a string and overwrite B<br>
# 15.Display a text on the screen: ‘Nameis done with HW2‘, but pass your ‘Name’ as a string variable<br>
# 16.Organize your code: use each line from this assignment as a comment line before each step<br>
# 17.Save all steps as a script in a .pyfile<br>
# 18.Email your Githublink to me including your .pyfile + screenshots of your running code before next class. 

# %%
# 1. Include a section with your name
# HYOJIN LEE

# %%
import numpy as np

# %%
# 2.Create matrix A with size (3,5) containing random numbers
A = np.random.rand(3, 5)
print(A)

# %%
# 3.Find the size and length of matrix A
print('size of A: {0}'.format(A.size))
print('shape of A: {0}'.format(A.shape))
print('length of A: {0}'.format(len(A)))

# %%
# 4.Resize (crop/slice) matrix A to size (3,4)
A = np.delete(A, 2, 1)
print('shape of A: {0}'.format(A.shape))
print(A)

# %%
# 5.Find the transpose of matrix A and assign it to B
B = A.T 
print(B)

# %%
# 6.Find the minimum value in column 1 of matrix B
print('The minimum value in column 1 of matrix B is {0}'.format(B[:,1].min()))

# %%
# 7.Find the minimum and maximum values for the entire matrix A
print('The minimum value in matrix A is {0}'.format(A.min()))
print('The maximum value in matrix A is {0}'.format(A.max()))


# %%
# 8.Create vector X (an array) with 4 random numbers
X = np.random.rand(4)
print(X)

# %%
# 9.Create a function and pass vector X and matrix A in it
# 10.In the new function multiply vector X with matrix A and assign the result to D
# (note:you may get an error! ... think why and fix it. Recall matric manipulation in class!)
def new_func(v_X, m_A):

    return np.dot(m_A, v_X)
    # or use transpose
    #D = np.dot(v_X, m_A.T)
    
D = new_func(X, A)
print(D)

# %%
# 11.Create a complex number Z with absolute and real parts != 0
X = np.random.rand(1) + 1j
print(X)

# %%
# 12.Show its real and imaginary parts as well as it’s absolute value
print('The real part of X is {0}'.format(X.real))
print('The imaginary part of X is {0}'.format(X.imag))
print('The absolute value of X is {0}'.format(abs(X)))


# %%
# 13.Multiply result D with the absolute value of Z and record it to C
Z = abs(X)
C = Z * D
print(C)

# %%
# 14.Convert matrix B from a matrix to a string and overwrite B
str_lst = [list(map(str, n)) for n in B]
B = str(str_lst)

print(B)

# %%
# 15.Display a text on the screen: ‘Nameis done with HW2‘, but pass your ‘Name’ as a string variable
name = 'Hyojin '
print('{0}is done with HW2‘'.format(name))

# %%
# 16.Organize your code: use each line from this assignment as a comment line before each step<br>
# 17.Save all steps as a script in a .pyfile<br>
# 18.Email your Githublink to me including your .pyfile + screenshots of your running code before next class.