decomposePar

mpirun -np 8 foamRun -parallel > log &
pyFoamPlotWatcher.py log

reconstructPar -latestTime
rm -r processor*