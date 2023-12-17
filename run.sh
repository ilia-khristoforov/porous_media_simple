decomposePar

mpirun -np 6 foamRun -parallel > log &
pyFoamPlotWatcher.py log

reconstructPar -latestTime
rm -r processor*

gnuplot plt
