#!/usr/bin/env python3

# To run script install libraries using command:
# pip install pyabf

import csv
import numpy as np
import matplotlib.pyplot as plt
import pyabf
import pyabf.tools.memtest
from statistics import mean
from math import sqrt

import settings as s


def make_stats(memtest, abf, path, filename):

    '''
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
    '''


    names = ['Sweep #:','Ra, MOhm:', 'Ih, pA:', 'Rm, MOhm:', 'Cm, pF:']
    units = ['','Ra, MOhm:', 'Ih, pA:', 'Rm, MOhm:', 'Cm, pF:']
    body = list(zip(*[[i+1 for i in range(len(memtest.Ra.values))],
                      memtest.Ra.values, 
                      memtest.Ih.values, 
                      memtest.Rm.values, 
                      memtest.CmStep.values]))    

    median = ['Median:',
               round(mean(memtest.Ra.values), 2),
               round(mean(memtest.Ih.values), 2),
               round(mean(memtest.Rm.values), 2), 
               round(mean(memtest.CmStep.values), 2)]

    sem = ['StdErrMean:',
              round(np.std(memtest.Ra.values) /sqrt(abf.sweepCount), 2),
              round(np.std(memtest.Ih.values) /sqrt(abf.sweepCount), 2),
              round(np.std(memtest.Rm.values) /sqrt(abf.sweepCount), 2),
              round(np.std(memtest.CmStep.values) /sqrt(abf.sweepCount),2)]

    with open(path + filename + '_memtest.csv', 'w') as f:     
        write = csv.writer(f, delimiter=',', lineterminator='\r',)
        write.writerow(names)
        write.writerow([''])
        write.writerows(body)
        write.writerow([''])
        write.writerow(units)
        write.writerow(median)
        write.writerow(sem)





def make_plot(memtest, memtest_ih, abf, abf_ih, path, filename):

    if s.X_TICKS == 'time': 
        x_ticks = abf.sweepTimesMin
        x_ticks_ih = abf_ih.sweepTimesMin
        x_label = "Recording Time (minutes)"
        
    if s.X_TICKS == 'sweeps': 
        x_ticks = list(range(1, abf.sweepCount +1))
        x_ticks_ih = list(range(1, abf_ih.sweepCount +1))
        x_label = "Sweep number"
        

    fig = plt.figure(figsize=(s.FIGURE_W, s.FIGURE_H))

    ax3 = fig.add_subplot(221)
    ax3.grid(alpha=.3)
    ax3.plot(x_ticks, memtest.Ra.values,
            ".", color='C0', alpha=.7, mew=0)
    ax3.set_title(memtest.Ra.name)
    ax3.set_ylabel(memtest.Ra.units)

    ax1 = fig.add_subplot(222)
    ax1.grid(alpha=.3)
    ax1.plot(x_ticks_ih, memtest_ih.Ih.values,
            ".", color='C3', alpha=.7, mew=0)
    ax1.set_title(memtest_ih.Ih.name)
    ax1.set_ylabel(memtest_ih.Ih.units)

    ax2 = fig.add_subplot(223)
    ax2.grid(alpha=.3)
    ax2.plot(x_ticks, memtest.Rm.values,
            ".", color='C5', alpha=.7, mew=0)
    ax2.set_title(memtest.Rm.name)
    ax2.set_ylabel(memtest.Rm.units)

    ax4 = fig.add_subplot(224)
    ax4.grid(alpha=.3)
    ax4.plot(x_ticks, memtest.CmStep.values,
            ".", color='C2', alpha=.7, mew=0)
    ax4.set_title(memtest.CmStep.name)
    ax4.set_ylabel(memtest.CmStep.units)

    for ax in [ax1, ax2, ax3, ax4]:
        ax.margins(0.1, 0.9)
        ax.set_xlabel(x_label)
        for tagTime in abf.tagTimesMin:
            ax.axvline(tagTime, color='k', ls='--')


    # Вивести рисунок
    plt.tight_layout()
    fig.patch.set_facecolor('white')
    plt.suptitle('')   # (filename[-15:])  # Вывести только имя файла (последние 15 символов пути для типичного abf файла)

    if s.SAVE_GRAPH:
        plt.savefig(path + filename + '_memtest.' + s.SAVE_FORMAT, transparent=True)    
        
    if s.SHOW_GRAPH:
        plt.show()
    
    plt.close()



def process_abf(path, filename):

    # print('\n' + '-' * 70, '\n')

    # Перехоплення помилки відсутнього файлу
    try:
        # Відкривання abf файлу
        abf = pyabf.ABF(path + filename)
        abf_ih = pyabf.ABF(path + filename.replace('_baselined.abf', '.abf'))   # substract '_baselined' from filename

        memtest = pyabf.tools.memtest.Memtest(abf)
        memtest_ih = pyabf.tools.memtest.Memtest(abf_ih)

    except ValueError as e:
        print(e)

    else:
        try:
            if s.SHOW_GRAPH or s.SAVE_GRAPH:                 
                make_plot(memtest, memtest_ih, abf, abf_ih, path, filename)
        
            if s.MAKE_STATS:                
                make_stats(memtest, abf, path, filename)

        except Exception as e: 
            print(e)
            
        else: 
            print(path + filename, '    -done')

def main():

    for i,j in s.FILES_LIST:
        process_abf(s.DIRECTORY,i)

if __name__ == '__main__':
    main()