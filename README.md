# complex_exponentiation
Compute complex exponents (z to the power of w where both z and w are complex numbers) using Euler's Formula's extension on the complex plane.

The extensions were found by me, personally. <del>Depends on NumPY though. Will try and make it less dependant</del>. LaTeX code of my equation can be found here:

<code>z^w=\frac{z^{Re(w)}\psi^{Im(w)\ln (\left | z \right |)}}{e^{\arctan( \frac{Im(w)}{Re(w)})Im(w)}}</code>

and LaTeX form:

<a href="https://www.codecogs.com/eqnedit.php?latex=z^w&space;=&space;\frac{z^{Re(w)}\psi^{Im(w)\ln&space;(\left&space;|&space;z&space;\right&space;|)}}{e^{\arctan(&space;\frac{Im(w)}{Re(w)})Im(w)}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?z^w&space;=&space;\frac{z^{Re(w)}\psi^{Im(w)\ln&space;(\left&space;|&space;z&space;\right&space;|)}}{e^{\arctan(&space;\frac{Im(w)}{Re(w)})Im(w)}}" title="z^w = \frac{z^{Re(w)}\psi^{Im(w)\ln (\left | z \right |)}}{e^{\arctan( \frac{Im(w)}{Re(w)})Im(w)}}" /></a>

where Re() function returns the real part and the Im() function returns the imaginary part of the complex number.

<blockquote> ln(|z|) </blockquote> 

denotes natural logarithm of the length of the complex number "z" on the complex plane. Which equates to: 

<a href="https://www.codecogs.com/eqnedit.php?latex=\left&space;|&space;z&space;\right&space;|&space;=&space;\sqrt&space;{Re(z)^2&space;&plus;&space;Im(z)^2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\left&space;|&space;z&space;\right&space;|&space;=&space;\sqrt&space;{Re(z)^2&space;&plus;&space;Im(z)^2}" title="\left | z \right | = \sqrt {Re(z)^2 + Im(z)^2}" /></a>

and also,

<a href="https://www.codecogs.com/eqnedit.php?latex=\psi&space;=&space;(-1)^{\frac{1}{\pi&space;}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\psi&space;=&space;(-1)^{\frac{1}{\pi&space;}}" title="\psi = (-1)^{\frac{1}{\pi }}" /></a>

Psi was given its own symbol because it is used a lot during the proof of the extension and pops up a lot in side extensions as well. Also it helps get rid of exponent of exponents in LaTeX form.

Although less obvious, 

<a href="https://www.codecogs.com/eqnedit.php?latex=\arctan(\frac{Im(w)}{Re(w)})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\arctan(\frac{Im(w)}{Re(w)})" title="\arctan(\frac{Im(w)}{Re(w)})" /></a>

simply denotes the angle between the real axis and the complex vector, which is called the arguement of the complex number.

A simpler notation would use R_ and I_ to denote Im() and Re() functions. Also, we can use theta for the arguement of w. The new and simpler equation looks like:

<a href="https://www.codecogs.com/eqnedit.php?latex=z^w&space;=&space;z^{R_{w}}&space;\left&space;(&space;\frac{\psi&space;^{ln\left&space;|&space;z&space;\right&space;|}}{e^{\theta_{w}}}\right&space;)^{I_{w}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?z^w&space;=&space;z^{R_{w}}&space;\left&space;(&space;\frac{\psi&space;^{ln\left&space;|&space;z&space;\right&space;|}}{e^{\theta_{w}}}\right&space;)^{I_{w}}" title="z^w = z^{R_{w}} \left ( \frac{\psi ^{ln\left | z \right |}}{e^{\theta_{w}}}\right )^{I_{w}}" /></a>

for which the LaTeX code is:

<code> z^w=z^{R_{w}} \left ( \frac{\psi ^{ln\left | z \right |}}{e^{\theta_{w}}}\right )^{I_{w}} </code>

