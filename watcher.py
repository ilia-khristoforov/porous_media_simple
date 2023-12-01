# state file generated using paraview version 5.10.1

# uncomment the following three lines to ensure this script works in future versions
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1146, 790]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [0.07199999690055847, 0.07200000062584877, 0.00139999995008111]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.07152223262276855, 0.07393132637801579, 0.0025078271309129357]
renderView1.CameraFocalPoint = [0.07152072277258671, 0.07218042433561159, 0.0027425838616330304]
renderView1.CameraViewUp = [0.2636439248049695, 0.12796353809397165, 0.9560947724111373]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 0.02503917154418135

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1146, 790)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'PVFoamReader'
porous_media_simple_2OpenFOAM = PVFoamReader(registrationName='porous_media_simple_2.OpenFOAM', FileName='/home/cececerece/OpenFOAM/cececerece-11/run/porous_media_simple_2/porous_media_simple_2.OpenFOAM')
porous_media_simple_2OpenFOAM.MeshParts = ['internalMesh']
porous_media_simple_2OpenFOAM.Fields = ['p', 'U']

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=porous_media_simple_2OpenFOAM)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', 'p']
clip1.Value = 5.3252676333650015

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [0.07200000062584877, 0.07200514897704124, 0.002268237903578962]
clip1.ClipType.Normal = [0.0, 0.0, 1.0]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [0.07200000062584877, 0.07200514897704124, 0.0004002699861302972]

# create a new 'Clip'
clip2 = Clip(registrationName='Clip2', Input=porous_media_simple_2OpenFOAM)
clip2.ClipType = 'Plane'
clip2.HyperTreeGridClipper = 'Plane'
clip2.Scalars = ['POINTS', 'p']
clip2.Value = 5.3252676333650015

# init the 'Plane' selected for 'ClipType'
clip2.ClipType.Origin = [0.039995769659070285, 0.07200514897704124, 0.0004002699861302972]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip2.HyperTreeGridClipper.Origin = [0.07200000062584877, 0.07200514897704124, 0.0004002699861302972]

# create a new 'Clip'
clip3 = Clip(registrationName='Clip3', Input=porous_media_simple_2OpenFOAM)
clip3.ClipType = 'Plane'
clip3.HyperTreeGridClipper = 'Plane'
clip3.Scalars = ['POINTS', 'p']
clip3.Value = 5.3252676333650015

