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
    subsitutions = [(M, M_val), (m, m_val), (ell, ell_val), (g, g_val)]
    return float(z.subs(subsitutions))

a_val = substitute(a)
b_val = substitute(b)
c_val = substitute(c)
d_val = substitute(d)
#--------------------------
import control as C
import matplotlib.pyplot as plt
import numpy as np

num = [-c_val]
den = [1, 0, -d_val]
G_theta  = C.TransferFunction(num, den)

Kp = 100
Ki = 0.1
Kd = 10

G_c = -C.TransferFunction([Kd, Kp, Ki], [1, 0])
G_d = C.feedback(G_theta, G_c)
t_span = np.linspace(0,1,500)
t_imp, x3_imp = C.impulse_response(G_d, t_span)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.plot(t_imp, x3_imp*180/np.pi)
plt.ylabel('Angle θ (degrees)')
plt.xlabel('Time(s)')
minor_ticks = np.arange(-5, 0, 0.1)
ax.set_yticks(minor_ticks, minor=True)
plt.grid()
plt.show()
