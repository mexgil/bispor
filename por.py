from math import cos, sin, acos, sqrt

alpha = 1.0472
beta = 0
AE = 10
AD = 15
AC = 15

Cx = AC*cos(alpha+beta)
Cy = AC*sin(alpha+beta)
Dx = AD*cos(alpha)
Dy = AD*sin(alpha)
Ex = AE
Ey = 0

beta = 0
BM = 10
BL = 15
BN = 15

Lx = BL*cos(alpha+beta)
Ly = BL*sin(alpha+beta)
Mx = BM*cos(alpha)
My = BM*sin(alpha)
Nx = BN
Ny = 0

ML = sqrt((Lx - Mx)**2 + (Ly-My)**2)
MN = sqrt((Nx - Mx)**2 + (Ny-My)**2)
NL = sqrt((Nx - Lx)**2 + (Ny-Ly)**2)
a_NML = acos((MN**2+NL**2-ML**2)/(2*MN*NL))

a_LMx = 0
My = 0
Mx = 0
Lx = ML*cos(a_LMx)
Ly = ML*sin(a_LMx)
Nx = MN*cos(a_NML+a_LMx)
Ny = MN*sin(a_NML+a_LMx)

dist = sqrt((Ex-Mx)**2+(Ey-My)**2)+sqrt((Dx-Lx)**2+(Dy-Ly)**2) + sqrt((Cx-Nx)**2+(Cy-Ny)**2)

def calc_n_dist(rot_angl, step_x, step_y):
    n_a_LMx = 0+rot_angl
    n_Mx = 0+step_x
    n_My = 0+step_y
    n_Lx = ML*cos(n_a_LMx)+step_x
    n_Ly = ML*sin(n_a_LMx)+step_y
    n_Nx = MN*cos(a_NML+n_a_LMx)+step_x
    n_Ny = MN*sin(a_NML+n_a_LMx)+step_y
    return sqrt((Ex-n_Mx)**2+(Ey-n_My)**2)+sqrt((Dx-n_Lx)**2+(Dy-n_Ly)**2) + sqrt((Cx-n_Nx)**2+(Cy-n_Ny)**2)

def fun1(x):
    return calc_n_dist(*x)
