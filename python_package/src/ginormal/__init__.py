"""
Density function and generation of random variables from the
generalized inverse normal distribution. Also provides density functions and
generation from the distribution truncated to positive or negative reals.

Functions provided
------------------
dtgin(z, a, m, t, sign=True, log=True, quasi=False)
dgin(z, a, m, t, log=True, quasi=False)
rtgin(size, a, m, t, sign, algo='hormann', verbose=False)
rgin(size, a, m, t, algo='hormann')

Truncated variants include a 't' in the name and require a sign argument for
whether truncation is to the right or left of 0.
"""

from ginormal.dgin import dgin
from ginormal.dtgin import dtgin
from ginormal.rtgin import rtgin
from ginormal.rgin import rgin