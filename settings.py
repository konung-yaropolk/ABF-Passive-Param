# To run script install libraries using command:
# pip install pyabf

# Note: for baselined records Holding Current measurements will be incorrect. 
# To get correct holding current values use intact records only.

# Parameters:

FIGURE_W = 5  # widtn in inches
FIGURE_H = 5  # Height in inches

X_TICKS = 'time'    # show 'time' or 'sweeps' on X axis

MAKE_STATS = True     # save .csv file for each listed .abf file with values for each sweep
SHOW_GRAPH = False
SAVE_GRAPH = True     # save summary figure for each listed .abf file
SAVE_FORMAT = 'png'   # png, svg, pdf, eps

DIRECTORY = 'F:/Lab Work Files/Patch-clamp data'    # full path to directory with files, leave empty if you run this script in it

FILES_LIST = [

# Список імен abf файлів без росширення, в лапках, розділені комами, номер трейсу для нарізки (починаючи з нульового)




# # MCU Project:

# # 2M Ca:

# ['/MCU_Project_Yariks_data/2021_04_15/2021_04_15_0000.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_19/2021_04_19_0006.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_19/2021_04_19_0009.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_19/2021_04_19_0010.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_19/2021_04_19_0014.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_20_M1/2021_04_20_0001.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_20_M1/2021_04_20_0002.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_20_M2/2021_04_20_0008.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_20_M2/2021_04_20_0010.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_20_M2/2021_04_20_0011.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_22/2021_04_22_0004.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_22/2021_04_22_0005.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_22/2021_04_22_0010.abf', 14],
# ['/MCU_Project_Yariks_data/2021_04_22/2021_04_22_0011.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_22/2021_04_22_0016.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_22/2021_04_22_0018.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_22/2021_04_22_0024.abf', 13],
# ['/MCU_Project_Yariks_data/2021_04_22/2021_04_22_0025.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_23/2021_04_23_0000.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_23/2021_04_23_0001.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_23/2021_04_23_0005.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_23/2021_04_23_0006.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_23/2021_04_23_0011.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_23/2021_04_23_0018.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_23/2021_04_23_0019.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_25/2021_04_25_0009.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_25/2021_04_25_0010.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_25/2021_04_25_0015.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_26/2021_04_26_0006.abf', 13],
# ['/MCU_Project_Yariks_data/2021_04_26/2021_04_26_0010.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_26/2021_04_26_0011.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_26/2021_04_26_0021.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_26/2021_04_26_0022.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_26/2021_04_26_0025.abf', 13],
# ['/MCU_Project_Yariks_data/2021_04_26/2021_04_26_0027.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_26/2021_04_26_0028.abf', 13],
# ['/MCU_Project_Yariks_data/2021_04_30/2021_04_30_0001.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_30/2021_04_30_0006.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_30/2021_04_30_0013.abf', 11],
# ['/MCU_Project_Yariks_data/2021_05_04/2021_05_04_0001.abf', 13],
# ['/MCU_Project_Yariks_data/2021_05_04/2021_05_04_0004.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_04/2021_05_04_0005.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_04/2021_05_04_0009.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_04/2021_05_04_0010.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_04/2021_05_04_0013.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_04/2021_05_04_0016.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_06/2021_05_06_0004.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_06/2021_05_06_0005.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_07/2021_05_07_0000.abf', 15],
# ['/MCU_Project_Yariks_data/2021_05_07/2021_05_07_0004.abf', 13],
# ['/MCU_Project_Yariks_data/2021_05_07/2021_05_07_0005.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_07/2021_05_07_0009.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_07/2021_05_07_0016.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M1/2021_05_10_0004.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M1/2021_05_10_0007.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M1/2021_05_10_0009.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M1/2021_05_10_0012.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M1/2021_05_10_0014.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M1/2021_05_10_0017.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M1/2021_05_10_0021.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M2/2021_05_10_0029.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M2/2021_05_10_0031.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M2/2021_05_10_0034.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M2/2021_05_10_0038.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M2/2021_05_10_0043.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M2/2021_05_10_0045.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M2/2021_05_11_0005.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M2/2021_05_11_0007.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M2/2021_05_11_0012.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M2/2021_05_11_0014.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_11/2021_05_11_0030.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_11/2021_05_11_0032.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_11/2021_05_11_0036.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_11/2021_05_11_0049.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_11/2021_05_11_0051.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_11/2021_05_11_0055.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_11/2021_05_11_0062.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_11/2021_05_11_0064.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_11/2021_05_11_0069.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_11/2021_05_11_0071.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_12_0002.abf', 14],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_12_0005.abf', 13],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_12_0009.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_12_0017.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_12_0019.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_12_0025.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_12_0027.abf', 13],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_12_0032.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_12_0034.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_12_0038.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_12_0042.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_12_0046.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_12_0052.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_13_0004.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_13_0006.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_13_0014.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_13_0023.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_13/2021_05_13_0036.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_13/2021_05_13_0038.abf', 11],
# ['/MCU_Project_Yariks_data/2021_05_13/2021_05_13_0046.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_13/2021_05_13_0053.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_13/2021_05_13_0055.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_14/2021_05_14_0002.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_14/2021_05_14_0003.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_14/2021_05_14_0009.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_14/2021_05_14_0010.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_14/2021_05_14_0015.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_14/2021_05_14_0017.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_19/2021_05_19_0006.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_19/2021_05_19_0008.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_19/2021_05_19_0015.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_19/2021_05_19_0026.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_19/2021_05_19_0028.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_19/2021_05_19_0037.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_19/2021_05_19_0039.abf', 13],
# ['/MCU_Project_Yariks_data/2021_05_19/2021_05_19_0053.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_19/2021_05_19_0054.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_19/2021_05_19_0057.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_19/2021_05_20_0000.abf', 13],
# ['/MCU_Project_Yariks_data/2021_05_20_M2/2021_05_20_0012.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_20_M2/2021_05_20_0013.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_20_M2/2021_05_20_0017.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_20_M2/2021_05_20_0020.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_20_M2/2021_05_20_0021.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_20_M2/2021_05_20_0023.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_20_M2/2021_05_20_0024.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_20_M2/2021_05_20_0030.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_20_M2/2021_05_20_0031.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_27/2021_05_27_0009.abf', 13],
# ['/MCU_Project_Yariks_data/2021_05_27/2021_05_27_0010.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_27/2021_05_27_0025.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0004.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0005.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0012.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0013.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0020.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0019.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0031.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0033.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0034.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0039.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0042.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0046.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_29/2021_05_29_0007.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_29/2021_05_29_0008.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_29/2021_05_29_0009.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_29/2021_05_29_0026.abf', 13],
# ['/MCU_Project_Yariks_data/2021_05_29/2021_05_29_0028.abf', 13],
# ['/MCU_Project_Yariks_data/2021_05_31/2021_05_31_0003.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_31/2021_05_31_0005.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_01_M2/2021_06_01_0012.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_01_M2/2021_06_01_0013.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_01_M2/2021_06_01_0018.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0014.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0019.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0020.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0027.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0028.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0033.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0034.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0038.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0039.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0048.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0050.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0057.abf', 14],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0058.abf', 13],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_03_0004.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_03_0009.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_03_0013.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_03_0014.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_03/2021_06_03_0029.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_03/2021_06_03_0034.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_03/2021_06_03_0035.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_03/2021_06_04_0001.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_03/2021_06_04_0002.abf', 11],
# ['/MCU_Project_Yariks_data/2021_06_04/2021_06_04_0011.abf', 13],
# ['/MCU_Project_Yariks_data/2021_06_05_M2/2021_06_05_0009.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_05_M2/2021_06_06_0001.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_05_M2/2021_06_06_0004.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_05_M2/2021_06_06_0005.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_05_M2/2021_06_06_0015.abf', 17],
# ['/MCU_Project_Yariks_data/2021_06_05_M2/2021_06_06_0016.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0006.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0008.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0012.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0014.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0016.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0017.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0020.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0021.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0025.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0026.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0030.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0033.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0037.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0040.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0041.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0001.abf', 7],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0005.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0006.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0011.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0012.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0018.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0020.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0021.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0027.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0028.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0036.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0037.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0043.abf', 14],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0044.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0057.abf', 11],
# ['/MCU_Project_Yariks_data/2021_06_08/2021_06_08_0062.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_08/2021_06_08_0065.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_08/2021_06_08_0071.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_08/2021_06_08_0072.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_08/2021_06_08_0075.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_11/2021_05_11_0075.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_22/2021_04_22_0004.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_22/2021_04_22_0005.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_03/2021_06_03_0040.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_03/2021_06_03_0041.abf', 12],




# # 1M Ca:

# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0025.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0036.abf', 9],
# ['/MCU_Project_Yariks_data/2021_05_29/2021_05_29_0029.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0030.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0031.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0041.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0042.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0052.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0053.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0059.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0060.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_03_0015.abf', 14],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_03_0016.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_03_0017.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_03/2021_06_03_0036.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_03/2021_06_03_0037.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_03/2021_06_04_0004.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_05_M2/2021_06_05_0012.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_05_M2/2021_06_05_0017.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_05_M2/2021_06_06_0007.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_05_M2/2021_06_06_0008.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_05_M2/2021_06_06_0013.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0023.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0028.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0035.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0036.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0043.abf', 13],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0000.abf', 14],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0007.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0008.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0009.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0014.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0015.abf', 13],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0030.abf', 13],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0031.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0039.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0040.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0046.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0047.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_08/2021_06_08_0077.abf', 12],




# # 2M & 1M in 2022:

# ['/MCU_Project_Yariks_data/2022_09_14/2022_09_14_0003.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_14/2022_09_14_0004.abf', 13],
# ['/MCU_Project_Yariks_data/2022_09_14/2022_09_14_0005.abf', 9],
# ['/MCU_Project_Yariks_data/2022_09_14/2022_09_14_0006.abf', 13],

# ['/MCU_Project_Yariks_data/2022_09_19/2022_09_19_0001.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_19/2022_09_19_0002.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_19/2022_09_19_0006.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_19/2022_09_19_0008.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_19/2022_09_19_0012.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_19/2022_09_19_0013.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_19/2022_09_19_0014.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_19/2022_09_19_0021.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_19/2022_09_19_0022.abf', 12],

# ['/MCU_Project_Yariks_data/2022_09_20/2022_09_20_0001.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_20/2022_09_20_0002.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_20/2022_09_20_0005.abf', 13],
# ['/MCU_Project_Yariks_data/2022_09_20/2022_09_20_0006.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_20/2022_09_20_0009.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_20/2022_09_20_0011.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_20/2022_09_20_0014.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_20/2022_09_20_0015.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_20/2022_09_20_0023.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_20/2022_09_20_0028.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_20/2022_09_20_0033.abf', 13],
# ['/MCU_Project_Yariks_data/2022_09_20/2022_09_20_0034.abf', 13],

# ['/MCU_Project_Yariks_data/2022_09_21/2022_09_21_0001.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_21/2022_09_21_0003.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_21/2022_09_21_0005.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_21/2022_09_21_0007.abf', 12],

# ['/MCU_Project_Yariks_data/2022_09_22/2022_09_22_0003.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_22/2022_09_22_0006.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_22/2022_09_22_0007.abf', 4],
# ['/MCU_Project_Yariks_data/2022_09_22/2022_09_22_0013.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_22/2022_09_22_0014.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_22/2022_09_22_0020.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_22/2022_09_22_0021.abf', 4],

# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_29_0001.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_29_0006.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_29_0007.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_29_0014.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_29_0015.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_29_0020.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_29_0021.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_29_0026.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_29_0028.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_29_0032.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_29_0033.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_29_0036.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_30_0000.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_30_0003.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_30_0004.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_30_0009.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_30_0010.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_30_0013.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_30_0016.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_30_0017.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_30_0023.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_30_0024.abf', 12],




# # 2M & 1M & 4M in 2023:

# ['/MCU_Project_Yariks_data/2023_02_08/2023_02_08_0004.abf', 12],
# ['/MCU_Project_Yariks_data/2023_02_08/2023_02_08_0008.abf', 14],
# ['/MCU_Project_Yariks_data/2023_02_08/2023_02_08_0013.abf', 12],
# ['/MCU_Project_Yariks_data/2023_02_08/2023_02_08_0014.abf', 22],
# ['/MCU_Project_Yariks_data/2023_02_08/2023_02_08_0016.abf', 12],
# ['/MCU_Project_Yariks_data/2023_02_08/2023_02_08_0017.abf', 12],
# ['/MCU_Project_Yariks_data/2023_02_08/2023_02_08_0018.abf', 23],
# ['/MCU_Project_Yariks_data/2023_02_08/2023_02_08_0019.abf', 12],

# ['/MCU_Project_Yariks_data/2023_02_16/2023_02_16_0001.abf', 12],
# ['/MCU_Project_Yariks_data/2023_02_16/2023_02_16_0004.abf', 12],
# ['/MCU_Project_Yariks_data/2023_02_16/2023_02_16_0005.abf', 12],
# ['/MCU_Project_Yariks_data/2023_02_16/2023_02_16_0006.abf', 22],
# ['/MCU_Project_Yariks_data/2023_02_16/2023_02_16_0007.abf', 12],
# ['/MCU_Project_Yariks_data/2023_02_16/2023_02_16_0012.abf', 12],

# ['/MCU_Project_Yariks_data/2023_04_07/2023_04_07_0003.abf', 12],
# ['/MCU_Project_Yariks_data/2023_04_07/2023_04_07_0007.abf', 12],

# ['/MCU_Project_Yariks_data/2023_04_10/2023_04_10_0001.abf', 12],
# ['/MCU_Project_Yariks_data/2023_04_10/2023_04_10_0003.abf', 12],
# ['/MCU_Project_Yariks_data/2023_04_10/2023_04_10_0004.abf', 12],
# ['/MCU_Project_Yariks_data/2023_04_10/2023_04_10_0007.abf', 12],

# ['/MCU_Project_Yariks_data/2023_04_20/2023_04_20_0001.abf', 12],
# ['/MCU_Project_Yariks_data/2023_04_20/2023_04_20_0002.abf', 12],
# ['/MCU_Project_Yariks_data/2023_04_20/2023_04_20_0003.abf', 22],
# ['/MCU_Project_Yariks_data/2023_04_20/2023_04_20_0004.abf', 12],
# ['/MCU_Project_Yariks_data/2023_04_20/2023_04_20_0010.abf', 12],

# ['/MCU_Project_Yariks_data/2023_04_27/2023_04_27_0001.abf', 18],
# ['/MCU_Project_Yariks_data/2023_04_27/2023_04_27_0017.abf', 12],
# ['/MCU_Project_Yariks_data/2023_04_27/2023_04_27_0024.abf', 12],

# ['/MCU_Project_Yariks_data/2023_05_03/2023_05_03_0010.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_03/2023_05_03_0012.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_03/2023_05_03_0013.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_03/2023_05_03_0014.abf', 23],
# ['/MCU_Project_Yariks_data/2023_05_03/2023_05_03_0015.abf', 13],
# ['/MCU_Project_Yariks_data/2023_05_03/2023_05_03_0022.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_03/2023_05_03_0024.abf', 12],

# ['/MCU_Project_Yariks_data/2023_05_05/2023_05_05_0001.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_05/2023_05_05_0002.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_05/2023_05_05_0003.abf', 22],
# ['/MCU_Project_Yariks_data/2023_05_05/2023_05_05_0004.abf', 12],

# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0001.abf', 14],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0006.abf', 11],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0007.abf', 11],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0008.abf', 22],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0009.abf', 11],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0016.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0017.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0018.abf', 22],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0019.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0024.abf', 14],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0026.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0027.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0028.abf', 22],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0029.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0033.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0034.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0035.abf', 22],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0036.abf', 13],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0043.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0044.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0045.abf', 30],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0046.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0048.abf', 13],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0049.abf', 13],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0050.abf', 23],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0051.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0055.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0057.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0058.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0059.abf', 25],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_09_0000.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_09_0005.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_09_0006.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_09_0007.abf', 22],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_09_0008.abf', 13],

# ['/MCU_Project_Yariks_data/2023_05_10/2023_05_10_0007.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_10/2023_05_10_0008.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_10/2023_05_10_0009.abf', 22],
# ['/MCU_Project_Yariks_data/2023_05_10/2023_05_10_0010.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_10/2023_05_10_0015.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_10/2023_05_10_0016.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_10/2023_05_10_0018.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_10/2023_05_10_0019.abf', 6],
# ['/MCU_Project_Yariks_data/2023_05_10/2023_05_10_0020.abf', 22],
# ['/MCU_Project_Yariks_data/2023_05_10/2023_05_10_0021.abf', 12],




# # SNI/SHAM + PMX205:

# ['/SNI-SHAM + PMX/2023_08_10/2023_08_10_0006.abf',0],
# ['/SNI-SHAM + PMX/2023_08_10/2023_08_10_0012.abf',0],
# ['/SNI-SHAM + PMX/2023_08_10/2023_08_10_0017.abf',0],

# ['/SNI-SHAM + PMX/2023_08_11/2023_08_11_0005.abf',0],
# ['/SNI-SHAM + PMX/2023_08_11/2023_08_11_0008.abf',0],
# ['/SNI-SHAM + PMX/2023_08_11/2023_08_11_0011.abf',0],
# ['/SNI-SHAM + PMX/2023_08_11/2023_08_11_0014.abf',0],
# ['/SNI-SHAM + PMX/2023_08_11/2023_08_11_0017.abf',0],
# ['/SNI-SHAM + PMX/2023_08_11/2023_08_11_0020.abf',0],
# ['/SNI-SHAM + PMX/2023_08_11/2023_08_11_0023.abf',0],

# ['/SNI-SHAM + PMX/2023_08_28/2023_08_28_0003.abf',0],
# ['/SNI-SHAM + PMX/2023_08_28/2023_08_28_0007.abf',0],
# ['/SNI-SHAM + PMX/2023_08_28/2023_08_28_0011.abf',0],
# ['/SNI-SHAM + PMX/2023_08_28/2023_08_28_0015.abf',0],

# ['/SNI-SHAM + PMX/2023_08_31/2023_08_31_0020.abf',0],
# ['/SNI-SHAM + PMX/2023_08_31/2023_08_31_0021.abf',0],




# # TRP project:

# ['/TRP project/2024_03_11/2024_03_11_0003.abf',0],
# ['/TRP project/2024_03_11/2024_03_11_0006.abf',0],
# ['/TRP project/2024_03_11/2024_03_11_0008.abf',0],
# ['/TRP project/2024_03_11/2024_03_11_0009.abf',0],

# ['/TRP project/2024_03_12/2024_03_12_0001.abf',0],
# ['/TRP project/2024_03_12/2024_03_12_0003.abf',0],
# ['/TRP project/2024_03_12/2024_03_12_0005.abf',0],

# ['/TRP project/2024_03_24/2024_03_24_0001.abf',0],

# ['/TRP project/2024_03_25/2024_03_25_0009.abf',0],
# ['/TRP project/2024_03_25/2024_03_25_0011.abf',0],

# ['/TRP project/2024_03_26_M1/2024_03_26_0001.abf',0],
# ['/TRP project/2024_03_26_M1/2024_03_26_0003.abf',0],
    
# ['/TRP project/2024_03_26_M2/2024_03_26_0007.abf',0],

# ['/TRP project/2024_04_08/2024_04_09_0004.abf',0],

# ['/TRP project/2024_04_09/2024_04_09_0006.abf',0],

# ['/TRP project/2024_04_18/2024_04_18_0003.abf',0],

# ['/TRP project/2024_05_21_M1/2024_05_21_0006.abf',0],
# ['/TRP project/2024_05_21_M2/2024_05_21_0009.abf',0],
# ['/TRP project/2024_05_22/2024_05_22_0010.abf',0],
# ['/TRP project/2024_05_23_M1/2024_05_23_0001.abf',0],
# ['/TRP project/2024_05_23_M2/2024_05_23_0004.abf',0],
# ['/TRP project/2024_05_23_M2/2024_05_23_0008.abf',0],

# ['/TRP project/2024_05_28_M1/2024_05_28_0001.abf',0],
# ['/TRP project/2024_05_28_M1/2024_05_28_0003.abf',0],
# ['/TRP project/2024_05_29_M1/2024_05_29_0008.abf',0],
# ['/TRP project/2024_05_29_M1/2024_05_29_0012.abf',0],
# ['/TRP project/2024_05_29_M2/2024_05_29_0016.abf',0],
# ['/TRP project/2024_05_29_M3/2024_05_29_0020.abf',0],

]


if __name__ == '__main__':
    ABF_passive_param = __import__('ABF-passive-param')
    ABF_passive_param.main()