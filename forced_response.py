import sympy as sym

M, m, g, x1, x2, x3, x4, F, ell = sym.symbols('M, m, g, x1, x2, x3, x4, F, ell')
phi = 4*m*ell*x4**2*sym.sin(x3) + 4*F - 3*m*g*sym.sin(x3)*sym.cos(x3)
phi /= 4*(M+m) - 3*m*sym.cos(x3)**2

d_phi_F = phi.diff(F)
d_phi_x3 = phi.diff(x3)
d_phi_x4 = phi.diff(x4)

d_phi_F_eq = d_phi_F.subs([(F, 0), (x3,0), (x4,0)])
d_phi_x3_eq = d_phi_x3.subs([(F,0),(x3,0),(x4,0)])
d_phi_x4_eq = d_phi_x4.subs([(F,0),(x3,0),(x4,0)])

a = d_phi_F_eq
b = -(d_phi_x3_eq)

c = 3/ell/(4*M+m)
d = 3*(M+m)*g/ell/(4*M+m)

M_val = 0.3
m_val = 0.1
ell_val = 0.35
g_val = 9.81
def substitute(z):
    subs = [(M, M_val), (m, m_val), (ell, ell_val), (g, g_val)]
    return float(z.subs(subs))
a_val = substitute(a)
b_val = substitute(b)
c_val = substitute(c)
d_val = substitute(d)

import control as C
import matplotlib.pyplot as plt
import numpy as np

num_t = [-c_val]
den_t = [1, 0, -d_val]
G_theta  = C.TransferFunction(num_t, den_t)

num_x = [a_val, 0, (-a_val*d_val)+(b_val*c_val)]
den_x = [1, 0, -d_val, 0, 0]
G_x = C.TransferFunction(num_x, den_x)

#forced response
t_span = np.linspace(0,0.2,500)
F_input = np.sin(100*t_span**2)
#for θ(t) vs t
t_out, x3_out = C.forced_response(G_theta, t_span, F_input)
#for x(t) vs t
t_out, x1_out = C.forced_response(G_x, t_span, F_input)
#for θ(t) vs t
plt.plot(t_out, x3_out)
#for x(t) vs t
plt.plot(t_out, x1_out)
plt.xlabel('Time (s)')
#for θ(t) vs t
plt.ylabel('θ(t)')
#for x(t) vs t
plt.ylabel('x(t)')
plt.grid()
plt.show()
