import math

print("Computes z^w where z&w are elements of I\n")

psi = complex(0.540302306, 0.841470985)
e = 2.7182818284

print("e = " + str(e) + "\n(-1)^(1/pi) = e^i = cos(1 rad) + i.sin(1 rad) = " + str(psi) + "\n")

re_z = float(input("Re(Z): "))
im_z = float(input("im(z): "))
re_w = float(input("Re(w): "))
im_w = float(input("im(w): "))

z = complex(re_z, im_z)
w = complex(re_w, im_w)

# z^(Re(w))

z_rew = z**re_w

# psi^(Im(w)*ln(|z|))

psi_exp = psi ** (im_w * (math.log(math.sqrt(re_z ** 2 + im_z ** 2))))

# e^arctan(Im(z)/Re(z))

e_exp = e ** (math.atan(im_z / re_z) * im_w)

# final calculation

res = (z_rew * psi_exp) / e_exp

im_res = res.imag
re_res = res.real

if im_res < 0.0:
    print("\nResult is: " + str(re_res) + " - " + str(im_res * -1) + "i")
else:
    print("\nResult is: " + str(re_res) + " + " + str(im_res) + "i")

