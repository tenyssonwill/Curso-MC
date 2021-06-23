import sys
from os.path import join as pjoin
# sys.path.append(r'C:\Program Files\MCXStudio\MCXSuite\mcx\pymcx')
sys.path.append(r'C:\Users\there\IdeaProjects\pymcx')
import pymcx as mcx

mcx_local = pjoin('C:\\', 'Program Files', 'MCXStudio', 'MCXSuite', 'mcx', 'bin', 'mcx.exe')
# mcx_local = "C:\Program Files\MCXStudio\MCXSuite\mcx\bin\mcx.exe"
print(mcx_local)
cfg = mcx.create()  # create a default config dictionary

cfg["Session"]["Photons"] = 1e6
cfg["Optode"]["Detector"] = [{"Pos": [29.0, 19.0, 0.0], "R": 1.0}]
data = mcx.run(cfg, mcxbin=mcx_local)
