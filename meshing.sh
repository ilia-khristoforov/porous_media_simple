snappyHexMeshConfig -clearBoundary -nCells '(280 260 26)' -insidePoint '(0.07 0.07 0.0027)' -inletRegions '(inlet)' -outletRegions '(outlet)'

blockMesh
decomposePar

mpirun -np 8 snappyHexMesh -parallel

reconstructPar

topoSet


echo 'CLEANING UP'
rm -r processor*
rm -r constant/polyMesh
cp -r 0.04/polyMesh constant/polyMesh
rm -r 0.*
checkMesh
echo 'WE ARE SO READY'
