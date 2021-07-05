#!/usr/bin/env python3

# To run script install libraries using command:
# pip install pyabf

import numpy as np
import matplotlib.pyplot as plt
import pyabf
import pyabf.tools.memtest
from statistics import mean
from math import sqrt


# Список імен файлів без росширення, в лапках, розділені комами

FILE_LIST = [
             
'1',
'3',
'2',

]


SHOW_STATS = True
SHOW_GRAPH = True



def main(filename):

    print('\n\n' + '-' * 70, '\n')

    # Перехоплення помилки відсутнього файлу
    try:
        # Відкривання abf файлу
        abf = pyabf.ABF(filename + '.abf')
        memtest = pyabf.tools.memtest.Memtest(abf)
    except ValueError:
        print(filename + '.abf','not found!\n\n')
    else:
        print(filename+'.abf\n\n')

        if SHOW_STATS:

            print('Average on', abf.sweepCount,'sweeps:\n')
            print('Ra, MOhm:           ', round(mean(memtest.Ra.values), 2))
            print('Rm, MOhm:           ', round(mean(memtest.Rm.values), 2))
            print('Cm, pF:             ', round(mean(memtest.CmStep.values), 2))
            print('Ih, pA:             ', round(mean(memtest.Ih.values), 2))

            print('\n\nStandard error mean on', abf.sweepCount,'sweeps:\n')
            print('Ra:                 ', round(np.std(memtest.Ra.values) /sqrt(abf.sweepCount), 2))
            print('Rm:                 ', round(np.std(memtest.Rm.values) /sqrt(abf.sweepCount), 2))
            print('Cm:                 ', round(np.std(memtest.CmStep.values) /sqrt(abf.sweepCount),2))
            print('Ih:                 ', round(np.std(memtest.Ih.values) /sqrt(abf.sweepCount), 2))
            print('\n\n')


        if SHOW_GRAPH:

            # Створення нового рисунку
            fig = plt.figure(figsize=(8, 6))

            # Виведення значень опору доступу (Ra)
            ax3 = fig.add_subplot(221)
            ax3.grid(alpha=.2)
            ax3.plot(list(range(1, abf.sweepCount +1)), memtest.Ra.values,
                        ".", color='black', alpha=.7, mew=0)
            ax3.set_title(memtest.Ra.name)
            ax3.set_ylabel(memtest.Ra.units)

            # Виведення значень мембранного опору(Rm)
            ax2 = fig.add_subplot(222)
            ax2.grid(alpha=.2)
            ax2.plot(list(range(1, abf.sweepCount +1)), memtest.Rm.values,
                        ".", color='black', alpha=.7, mew=0)
            ax2.set_title(memtest.Rm.name)
            ax2.set_ylabel(memtest.Rm.units)

            # Виведення значень мембранної ємності (Cm)
            ax4 = fig.add_subplot(223)
            ax4.grid(alpha=.2)
            ax4.plot(list(range(1, abf.sweepCount +1)), memtest.CmStep.values,
                        ".", color='black', alpha=.7, mew=0)
            ax4.set_title(memtest.CmStep.name)
            ax4.set_ylabel(memtest.CmStep.units)

            # Виведення значень струму утримання (Ih)
            ax1 = fig.add_subplot(224)
            ax1.grid(alpha=.2)
            ax1.plot(list(range(1, abf.sweepCount +1)), memtest.Ih.values,
                        ".", color='black', alpha=.7, mew=0)
            ax1.set_title(memtest.Ih.name)
            ax1.set_ylabel(memtest.Ih.units)

            # Вивсети значення на осі абсис
            for ax in [ax1, ax2, ax3, ax4]:
                ax.margins(0, .9)
                ax.set_xlabel("Sweep number")
                for tagTime in abf.tagTimesMin:
                    ax.axvline(tagTime, color='k', ls='--')

            # Вивести рисунок
            plt.tight_layout()
            fig.patch.set_facecolor('white')
            plt.suptitle(filename+'.abf')
            plt.show()

    print('\n\n\n')

for filename in FILE_LIST:
    main(filename)
