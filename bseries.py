###############################################################################
#
# Wageningin B-Series Propeller
#
# Thrust and torque curves for the Wageningen B-series propellers
# https://deepblue.lib.umich.edu/bitstream/handle/2027.42/91702/Publication_No_237.pdf?sequence=1&isAllowed=y
#
###############################################################################
#
# INPUTS:
#
# J: propeller advance ratio = v/nD
# P/D: pitch to diameter ratio
# Ar: blade area ratio = Ae/Ao
# Z: number of blades
#
# INPUT LIMITS:
#
# J > 0
# 0.5 < P/D < 1.4
# 0.3 < Ae/Ao < 1.05
# 2 < Z < 7
#
# OUTPUTS
# 
# KT: nondimensional thrust coefficient
# KQ: nondimensional torque coefficient
#
# DESCRIPTION:
#
# The Wageningen B-series propeller is used as a conceptual design model
# in marine engineering. It requires the number of blades, the blade area
# ratio (blade projected area, divided by total disk area), and the pitch-
# to-diameter ratio to be specified. Typically, curves are generated for
# a range of advance ratios ranging from 0 to the point at which either
# the thrust or torque coefficient become zero or negative.
#
# These functions are constructed to be used generally, either for plotting,
# analysis, or design optimization.
#
###############################################################################

def KT(J, PD, Ar, Z):

    CT = [8.80496E-03, -2.04554E-01, 1.66351E-01, 1.58114E-01, -1.47581E-01,
        -4.81497E-01, 4.15437E-01, 1.44043E-02, -5.30054E-02, 1.43481E-02,
        6.06826E-02, -1.25894E-02, 1.09689E-02, -1.33698E-01, 6.38407E-03,
        -1.32718E-03, 1.68496E-01, -5.07214E-02, 8.54559E-02, -5.04475E-02,
        1.04650E-02, -6.48272E-03, -8.41728E-03, 1.68424E-02, -1.02296E-03,
        -3.17791E-02, 1.86040E-02, -4.10798E-03, -6.06848E-04, -4.98190E-03,
        2.59830E-03, -5.60528E-04, -1.63652E-03, -3.28787E-04, 1.16502E-04,
        6.90904E-04, 4.21749E-03, 5.65229E-05, -1.46564E-03]

    s = [0, 1, 0, 0, 2,
        1, 0, 0, 2, 0,
        1, 0, 1, 0, 0,
        2, 3, 0, 2, 3,
        1, 2, 0, 1, 3,
        0, 1, 0, 0, 1,
        2, 3, 1, 1, 2,
        0, 0, 3, 0]

    t = [0, 0, 1, 2, 0,
        1, 2, 0, 0, 1,
        1, 0, 0, 3, 6,
        6, 0, 0, 0, 0,
        6, 6, 3, 3, 3,
        3, 0, 2, 0, 0,
        0, 0, 2, 6, 6,
        0, 3, 6, 3]

    u = [0, 0, 0, 0, 1,
        1, 1, 0, 0, 0,
        0, 1, 1, 0, 0,
        0, 1, 2, 2, 2,
        2, 2, 0, 0, 0,
        1, 2, 2, 0, 0,
        0, 0, 0, 0, 0,
        1, 1, 1, 2]

    v = [0, 0, 0, 0, 0,
        0, 0, 1, 1, 1,
        1, 1, 1, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 1, 1, 1,
        1, 1, 1, 2, 2,
        2, 2, 2, 2, 2,
        2, 2, 2, 2]

    res = 0
    for i in range(len(CT)):
        res += CT[i] * J**s[i] * PD**t[i] * Ar**u[i] * Z**v[i]

    return res

def KQ(J, PD, Ar, Z):

    CQ = [3.79368E-03, 8.86523E-03, -3.22410E-02, 3.44778E-03, -4.08811E-02,
        -1.08009E-01, -8.85381E-02, 1.88561E-01, -3.70871E-03, 5.13696E-03,
        2.09449E-02, 4.74319E-03, -7.23408E-03, 4.38388E-03, -2.69403E-02,
        5.58082E-02, 1.61886E-02, 3.18086E-03, 1.58960E-02, 4.71729E-02,
        1.96283E-02, -5.02782E-02, -3.00550E-02, 4.17122E-02, -3.97722E-02,
        -3.50024E-03, -1.06854E-02, 1.10903E-03, -3.13912E-04, 3.59850E-03,
        -1.42121E-03, -3.83637E-03, 1.26803E-02, -3.18278E-03, 3.34268E-03,
        -1.83491E-03, 1.12451E-04, -2.97228E-05, 2.69551E-04, 8.32650E-04,
        1.55334E-03, 3.02683E-04, -1.84300E-04, -4.25399E-04, 8.69243E-05,
        -4.65900E-04, 5.54194E-05]

    s = [0, 2, 1, 0, 0,
        1, 2, 0, 1, 0,
        1, 2, 2, 1, 0,
        3, 0, 1, 0, 1,
        3, 0, 3, 2, 0,
        0, 3, 3, 0, 3,
        0, 1, 0, 2, 0,
        1, 3, 3, 1, 2,
        0, 0, 0, 0, 3,
        0, 1]

    t = [0, 0, 1, 2, 1,
        1, 1, 2, 0, 1,
        1, 1, 0, 1, 2,
        0, 3, 3, 0, 0,
        0, 1, 1, 2, 3,
        6, 0, 3, 6, 0,
        6, 0, 2, 3, 6,
        1, 2, 6, 0, 0,
        2, 6, 0, 3, 3,
        6, 6]

    u = [0, 0, 0, 0, 1,
        1, 1, 1, 0, 0,
        0, 0, 1, 1, 1,
        1, 1, 1, 2, 2,
        2, 2, 2, 2, 2,
        2, 0, 0, 0, 1,
        1, 2, 2, 2, 2,
        0, 0, 0, 1, 1,
        1, 1, 2, 2, 2,
        2, 2]

    v = [0, 0, 0, 0, 0,
        0, 0, 0, 1, 1,
        1, 1, 1, 1, 1,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 1, 1, 1, 1,
        1, 1, 1, 1, 1,
        2, 2, 2, 2, 2,
        2, 2, 2, 2, 2,
        2, 2]

    res = 0
    for i in range(len(CQ)):
        res += CQ[i] * J**s[i] * PD**t[i] * Ar**u[i] * Z**v[i]

    return res