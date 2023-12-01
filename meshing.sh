snappyHexMeshConfig -clearBoundary -insidePoint '(0.07 0.07 0.0027)' -inletRegions '(inlet)' -outletRegions '(outlet)'

blockMesh
decomposePar

mpirun -np 8 snappyHexMesh -parallel

reconstructPar

topoSet