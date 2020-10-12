import matplotlib.pyplot as plt
import numpy as np

import bseries as bs

Ar = 1.05
Z = 7

fig, ax = plt.subplots()
J = np.arange(0, 1.4, 0.001)
# initialize the legend list and add entries as necessery
lgnd = []

for PD in np.arange(0.5, 1.5, 0.1):

    KT = np.array([])
    KQ = np.array([])
    eta = np.array([])

    for i in range(len(J)):
        KT_tmp = bs.KT(J[i],PD,Ar,Z)
        KQ_tmp = bs.KQ(J[i],PD,Ar,Z)

        if KT_tmp >= 0:
            KT = np.append(KT,KT_tmp)
            eta = np.append(eta,KT_tmp*J[i]/(2*np.pi*KQ_tmp))
        if KQ_tmp >= 0:
            KQ = np.append(KQ,KQ_tmp)
            

    ax.plot(J[0:len(KT)],KT)
    #ax.plot(J[0:len(KQ)],KQ)
    #ax.plot(J[0:len(eta)],eta)

    lgnd.append('P/D = ' + str(np.ceil(10*PD)/10))


ax.legend(lgnd)
ax.set_ylim(0,0.8)
ax.set_xlim(0,1.4)
plt.show()