# init the 'Plane' selected for 'ClipType'
clip3.ClipType.Origin = [0.05418908735017745, 0.07200514897704124, 0.0004002699861302972]
clip3.ClipType.Normal = [0.0, 1.0, 0.0]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip3.HyperTreeGridClipper.Origin = [0.07200000062584877, 0.07200514897704124, 0.0004002699861302972]

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=porous_media_simple_2OpenFOAM)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.07200000062584877, 0.07200514897704124, 0.0004002699861302972]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [0.07200000062584877, 0.07200514897704124, 0.0004002699861302972]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from clip3
clip3Display = Show(clip3, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')
uLUT.RGBPoints = [0.0, 0.02, 0.3813, 0.9981, 9.686498833009207e-07, 0.02000006, 0.424267768, 0.96906969, 1.937299766601817e-06, 0.02, 0.467233763, 0.940033043, 2.905949649902738e-06, 0.02, 0.5102, 0.911, 3.874599533203634e-06, 0.02000006, 0.546401494, 0.872669438, 4.843249416504557e-06, 0.02, 0.582600362, 0.83433295, 5.811899299805476e-06, 0.02, 0.6188, 0.796, 6.780549183106374e-06, 0.02000006, 0.652535156, 0.749802434, 7.749199066407292e-06, 0.02, 0.686267004, 0.703599538, 8.717848949708214e-06, 0.02, 0.72, 0.6574, 9.686498833009115e-06, 0.02000006, 0.757035456, 0.603735359, 1.0655148716310009e-05, 0.02, 0.794067037, 0.55006613, 1.162379859961093e-05, 0.02, 0.8311, 0.4964, 1.2592448482911852e-05, 0.021354336738172372, 0.8645368555261631, 0.4285579460761159, 1.3561098366212747e-05, 0.023312914349117714, 0.897999359924484, 0.36073871343115577, 1.452974824951367e-05, 0.015976108242848862, 0.9310479513349017, 0.2925631815088092, 1.5498398132814585e-05, 0.27421074700988196, 0.952562960995083, 0.15356836602739213, 1.6467048016115484e-05, 0.4933546281681699, 0.9619038625309482, 0.11119493614749336, 1.7435697899416383e-05, 0.6439, 0.9773, 0.0469, 1.84043477827173e-05, 0.762401813, 0.984669591, 0.034600153, 1.937299766601823e-05, 0.880901185, 0.992033407, 0.022299877, 2.0341647549319125e-05, 0.9995285432627147, 0.9995193706781492, 0.0134884641450013, 2.1310297432620038e-05, 0.999402998, 0.955036376, 0.079066628, 2.227894731592096e-05, 0.9994, 0.910666223, 0.148134024, 2.324759719922186e-05, 0.9994, 0.8663, 0.2172, 2.421624708252278e-05, 0.999269665, 0.818035981, 0.217200652, 2.5184896965823676e-05, 0.999133332, 0.769766184, 0.2172, 2.6153546849124596e-05, 0.999, 0.7215, 0.2172, 2.7122196732425495e-05, 0.99913633, 0.673435546, 0.217200652, 2.8090846615726438e-05, 0.999266668, 0.625366186, 0.2172, 2.905949649902734e-05, 0.9994, 0.5773, 0.2172, 3.0028146382328237e-05, 0.999402998, 0.521068455, 0.217200652, 3.099679626562915e-05, 0.9994, 0.464832771, 0.2172, 3.196544614893007e-05, 0.9994, 0.4086, 0.2172, 3.293409603223097e-05, 0.9947599917687346, 0.33177297300202935, 0.2112309638520206, 3.390274591553188e-05, 0.9867129505479589, 0.2595183410914934, 0.19012239549291934, 3.4871395798832794e-05, 0.9912458875646419, 0.14799417507952672, 0.21078892136920357, 3.584004568213372e-05, 0.949903037, 0.116867171, 0.252900603, 3.680869556543461e-05, 0.903199533, 0.078432949, 0.291800389, 3.777734544873555e-05, 0.8565, 0.04, 0.3307, 3.874599533203646e-05, 0.798902627, 0.04333345, 0.358434298, 3.971464521533734e-05, 0.741299424, 0.0466667, 0.386166944, 4.0683295098638264e-05, 0.6823529411764706, 0.050980392156862744, 0.41568627450980394, 4.0683295098638264e-05, 0.6837, 0.05, 0.4139]
uLUT.ColorSpace = 'RGB'
uLUT.NanColor = [1.0, 0.0, 0.0]
uLUT.NumberOfTableValues = 16
uLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')
uPWF.Points = [0.0, 0.0, 0.5, 0.0, 4.0683295098638264e-05, 1.0, 0.5, 0.0]
uPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
clip3Display.Representation = 'Surface'
clip3Display.ColorArrayName = ['POINTS', 'U']
clip3Display.LookupTable = uLUT
clip3Display.SelectTCoordArray = 'None'
clip3Display.SelectNormalArray = 'None'
clip3Display.SelectTangentArray = 'None'
clip3Display.OSPRayScaleArray = 'U'
clip3Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip3Display.SelectOrientationVectors = 'None'
clip3Display.ScaleFactor = 0.006692200154066086
clip3Display.SelectScaleArray = 'None'
clip3Display.GlyphType = 'Arrow'
clip3Display.GlyphTableIndexArray = 'None'
clip3Display.GaussianRadius = 0.0003346100077033043
clip3Display.SetScaleArray = ['POINTS', 'U']
clip3Display.ScaleTransferFunction = 'PiecewiseFunction'
clip3Display.OpacityArray = ['POINTS', 'U']
clip3Display.OpacityTransferFunction = 'PiecewiseFunction'
clip3Display.DataAxesGrid = 'GridAxesRepresentation'
clip3Display.PolarAxes = 'PolarAxesRepresentation'
clip3Display.ScalarOpacityFunction = uPWF
clip3Display.ScalarOpacityUnitDistance = 0.0006712675326459727
clip3Display.OpacityArrayName = ['POINTS', 'U']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip3Display.ScaleTransferFunction.Points = [-0.00014868071593809873, 0.0, 0.5, 0.0, 0.0012949509546160698, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip3Display.OpacityTransferFunction.Points = [-0.00014868071593809873, 0.0, 0.5, 0.0, 0.0012949509546160698, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for uLUT in view renderView1
uLUTColorBar = GetScalarBar(uLUT, renderView1)
uLUTColorBar.Title = 'U'
uLUTColorBar.ComponentTitle = 'Magnitude'

# set color bar visibility
uLUTColorBar.Visibility = 1

# show color legend
clip3Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(clip3)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')