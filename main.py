import numpy as np

print("Computes z^w where z&w are elements of I\n")

psi = complex(0.540302306, 0.841470985)
e = 2.7182818284

print("e = " + str(e) + "\n(-1)^(1/pi) = " + str(psi) + "\n")

re_z = int(input("Re(Z): "))
im_z = int(input("im(z): "))
re_w = int(input("Re(w): "))
im_w = int(input("im(w): "))

z = complex(re_z, im_z)
w = complex(re_w, im_w)

# z^(Re(w))

z_rew = z**re_w

# psi^(Im(w)*ln(|z|))

psi_exp = psi ** (im_w * (np.log(np.sqrt(re_z ** 2 + im_z ** 2))))

# e^arctan(Im(z)/Re(z))

e_exp = e ** (np.arctan(im_z / re_z) * im_w)

# final calculation

res = (z_rew * psi_exp) / e_exp

print("\nResult is: " + str(res))

