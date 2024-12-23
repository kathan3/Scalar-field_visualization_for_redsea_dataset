# trace generated using paraview version 5.13.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
redseasmallvtk = LegacyVTKReader(registrationName='redseasmall.vtk', FileNames=['/home/kathan/Documents/IISc_sem_3/Graphics_and_Visualizaiton/Submission_2/redseasmall/redseasmall.vtk'])

# set active source
SetActiveSource(redseasmallvtk)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
redseasmallvtkDisplay = Show(redseasmallvtk, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
redseasmallvtkDisplay.Selection = None
redseasmallvtkDisplay.Representation = 'Outline'
redseasmallvtkDisplay.ColorArrayName = [None, '']
redseasmallvtkDisplay.LookupTable = None
redseasmallvtkDisplay.MapScalars = 1
redseasmallvtkDisplay.MultiComponentsMapping = 0
redseasmallvtkDisplay.InterpolateScalarsBeforeMapping = 1
redseasmallvtkDisplay.UseNanColorForMissingArrays = 0
redseasmallvtkDisplay.Opacity = 1.0
redseasmallvtkDisplay.PointSize = 2.0
redseasmallvtkDisplay.LineWidth = 1.0
redseasmallvtkDisplay.RenderLinesAsTubes = 0
redseasmallvtkDisplay.RenderPointsAsSpheres = 0
redseasmallvtkDisplay.DisableLighting = 0
redseasmallvtkDisplay.Diffuse = 1.0
redseasmallvtkDisplay.Interpolation = 'Gouraud'
redseasmallvtkDisplay.Specular = 0.0
redseasmallvtkDisplay.SpecularColor = [1.0, 1.0, 1.0]
redseasmallvtkDisplay.SpecularPower = 100.0
redseasmallvtkDisplay.Luminosity = 0.0
redseasmallvtkDisplay.Ambient = 0.0
redseasmallvtkDisplay.Roughness = 0.3
redseasmallvtkDisplay.Metallic = 0.0
redseasmallvtkDisplay.EdgeTint = [1.0, 1.0, 1.0]
redseasmallvtkDisplay.Anisotropy = 0.0
redseasmallvtkDisplay.AnisotropyRotation = 0.0
redseasmallvtkDisplay.BaseIOR = 1.5
redseasmallvtkDisplay.CoatStrength = 0.0
redseasmallvtkDisplay.CoatIOR = 2.0
redseasmallvtkDisplay.CoatRoughness = 0.0
redseasmallvtkDisplay.CoatColor = [1.0, 1.0, 1.0]
redseasmallvtkDisplay.SelectNormalArray = 'None'
redseasmallvtkDisplay.SelectTangentArray = 'None'
redseasmallvtkDisplay.ComputePointNormals = 0
redseasmallvtkDisplay.Splitting = 1
redseasmallvtkDisplay.FeatureAngle = 30.0
redseasmallvtkDisplay.SelectTCoordArray = 'None'
redseasmallvtkDisplay.Texture = None
redseasmallvtkDisplay.RepeatTextures = 1
redseasmallvtkDisplay.InterpolateTextures = 0
redseasmallvtkDisplay.SeamlessU = 0
redseasmallvtkDisplay.SeamlessV = 0
redseasmallvtkDisplay.UseMipmapTextures = 0
redseasmallvtkDisplay.ShowTexturesOnBackface = 1
redseasmallvtkDisplay.BaseColorTexture = None
redseasmallvtkDisplay.NormalTexture = None
redseasmallvtkDisplay.NormalScale = 1.0
redseasmallvtkDisplay.CoatNormalTexture = None
redseasmallvtkDisplay.CoatNormalScale = 1.0
redseasmallvtkDisplay.MaterialTexture = None
redseasmallvtkDisplay.OcclusionStrength = 1.0
redseasmallvtkDisplay.AnisotropyTexture = None
redseasmallvtkDisplay.EmissiveTexture = None
redseasmallvtkDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
redseasmallvtkDisplay.TextureTransform = 'Transform2'
redseasmallvtkDisplay.EdgeOpacity = 1.0
redseasmallvtkDisplay.BackfaceRepresentation = 'Follow Frontface'
redseasmallvtkDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
redseasmallvtkDisplay.BackfaceOpacity = 1.0
redseasmallvtkDisplay.Translation = [0.0, 0.0, 0.0]
redseasmallvtkDisplay.Scale = [1.0, 1.0, 1.0]
redseasmallvtkDisplay.Orientation = [0.0, 0.0, 0.0]
redseasmallvtkDisplay.Origin = [0.0, 0.0, 0.0]
redseasmallvtkDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
redseasmallvtkDisplay.Pickable = 1
redseasmallvtkDisplay.Triangulate = 0
redseasmallvtkDisplay.UseShaderReplacements = 0
redseasmallvtkDisplay.ShaderReplacements = ''
redseasmallvtkDisplay.NonlinearSubdivisionLevel = 1
redseasmallvtkDisplay.MatchBoundariesIgnoringCellOrder = 0
redseasmallvtkDisplay.UseDataPartitions = 0
redseasmallvtkDisplay.OSPRayUseScaleArray = 'All Approximate'
redseasmallvtkDisplay.OSPRayScaleArray = 'SALT'
redseasmallvtkDisplay.OSPRayScaleFunction = 'Piecewise Function'
redseasmallvtkDisplay.OSPRayMaterial = 'None'
redseasmallvtkDisplay.Assembly = ''
redseasmallvtkDisplay.SelectedBlockSelectors = ['']
redseasmallvtkDisplay.BlockSelectors = ['/']
redseasmallvtkDisplay.BlockColors = []
redseasmallvtkDisplay.BlockColorArrayNames = []
redseasmallvtkDisplay.BlockLookupTables = []
redseasmallvtkDisplay.BlockUseSeparateColorMaps = []
redseasmallvtkDisplay.BlockMapScalars = []
redseasmallvtkDisplay.BlockInterpolateScalarsBeforeMappings = []
redseasmallvtkDisplay.BlockOpacities = []
redseasmallvtkDisplay.BlockMapScalarsGUI = 1
redseasmallvtkDisplay.BlockInterpolateScalarsBeforeMappingsGUI = 1
redseasmallvtkDisplay.BlockOpacitiesGUI = 1.0
redseasmallvtkDisplay.Orient = 0
redseasmallvtkDisplay.OrientationMode = 'Direction'
redseasmallvtkDisplay.SelectOrientationVectors = 'None'
redseasmallvtkDisplay.Scaling = 0
redseasmallvtkDisplay.ScaleMode = 'No Data Scaling Off'
redseasmallvtkDisplay.ScaleFactor = 1.9600000000000002
redseasmallvtkDisplay.SelectScaleArray = 'None'
redseasmallvtkDisplay.GlyphType = 'Arrow'
redseasmallvtkDisplay.UseGlyphTable = 0
redseasmallvtkDisplay.GlyphTableIndexArray = 'None'
redseasmallvtkDisplay.UseCompositeGlyphTable = 0
redseasmallvtkDisplay.UseGlyphCullingAndLOD = 0
redseasmallvtkDisplay.LODValues = []
redseasmallvtkDisplay.ColorByLODIndex = 0
redseasmallvtkDisplay.GaussianRadius = 0.098
redseasmallvtkDisplay.ShaderPreset = 'Sphere'
redseasmallvtkDisplay.CustomTriangleScale = 3
redseasmallvtkDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
redseasmallvtkDisplay.Emissive = 0
redseasmallvtkDisplay.ScaleByArray = 0
redseasmallvtkDisplay.SetScaleArray = ['POINTS', 'SALT']
redseasmallvtkDisplay.ScaleArrayComponent = ''
redseasmallvtkDisplay.UseScaleFunction = 1
redseasmallvtkDisplay.ScaleTransferFunction = 'Piecewise Function'
redseasmallvtkDisplay.OpacityByArray = 0
redseasmallvtkDisplay.OpacityArray = ['POINTS', 'SALT']
redseasmallvtkDisplay.OpacityArrayComponent = ''
redseasmallvtkDisplay.OpacityTransferFunction = 'Piecewise Function'
redseasmallvtkDisplay.DataAxesGrid = 'Grid Axes Representation'
redseasmallvtkDisplay.SelectionCellLabelBold = 0
redseasmallvtkDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
redseasmallvtkDisplay.SelectionCellLabelFontFamily = 'Arial'
redseasmallvtkDisplay.SelectionCellLabelFontFile = ''
redseasmallvtkDisplay.SelectionCellLabelFontSize = 18
redseasmallvtkDisplay.SelectionCellLabelItalic = 0
redseasmallvtkDisplay.SelectionCellLabelJustification = 'Left'
redseasmallvtkDisplay.SelectionCellLabelOpacity = 1.0
redseasmallvtkDisplay.SelectionCellLabelShadow = 0
redseasmallvtkDisplay.SelectionPointLabelBold = 0
redseasmallvtkDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
redseasmallvtkDisplay.SelectionPointLabelFontFamily = 'Arial'
redseasmallvtkDisplay.SelectionPointLabelFontFile = ''
redseasmallvtkDisplay.SelectionPointLabelFontSize = 18
redseasmallvtkDisplay.SelectionPointLabelItalic = 0
redseasmallvtkDisplay.SelectionPointLabelJustification = 'Left'
redseasmallvtkDisplay.SelectionPointLabelOpacity = 1.0
redseasmallvtkDisplay.SelectionPointLabelShadow = 0
redseasmallvtkDisplay.PolarAxes = 'Polar Axes Representation'
redseasmallvtkDisplay.ScalarOpacityUnitDistance = 0.1808356859802089
redseasmallvtkDisplay.ScalarOpacityFunction = None
redseasmallvtkDisplay.TransferFunction2D = None
redseasmallvtkDisplay.UseSeparateOpacityArray = 0
redseasmallvtkDisplay.OpacityArrayName = ['POINTS', 'SALT']
redseasmallvtkDisplay.OpacityComponent = ''
redseasmallvtkDisplay.UseTransfer2D = 0
redseasmallvtkDisplay.UseGradientForTransfer2D = 1
redseasmallvtkDisplay.ColorArray2Name = ['POINTS', 'SALT']
redseasmallvtkDisplay.ColorArray2Component = ''
redseasmallvtkDisplay.VolumeRenderingMode = 'Smart'
redseasmallvtkDisplay.Shade = 0
redseasmallvtkDisplay.GlobalIlluminationReach = 0.0
redseasmallvtkDisplay.VolumetricScatteringBlending = 0.0
redseasmallvtkDisplay.VolumeAnisotropy = 0.0
redseasmallvtkDisplay.BlendMode = 'Composite'
redseasmallvtkDisplay.IsosurfaceValues = []
redseasmallvtkDisplay.SliceFunction = 'Plane'
redseasmallvtkDisplay.UseCropping = 0
redseasmallvtkDisplay.CroppingOrigin = [0.0, 0.0, 0.0]
redseasmallvtkDisplay.CroppingScale = [1.0, 1.0, 1.0]
redseasmallvtkDisplay.SliceMode = 'XY Plane'
redseasmallvtkDisplay.Slice = 24
redseasmallvtkDisplay.SelectInputVectors = [None, '']
redseasmallvtkDisplay.NumberOfSteps = 40
redseasmallvtkDisplay.StepSize = 0.25
redseasmallvtkDisplay.NormalizeVectors = 1
redseasmallvtkDisplay.EnhancedLIC = 1
redseasmallvtkDisplay.ColorMode = 'Blend'
redseasmallvtkDisplay.LICIntensity = 0.8
redseasmallvtkDisplay.MapModeBias = 0.0
redseasmallvtkDisplay.EnhanceContrast = 'Off'
redseasmallvtkDisplay.LowLICContrastEnhancementFactor = 0.0
redseasmallvtkDisplay.HighLICContrastEnhancementFactor = 0.0
redseasmallvtkDisplay.LowColorContrastEnhancementFactor = 0.0
redseasmallvtkDisplay.HighColorContrastEnhancementFactor = 0.0
redseasmallvtkDisplay.AntiAlias = 0
redseasmallvtkDisplay.MaskOnSurface = 1
redseasmallvtkDisplay.MaskThreshold = 0.0
redseasmallvtkDisplay.MaskIntensity = 0.0
redseasmallvtkDisplay.MaskColor = [0.5, 0.5, 0.5]
redseasmallvtkDisplay.GenerateNoiseTexture = 0
redseasmallvtkDisplay.NoiseType = 'Gaussian'
redseasmallvtkDisplay.NoiseTextureSize = 128
redseasmallvtkDisplay.NoiseGrainSize = 2
redseasmallvtkDisplay.MinNoiseValue = 0.0
redseasmallvtkDisplay.MaxNoiseValue = 0.8
redseasmallvtkDisplay.NumberOfNoiseLevels = 1024
redseasmallvtkDisplay.ImpulseNoiseProbability = 1.0
redseasmallvtkDisplay.ImpulseNoiseBackgroundValue = 0.0
redseasmallvtkDisplay.NoiseGeneratorSeed = 1
redseasmallvtkDisplay.CompositeStrategy = 'AUTO'
redseasmallvtkDisplay.UseLICForLOD = 0
redseasmallvtkDisplay.WriteLog = ''

# init the 'Transform2' selected for 'TextureTransform'
redseasmallvtkDisplay.TextureTransform.Translate = [0.0, 0.0, 0.0]
redseasmallvtkDisplay.TextureTransform.Rotate = [0.0, 0.0, 0.0]
redseasmallvtkDisplay.TextureTransform.Scale = [1.0, 1.0, 1.0]

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
redseasmallvtkDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
redseasmallvtkDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
redseasmallvtkDisplay.GlyphType.TipResolution = 6
redseasmallvtkDisplay.GlyphType.TipRadius = 0.1
redseasmallvtkDisplay.GlyphType.TipLength = 0.35
redseasmallvtkDisplay.GlyphType.ShaftResolution = 6
redseasmallvtkDisplay.GlyphType.ShaftRadius = 0.03
redseasmallvtkDisplay.GlyphType.Invert = 0

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
redseasmallvtkDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 40.594237227, 1.0, 0.5, 0.0]
redseasmallvtkDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
redseasmallvtkDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 40.594237227, 1.0, 0.5, 0.0]
redseasmallvtkDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'Grid Axes Representation' selected for 'DataAxesGrid'
redseasmallvtkDisplay.DataAxesGrid.XTitle = 'X Axis'
redseasmallvtkDisplay.DataAxesGrid.YTitle = 'Y Axis'
redseasmallvtkDisplay.DataAxesGrid.ZTitle = 'Z Axis'
redseasmallvtkDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
redseasmallvtkDisplay.DataAxesGrid.XTitleFontFile = ''
redseasmallvtkDisplay.DataAxesGrid.XTitleBold = 0
redseasmallvtkDisplay.DataAxesGrid.XTitleItalic = 0
redseasmallvtkDisplay.DataAxesGrid.XTitleFontSize = 12
redseasmallvtkDisplay.DataAxesGrid.XTitleShadow = 0
redseasmallvtkDisplay.DataAxesGrid.XTitleOpacity = 1.0
redseasmallvtkDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
redseasmallvtkDisplay.DataAxesGrid.YTitleFontFile = ''
redseasmallvtkDisplay.DataAxesGrid.YTitleBold = 0
redseasmallvtkDisplay.DataAxesGrid.YTitleItalic = 0
redseasmallvtkDisplay.DataAxesGrid.YTitleFontSize = 12
redseasmallvtkDisplay.DataAxesGrid.YTitleShadow = 0
redseasmallvtkDisplay.DataAxesGrid.YTitleOpacity = 1.0
redseasmallvtkDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
redseasmallvtkDisplay.DataAxesGrid.ZTitleFontFile = ''
redseasmallvtkDisplay.DataAxesGrid.ZTitleBold = 0
redseasmallvtkDisplay.DataAxesGrid.ZTitleItalic = 0
redseasmallvtkDisplay.DataAxesGrid.ZTitleFontSize = 12
redseasmallvtkDisplay.DataAxesGrid.ZTitleShadow = 0
redseasmallvtkDisplay.DataAxesGrid.ZTitleOpacity = 1.0
redseasmallvtkDisplay.DataAxesGrid.FacesToRender = 63
redseasmallvtkDisplay.DataAxesGrid.CullBackface = 0
redseasmallvtkDisplay.DataAxesGrid.CullFrontface = 1
redseasmallvtkDisplay.DataAxesGrid.ShowGrid = 0
redseasmallvtkDisplay.DataAxesGrid.ShowEdges = 1
redseasmallvtkDisplay.DataAxesGrid.ShowTicks = 1
redseasmallvtkDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
redseasmallvtkDisplay.DataAxesGrid.AxesToLabel = 63
redseasmallvtkDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
redseasmallvtkDisplay.DataAxesGrid.XLabelFontFile = ''
redseasmallvtkDisplay.DataAxesGrid.XLabelBold = 0
redseasmallvtkDisplay.DataAxesGrid.XLabelItalic = 0
redseasmallvtkDisplay.DataAxesGrid.XLabelFontSize = 12
redseasmallvtkDisplay.DataAxesGrid.XLabelShadow = 0
redseasmallvtkDisplay.DataAxesGrid.XLabelOpacity = 1.0
redseasmallvtkDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
redseasmallvtkDisplay.DataAxesGrid.YLabelFontFile = ''
redseasmallvtkDisplay.DataAxesGrid.YLabelBold = 0
redseasmallvtkDisplay.DataAxesGrid.YLabelItalic = 0
redseasmallvtkDisplay.DataAxesGrid.YLabelFontSize = 12
redseasmallvtkDisplay.DataAxesGrid.YLabelShadow = 0
redseasmallvtkDisplay.DataAxesGrid.YLabelOpacity = 1.0
redseasmallvtkDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
redseasmallvtkDisplay.DataAxesGrid.ZLabelFontFile = ''
redseasmallvtkDisplay.DataAxesGrid.ZLabelBold = 0
redseasmallvtkDisplay.DataAxesGrid.ZLabelItalic = 0
redseasmallvtkDisplay.DataAxesGrid.ZLabelFontSize = 12
redseasmallvtkDisplay.DataAxesGrid.ZLabelShadow = 0
redseasmallvtkDisplay.DataAxesGrid.ZLabelOpacity = 1.0
redseasmallvtkDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
redseasmallvtkDisplay.DataAxesGrid.XAxisPrecision = 2
redseasmallvtkDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
redseasmallvtkDisplay.DataAxesGrid.XAxisLabels = []
redseasmallvtkDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
redseasmallvtkDisplay.DataAxesGrid.YAxisPrecision = 2
redseasmallvtkDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
redseasmallvtkDisplay.DataAxesGrid.YAxisLabels = []
redseasmallvtkDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
redseasmallvtkDisplay.DataAxesGrid.ZAxisPrecision = 2
redseasmallvtkDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
redseasmallvtkDisplay.DataAxesGrid.ZAxisLabels = []
redseasmallvtkDisplay.DataAxesGrid.UseCustomBounds = 0
redseasmallvtkDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'Polar Axes Representation' selected for 'PolarAxes'
redseasmallvtkDisplay.PolarAxes.Visibility = 0
redseasmallvtkDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
redseasmallvtkDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
redseasmallvtkDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
redseasmallvtkDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
redseasmallvtkDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
redseasmallvtkDisplay.PolarAxes.EnableCustomRange = 0
redseasmallvtkDisplay.PolarAxes.CustomRange = [0.0, 1.0]
redseasmallvtkDisplay.PolarAxes.AutoPole = 1
redseasmallvtkDisplay.PolarAxes.PolarAxisVisibility = 1
redseasmallvtkDisplay.PolarAxes.RadialAxesVisibility = 1
redseasmallvtkDisplay.PolarAxes.DrawRadialGridlines = 1
redseasmallvtkDisplay.PolarAxes.PolarArcsVisibility = 1
redseasmallvtkDisplay.PolarAxes.DrawPolarArcsGridlines = 1
redseasmallvtkDisplay.PolarAxes.NumberOfRadialAxes = 0
redseasmallvtkDisplay.PolarAxes.DeltaAngleRadialAxes = 45.0
redseasmallvtkDisplay.PolarAxes.NumberOfPolarAxes = 5
redseasmallvtkDisplay.PolarAxes.DeltaRangePolarAxes = 0.0
redseasmallvtkDisplay.PolarAxes.CustomMinRadius = 1
redseasmallvtkDisplay.PolarAxes.MinimumRadius = 0.0
redseasmallvtkDisplay.PolarAxes.CustomMaxRadius = 0
redseasmallvtkDisplay.PolarAxes.MaximumRadius = 1.0
redseasmallvtkDisplay.PolarAxes.CustomAngles = 1
redseasmallvtkDisplay.PolarAxes.MinimumAngle = 0.0
redseasmallvtkDisplay.PolarAxes.MaximumAngle = 90.0
redseasmallvtkDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
redseasmallvtkDisplay.PolarAxes.PolarArcResolutionPerDegree = 0.2
redseasmallvtkDisplay.PolarAxes.Ratio = 1.0
redseasmallvtkDisplay.PolarAxes.EnableOverallColor = 1
redseasmallvtkDisplay.PolarAxes.OverallColor = [1.0, 1.0, 1.0]
redseasmallvtkDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
redseasmallvtkDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
redseasmallvtkDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
redseasmallvtkDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
redseasmallvtkDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
redseasmallvtkDisplay.PolarAxes.PolarAxisTitleVisibility = 1
redseasmallvtkDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
redseasmallvtkDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
redseasmallvtkDisplay.PolarAxes.PolarTitleOffset = [20.0, 20.0]
redseasmallvtkDisplay.PolarAxes.PolarLabelVisibility = 1
redseasmallvtkDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
redseasmallvtkDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
redseasmallvtkDisplay.PolarAxes.PolarLabelOffset = 10.0
redseasmallvtkDisplay.PolarAxes.PolarExponentOffset = 5.0
redseasmallvtkDisplay.PolarAxes.RadialTitleVisibility = 1
redseasmallvtkDisplay.PolarAxes.RadialTitleFormat = '%-#3.1f'
redseasmallvtkDisplay.PolarAxes.RadialTitleLocation = 'Bottom'
redseasmallvtkDisplay.PolarAxes.RadialTitleOffset = [20.0, 0.0]
redseasmallvtkDisplay.PolarAxes.RadialUnitsVisibility = 1
redseasmallvtkDisplay.PolarAxes.ScreenSize = 10.0
redseasmallvtkDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
redseasmallvtkDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
redseasmallvtkDisplay.PolarAxes.PolarAxisTitleFontFile = ''
redseasmallvtkDisplay.PolarAxes.PolarAxisTitleBold = 0
redseasmallvtkDisplay.PolarAxes.PolarAxisTitleItalic = 0
redseasmallvtkDisplay.PolarAxes.PolarAxisTitleShadow = 0
redseasmallvtkDisplay.PolarAxes.PolarAxisTitleFontSize = 12
redseasmallvtkDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
redseasmallvtkDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
redseasmallvtkDisplay.PolarAxes.PolarAxisLabelFontFile = ''
redseasmallvtkDisplay.PolarAxes.PolarAxisLabelBold = 0
redseasmallvtkDisplay.PolarAxes.PolarAxisLabelItalic = 0
redseasmallvtkDisplay.PolarAxes.PolarAxisLabelShadow = 0
redseasmallvtkDisplay.PolarAxes.PolarAxisLabelFontSize = 12
redseasmallvtkDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
redseasmallvtkDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
redseasmallvtkDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
redseasmallvtkDisplay.PolarAxes.LastRadialAxisTextBold = 0
redseasmallvtkDisplay.PolarAxes.LastRadialAxisTextItalic = 0
redseasmallvtkDisplay.PolarAxes.LastRadialAxisTextShadow = 0
redseasmallvtkDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
redseasmallvtkDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
redseasmallvtkDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
redseasmallvtkDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
redseasmallvtkDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
redseasmallvtkDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
redseasmallvtkDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
redseasmallvtkDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
redseasmallvtkDisplay.PolarAxes.EnableDistanceLOD = 1
redseasmallvtkDisplay.PolarAxes.DistanceLODThreshold = 0.7
redseasmallvtkDisplay.PolarAxes.EnableViewAngleLOD = 1
redseasmallvtkDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
redseasmallvtkDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
redseasmallvtkDisplay.PolarAxes.PolarTicksVisibility = 1
redseasmallvtkDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
redseasmallvtkDisplay.PolarAxes.TickLocation = 'Both'
redseasmallvtkDisplay.PolarAxes.AxisTickVisibility = 1
redseasmallvtkDisplay.PolarAxes.AxisMinorTickVisibility = 0
redseasmallvtkDisplay.PolarAxes.AxisTickMatchesPolarAxes = 1
redseasmallvtkDisplay.PolarAxes.DeltaRangeMajor = 1.0
redseasmallvtkDisplay.PolarAxes.DeltaRangeMinor = 0.5
redseasmallvtkDisplay.PolarAxes.ArcTickVisibility = 1
redseasmallvtkDisplay.PolarAxes.ArcMinorTickVisibility = 0
redseasmallvtkDisplay.PolarAxes.ArcTickMatchesRadialAxes = 1
redseasmallvtkDisplay.PolarAxes.DeltaAngleMajor = 10.0
redseasmallvtkDisplay.PolarAxes.DeltaAngleMinor = 5.0
redseasmallvtkDisplay.PolarAxes.TickRatioRadiusSize = 0.02
redseasmallvtkDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
redseasmallvtkDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
redseasmallvtkDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
redseasmallvtkDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
redseasmallvtkDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
redseasmallvtkDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
redseasmallvtkDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
redseasmallvtkDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
redseasmallvtkDisplay.PolarAxes.ArcMajorTickSize = 0.0
redseasmallvtkDisplay.PolarAxes.ArcTickRatioSize = 0.3
redseasmallvtkDisplay.PolarAxes.ArcMajorTickThickness = 1.0
redseasmallvtkDisplay.PolarAxes.ArcTickRatioThickness = 0.5
redseasmallvtkDisplay.PolarAxes.Use2DMode = 0
redseasmallvtkDisplay.PolarAxes.UseLogAxis = 0

# init the 'Plane' selected for 'SliceFunction'
redseasmallvtkDisplay.SliceFunction.Origin = [45.9871, 14.0271, -10.2]
redseasmallvtkDisplay.SliceFunction.Normal = [1.0, 0.0, 0.0]
redseasmallvtkDisplay.SliceFunction.Offset = 0.0

# get the material library
materialLibrary1 = GetMaterialLibrary()

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# hide data in view
Hide(redseasmallvtk, renderView1)

# show data in view
redseasmallvtkDisplay = Show(redseasmallvtk, renderView1, 'UniformGridRepresentation')

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# show data in view
redseasmallvtkDisplay = Show(redseasmallvtk, renderView1, 'UniformGridRepresentation')

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [45.987098693847656, 14.027099609375, 33.519642501647844]
renderView1.CameraFocalPoint = [45.987098693847656, 14.027099609375, -10.200000002980232]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [64.27922131244884, 40.249553420596214, 19.619260667883363]
renderView1.CameraFocalPoint = [45.98709869384767, 14.027099609375, -10.20000000298021]
renderView1.CameraViewUp = [-0.465635602343102, 0.7863988124518927, -0.40590687799645586]
renderView1.CameraParallelScale = 11.315476125271417

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=redseasmallvtk)
calculator1.AttributeType = 'Point Data'
calculator1.CoordinateResults = 0
calculator1.ResultNormals = 0
calculator1.ResultTCoords = 0
calculator1.ResultArrayName = 'Result'
calculator1.Function = ''
calculator1.ReplaceInvalidResults = 1
calculator1.ReplacementValue = 0.0
calculator1.ResultArrayType = 'Double'
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [64.27922131244884, 40.249553420596214, 19.619260667883363]
renderView1.CameraFocalPoint = [45.98709869384767, 14.027099609375, -10.20000000298021]
renderView1.CameraViewUp = [-0.465635602343102, 0.7863988124518927, -0.40590687799645586]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on calculator1
calculator1.Function = 'iHatU+jHat*V+kHat*W'

# show data in view
calculator1Display = Show(calculator1, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
calculator1Display.Selection = None
calculator1Display.Representation = 'Outline'
calculator1Display.ColorArrayName = [None, '']
calculator1Display.LookupTable = None
calculator1Display.MapScalars = 1
calculator1Display.MultiComponentsMapping = 0
calculator1Display.InterpolateScalarsBeforeMapping = 1
calculator1Display.UseNanColorForMissingArrays = 0
calculator1Display.Opacity = 1.0
calculator1Display.PointSize = 2.0
calculator1Display.LineWidth = 1.0
calculator1Display.RenderLinesAsTubes = 0
calculator1Display.RenderPointsAsSpheres = 0
calculator1Display.DisableLighting = 0
calculator1Display.Diffuse = 1.0
calculator1Display.Interpolation = 'Gouraud'
calculator1Display.Specular = 0.0
calculator1Display.SpecularColor = [1.0, 1.0, 1.0]
calculator1Display.SpecularPower = 100.0
calculator1Display.Luminosity = 0.0
calculator1Display.Ambient = 0.0
calculator1Display.Roughness = 0.3
calculator1Display.Metallic = 0.0
calculator1Display.EdgeTint = [1.0, 1.0, 1.0]
calculator1Display.Anisotropy = 0.0
calculator1Display.AnisotropyRotation = 0.0
calculator1Display.BaseIOR = 1.5
calculator1Display.CoatStrength = 0.0
calculator1Display.CoatIOR = 2.0
calculator1Display.CoatRoughness = 0.0
calculator1Display.CoatColor = [1.0, 1.0, 1.0]
calculator1Display.SelectNormalArray = 'None'
calculator1Display.SelectTangentArray = 'None'
calculator1Display.ComputePointNormals = 0
calculator1Display.Splitting = 1
calculator1Display.FeatureAngle = 30.0
calculator1Display.SelectTCoordArray = 'None'
calculator1Display.Texture = None
calculator1Display.RepeatTextures = 1
calculator1Display.InterpolateTextures = 0
calculator1Display.SeamlessU = 0
calculator1Display.SeamlessV = 0
calculator1Display.UseMipmapTextures = 0
calculator1Display.ShowTexturesOnBackface = 1
calculator1Display.BaseColorTexture = None
calculator1Display.NormalTexture = None
calculator1Display.NormalScale = 1.0
calculator1Display.CoatNormalTexture = None
calculator1Display.CoatNormalScale = 1.0
calculator1Display.MaterialTexture = None
calculator1Display.OcclusionStrength = 1.0
calculator1Display.AnisotropyTexture = None
calculator1Display.EmissiveTexture = None
calculator1Display.EmissiveFactor = [1.0, 1.0, 1.0]
calculator1Display.TextureTransform = 'Transform2'
calculator1Display.EdgeOpacity = 1.0
calculator1Display.BackfaceRepresentation = 'Follow Frontface'
calculator1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
calculator1Display.BackfaceOpacity = 1.0
calculator1Display.Translation = [0.0, 0.0, 0.0]
calculator1Display.Scale = [1.0, 1.0, 1.0]
calculator1Display.Orientation = [0.0, 0.0, 0.0]
calculator1Display.Origin = [0.0, 0.0, 0.0]
calculator1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
calculator1Display.Pickable = 1
calculator1Display.Triangulate = 0
calculator1Display.UseShaderReplacements = 0
calculator1Display.ShaderReplacements = ''
calculator1Display.NonlinearSubdivisionLevel = 1
calculator1Display.MatchBoundariesIgnoringCellOrder = 0
calculator1Display.UseDataPartitions = 0
calculator1Display.OSPRayUseScaleArray = 'All Approximate'
calculator1Display.OSPRayScaleArray = 'SALT'
calculator1Display.OSPRayScaleFunction = 'Piecewise Function'
calculator1Display.OSPRayMaterial = 'None'
calculator1Display.Assembly = ''
calculator1Display.SelectedBlockSelectors = ['']
calculator1Display.BlockSelectors = ['/']
calculator1Display.BlockColors = []
calculator1Display.BlockColorArrayNames = []
calculator1Display.BlockLookupTables = []
calculator1Display.BlockUseSeparateColorMaps = []
calculator1Display.BlockMapScalars = []
calculator1Display.BlockInterpolateScalarsBeforeMappings = []
calculator1Display.BlockOpacities = []
calculator1Display.BlockMapScalarsGUI = 1
calculator1Display.BlockInterpolateScalarsBeforeMappingsGUI = 1
calculator1Display.BlockOpacitiesGUI = 1.0
calculator1Display.Orient = 0
calculator1Display.OrientationMode = 'Direction'
calculator1Display.SelectOrientationVectors = 'None'
calculator1Display.Scaling = 0
calculator1Display.ScaleMode = 'No Data Scaling Off'
calculator1Display.ScaleFactor = 1.9600000000000002
calculator1Display.SelectScaleArray = 'None'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.UseGlyphTable = 0
calculator1Display.GlyphTableIndexArray = 'None'
calculator1Display.UseCompositeGlyphTable = 0
calculator1Display.UseGlyphCullingAndLOD = 0
calculator1Display.LODValues = []
calculator1Display.ColorByLODIndex = 0
calculator1Display.GaussianRadius = 0.098
calculator1Display.ShaderPreset = 'Sphere'
calculator1Display.CustomTriangleScale = 3
calculator1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
calculator1Display.Emissive = 0
calculator1Display.ScaleByArray = 0
calculator1Display.SetScaleArray = ['POINTS', 'SALT']
calculator1Display.ScaleArrayComponent = ''
calculator1Display.UseScaleFunction = 1
calculator1Display.ScaleTransferFunction = 'Piecewise Function'
calculator1Display.OpacityByArray = 0
calculator1Display.OpacityArray = ['POINTS', 'SALT']
calculator1Display.OpacityArrayComponent = ''
calculator1Display.OpacityTransferFunction = 'Piecewise Function'
calculator1Display.DataAxesGrid = 'Grid Axes Representation'
calculator1Display.SelectionCellLabelBold = 0
calculator1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
calculator1Display.SelectionCellLabelFontFamily = 'Arial'
calculator1Display.SelectionCellLabelFontFile = ''
calculator1Display.SelectionCellLabelFontSize = 18
calculator1Display.SelectionCellLabelItalic = 0
calculator1Display.SelectionCellLabelJustification = 'Left'
calculator1Display.SelectionCellLabelOpacity = 1.0
calculator1Display.SelectionCellLabelShadow = 0
calculator1Display.SelectionPointLabelBold = 0
calculator1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
calculator1Display.SelectionPointLabelFontFamily = 'Arial'
calculator1Display.SelectionPointLabelFontFile = ''
calculator1Display.SelectionPointLabelFontSize = 18
calculator1Display.SelectionPointLabelItalic = 0
calculator1Display.SelectionPointLabelJustification = 'Left'
calculator1Display.SelectionPointLabelOpacity = 1.0
calculator1Display.SelectionPointLabelShadow = 0
calculator1Display.PolarAxes = 'Polar Axes Representation'
calculator1Display.ScalarOpacityUnitDistance = 0.1808356859802089
calculator1Display.ScalarOpacityFunction = None
calculator1Display.TransferFunction2D = None
calculator1Display.UseSeparateOpacityArray = 0
calculator1Display.OpacityArrayName = ['POINTS', 'SALT']
calculator1Display.OpacityComponent = ''
calculator1Display.UseTransfer2D = 0
calculator1Display.UseGradientForTransfer2D = 1
calculator1Display.ColorArray2Name = ['POINTS', 'SALT']
calculator1Display.ColorArray2Component = ''
calculator1Display.VolumeRenderingMode = 'Smart'
calculator1Display.Shade = 0
calculator1Display.GlobalIlluminationReach = 0.0
calculator1Display.VolumetricScatteringBlending = 0.0
calculator1Display.VolumeAnisotropy = 0.0
calculator1Display.BlendMode = 'Composite'
calculator1Display.IsosurfaceValues = []
calculator1Display.SliceFunction = 'Plane'
calculator1Display.UseCropping = 0
calculator1Display.CroppingOrigin = [0.0, 0.0, 0.0]
calculator1Display.CroppingScale = [1.0, 1.0, 1.0]
calculator1Display.SliceMode = 'XY Plane'
calculator1Display.Slice = 24
calculator1Display.SelectInputVectors = [None, '']
calculator1Display.NumberOfSteps = 40
calculator1Display.StepSize = 0.25
calculator1Display.NormalizeVectors = 1
calculator1Display.EnhancedLIC = 1
calculator1Display.ColorMode = 'Blend'
calculator1Display.LICIntensity = 0.8
calculator1Display.MapModeBias = 0.0
calculator1Display.EnhanceContrast = 'Off'
calculator1Display.LowLICContrastEnhancementFactor = 0.0
calculator1Display.HighLICContrastEnhancementFactor = 0.0
calculator1Display.LowColorContrastEnhancementFactor = 0.0
calculator1Display.HighColorContrastEnhancementFactor = 0.0
calculator1Display.AntiAlias = 0
calculator1Display.MaskOnSurface = 1
calculator1Display.MaskThreshold = 0.0
calculator1Display.MaskIntensity = 0.0
calculator1Display.MaskColor = [0.5, 0.5, 0.5]
calculator1Display.GenerateNoiseTexture = 0
calculator1Display.NoiseType = 'Gaussian'
calculator1Display.NoiseTextureSize = 128
calculator1Display.NoiseGrainSize = 2
calculator1Display.MinNoiseValue = 0.0
calculator1Display.MaxNoiseValue = 0.8
calculator1Display.NumberOfNoiseLevels = 1024
calculator1Display.ImpulseNoiseProbability = 1.0
calculator1Display.ImpulseNoiseBackgroundValue = 0.0
calculator1Display.NoiseGeneratorSeed = 1
calculator1Display.CompositeStrategy = 'AUTO'
calculator1Display.UseLICForLOD = 0
calculator1Display.WriteLog = ''

# init the 'Transform2' selected for 'TextureTransform'
calculator1Display.TextureTransform.Translate = [0.0, 0.0, 0.0]
calculator1Display.TextureTransform.Rotate = [0.0, 0.0, 0.0]
calculator1Display.TextureTransform.Scale = [1.0, 1.0, 1.0]

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
calculator1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
calculator1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
calculator1Display.GlyphType.TipResolution = 6
calculator1Display.GlyphType.TipRadius = 0.1
calculator1Display.GlyphType.TipLength = 0.35
calculator1Display.GlyphType.ShaftResolution = 6
calculator1Display.GlyphType.ShaftRadius = 0.03
calculator1Display.GlyphType.Invert = 0

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 40.594237227, 1.0, 0.5, 0.0]
calculator1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 40.594237227, 1.0, 0.5, 0.0]
calculator1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'Grid Axes Representation' selected for 'DataAxesGrid'
calculator1Display.DataAxesGrid.XTitle = 'X Axis'
calculator1Display.DataAxesGrid.YTitle = 'Y Axis'
calculator1Display.DataAxesGrid.ZTitle = 'Z Axis'
calculator1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
calculator1Display.DataAxesGrid.XTitleFontFile = ''
calculator1Display.DataAxesGrid.XTitleBold = 0
calculator1Display.DataAxesGrid.XTitleItalic = 0
calculator1Display.DataAxesGrid.XTitleFontSize = 12
calculator1Display.DataAxesGrid.XTitleShadow = 0
calculator1Display.DataAxesGrid.XTitleOpacity = 1.0
calculator1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
calculator1Display.DataAxesGrid.YTitleFontFile = ''
calculator1Display.DataAxesGrid.YTitleBold = 0
calculator1Display.DataAxesGrid.YTitleItalic = 0
calculator1Display.DataAxesGrid.YTitleFontSize = 12
calculator1Display.DataAxesGrid.YTitleShadow = 0
calculator1Display.DataAxesGrid.YTitleOpacity = 1.0
calculator1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
calculator1Display.DataAxesGrid.ZTitleFontFile = ''
calculator1Display.DataAxesGrid.ZTitleBold = 0
calculator1Display.DataAxesGrid.ZTitleItalic = 0
calculator1Display.DataAxesGrid.ZTitleFontSize = 12
calculator1Display.DataAxesGrid.ZTitleShadow = 0
calculator1Display.DataAxesGrid.ZTitleOpacity = 1.0
calculator1Display.DataAxesGrid.FacesToRender = 63
calculator1Display.DataAxesGrid.CullBackface = 0
calculator1Display.DataAxesGrid.CullFrontface = 1
calculator1Display.DataAxesGrid.ShowGrid = 0
calculator1Display.DataAxesGrid.ShowEdges = 1
calculator1Display.DataAxesGrid.ShowTicks = 1
calculator1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
calculator1Display.DataAxesGrid.AxesToLabel = 63
calculator1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
calculator1Display.DataAxesGrid.XLabelFontFile = ''
calculator1Display.DataAxesGrid.XLabelBold = 0
calculator1Display.DataAxesGrid.XLabelItalic = 0
calculator1Display.DataAxesGrid.XLabelFontSize = 12
calculator1Display.DataAxesGrid.XLabelShadow = 0
calculator1Display.DataAxesGrid.XLabelOpacity = 1.0
calculator1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
calculator1Display.DataAxesGrid.YLabelFontFile = ''
calculator1Display.DataAxesGrid.YLabelBold = 0
calculator1Display.DataAxesGrid.YLabelItalic = 0
calculator1Display.DataAxesGrid.YLabelFontSize = 12
calculator1Display.DataAxesGrid.YLabelShadow = 0
calculator1Display.DataAxesGrid.YLabelOpacity = 1.0
calculator1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
calculator1Display.DataAxesGrid.ZLabelFontFile = ''
calculator1Display.DataAxesGrid.ZLabelBold = 0
calculator1Display.DataAxesGrid.ZLabelItalic = 0
calculator1Display.DataAxesGrid.ZLabelFontSize = 12
calculator1Display.DataAxesGrid.ZLabelShadow = 0
calculator1Display.DataAxesGrid.ZLabelOpacity = 1.0
calculator1Display.DataAxesGrid.XAxisNotation = 'Mixed'
calculator1Display.DataAxesGrid.XAxisPrecision = 2
calculator1Display.DataAxesGrid.XAxisUseCustomLabels = 0
calculator1Display.DataAxesGrid.XAxisLabels = []
calculator1Display.DataAxesGrid.YAxisNotation = 'Mixed'
calculator1Display.DataAxesGrid.YAxisPrecision = 2
calculator1Display.DataAxesGrid.YAxisUseCustomLabels = 0
calculator1Display.DataAxesGrid.YAxisLabels = []
calculator1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
calculator1Display.DataAxesGrid.ZAxisPrecision = 2
calculator1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
calculator1Display.DataAxesGrid.ZAxisLabels = []
calculator1Display.DataAxesGrid.UseCustomBounds = 0
calculator1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'Polar Axes Representation' selected for 'PolarAxes'
calculator1Display.PolarAxes.Visibility = 0
calculator1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
calculator1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
calculator1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
calculator1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
calculator1Display.PolarAxes.EnableCustomRange = 0
calculator1Display.PolarAxes.CustomRange = [0.0, 1.0]
calculator1Display.PolarAxes.AutoPole = 1
calculator1Display.PolarAxes.PolarAxisVisibility = 1
calculator1Display.PolarAxes.RadialAxesVisibility = 1
calculator1Display.PolarAxes.DrawRadialGridlines = 1
calculator1Display.PolarAxes.PolarArcsVisibility = 1
calculator1Display.PolarAxes.DrawPolarArcsGridlines = 1
calculator1Display.PolarAxes.NumberOfRadialAxes = 0
calculator1Display.PolarAxes.DeltaAngleRadialAxes = 45.0
calculator1Display.PolarAxes.NumberOfPolarAxes = 5
calculator1Display.PolarAxes.DeltaRangePolarAxes = 0.0
calculator1Display.PolarAxes.CustomMinRadius = 1
calculator1Display.PolarAxes.MinimumRadius = 0.0
calculator1Display.PolarAxes.CustomMaxRadius = 0
calculator1Display.PolarAxes.MaximumRadius = 1.0
calculator1Display.PolarAxes.CustomAngles = 1
calculator1Display.PolarAxes.MinimumAngle = 0.0
calculator1Display.PolarAxes.MaximumAngle = 90.0
calculator1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
calculator1Display.PolarAxes.PolarArcResolutionPerDegree = 0.2
calculator1Display.PolarAxes.Ratio = 1.0
calculator1Display.PolarAxes.EnableOverallColor = 1
calculator1Display.PolarAxes.OverallColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.PolarAxisTitleVisibility = 1
calculator1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
calculator1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
calculator1Display.PolarAxes.PolarTitleOffset = [20.0, 20.0]
calculator1Display.PolarAxes.PolarLabelVisibility = 1
calculator1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
calculator1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
calculator1Display.PolarAxes.PolarLabelOffset = 10.0
calculator1Display.PolarAxes.PolarExponentOffset = 5.0
calculator1Display.PolarAxes.RadialTitleVisibility = 1
calculator1Display.PolarAxes.RadialTitleFormat = '%-#3.1f'
calculator1Display.PolarAxes.RadialTitleLocation = 'Bottom'
calculator1Display.PolarAxes.RadialTitleOffset = [20.0, 0.0]
calculator1Display.PolarAxes.RadialUnitsVisibility = 1
calculator1Display.PolarAxes.ScreenSize = 10.0
calculator1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
calculator1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
calculator1Display.PolarAxes.PolarAxisTitleFontFile = ''
calculator1Display.PolarAxes.PolarAxisTitleBold = 0
calculator1Display.PolarAxes.PolarAxisTitleItalic = 0
calculator1Display.PolarAxes.PolarAxisTitleShadow = 0
calculator1Display.PolarAxes.PolarAxisTitleFontSize = 12
calculator1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
calculator1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
calculator1Display.PolarAxes.PolarAxisLabelFontFile = ''
calculator1Display.PolarAxes.PolarAxisLabelBold = 0
calculator1Display.PolarAxes.PolarAxisLabelItalic = 0
calculator1Display.PolarAxes.PolarAxisLabelShadow = 0
calculator1Display.PolarAxes.PolarAxisLabelFontSize = 12
calculator1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
calculator1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
calculator1Display.PolarAxes.LastRadialAxisTextFontFile = ''
calculator1Display.PolarAxes.LastRadialAxisTextBold = 0
calculator1Display.PolarAxes.LastRadialAxisTextItalic = 0
calculator1Display.PolarAxes.LastRadialAxisTextShadow = 0
calculator1Display.PolarAxes.LastRadialAxisTextFontSize = 12
calculator1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
calculator1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
calculator1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
calculator1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
calculator1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
calculator1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
calculator1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
calculator1Display.PolarAxes.EnableDistanceLOD = 1
calculator1Display.PolarAxes.DistanceLODThreshold = 0.7
calculator1Display.PolarAxes.EnableViewAngleLOD = 1
calculator1Display.PolarAxes.ViewAngleLODThreshold = 0.7
calculator1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
calculator1Display.PolarAxes.PolarTicksVisibility = 1
calculator1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
calculator1Display.PolarAxes.TickLocation = 'Both'
calculator1Display.PolarAxes.AxisTickVisibility = 1
calculator1Display.PolarAxes.AxisMinorTickVisibility = 0
calculator1Display.PolarAxes.AxisTickMatchesPolarAxes = 1
calculator1Display.PolarAxes.DeltaRangeMajor = 1.0
calculator1Display.PolarAxes.DeltaRangeMinor = 0.5
calculator1Display.PolarAxes.ArcTickVisibility = 1
calculator1Display.PolarAxes.ArcMinorTickVisibility = 0
calculator1Display.PolarAxes.ArcTickMatchesRadialAxes = 1
calculator1Display.PolarAxes.DeltaAngleMajor = 10.0
calculator1Display.PolarAxes.DeltaAngleMinor = 5.0
calculator1Display.PolarAxes.TickRatioRadiusSize = 0.02
calculator1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
calculator1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
calculator1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
calculator1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
calculator1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
calculator1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
calculator1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
calculator1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
calculator1Display.PolarAxes.ArcMajorTickSize = 0.0
calculator1Display.PolarAxes.ArcTickRatioSize = 0.3
calculator1Display.PolarAxes.ArcMajorTickThickness = 1.0
calculator1Display.PolarAxes.ArcTickRatioThickness = 0.5
calculator1Display.PolarAxes.Use2DMode = 0
calculator1Display.PolarAxes.UseLogAxis = 0

# init the 'Plane' selected for 'SliceFunction'
calculator1Display.SliceFunction.Origin = [45.9871, 14.0271, -10.2]
calculator1Display.SliceFunction.Normal = [1.0, 0.0, 0.0]
calculator1Display.SliceFunction.Offset = 0.0

# hide data in view
Hide(redseasmallvtk, renderView1)

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [64.27922131244884, 40.249553420596214, 19.619260667883363]
renderView1.CameraFocalPoint = [45.98709869384767, 14.027099609375, -10.20000000298021]
renderView1.CameraViewUp = [-0.465635602343102, 0.7863988124518927, -0.40590687799645586]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [64.27922131244884, 40.249553420596214, 19.619260667883363]
renderView1.CameraFocalPoint = [45.98709869384767, 14.027099609375, -10.20000000298021]
renderView1.CameraViewUp = [-0.465635602343102, 0.7863988124518927, -0.40590687799645586]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on calculator1
calculator1.Function = 'iHat*U+jHat*V+kHat*W'

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [64.27922131244884, 40.249553420596214, 19.619260667883363]
renderView1.CameraFocalPoint = [45.98709869384767, 14.027099609375, -10.20000000298021]
renderView1.CameraViewUp = [-0.465635602343102, 0.7863988124518927, -0.40590687799645586]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [62.17978470675151, 45.498054206333805, -35.866769904472804]
renderView1.CameraFocalPoint = [45.987098693847635, 14.02709960937499, -10.200000002980234]
renderView1.CameraViewUp = [-0.919563537338946, 0.19484250355003593, -0.34123203191822293]
renderView1.CameraParallelScale = 11.315476125271417

# create a new 'Glyph'
glyph1 = Glyph(registrationName='Glyph1', Input=calculator1,
    GlyphType='Arrow')
glyph1.OrientationArray = ['POINTS', 'Result']
glyph1.ScaleArray = ['POINTS', 'No scale array']
glyph1.VectorScaleMode = 'Scale by Magnitude'
glyph1.ScaleFactor = 1.9600000000000002
glyph1.GlyphTransform = 'Transform2'
glyph1.GlyphMode = 'Uniform Spatial Distribution (Bounds Based)'
glyph1.MaximumNumberOfSamplePoints = 5000
glyph1.Seed = 10339
glyph1.Stride = 1

# init the 'Arrow' selected for 'GlyphType'
glyph1.GlyphType.TipResolution = 6
glyph1.GlyphType.TipRadius = 0.1
glyph1.GlyphType.TipLength = 0.35
glyph1.GlyphType.ShaftResolution = 6
glyph1.GlyphType.ShaftRadius = 0.03
glyph1.GlyphType.Invert = 0

# init the 'Transform2' selected for 'GlyphTransform'
glyph1.GlyphTransform.Translate = [0.0, 0.0, 0.0]
glyph1.GlyphTransform.Rotate = [0.0, 0.0, 0.0]
glyph1.GlyphTransform.Scale = [1.0, 1.0, 1.0]
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [62.17978470675151, 45.498054206333805, -35.866769904472804]
renderView1.CameraFocalPoint = [45.987098693847635, 14.02709960937499, -10.200000002980234]
renderView1.CameraViewUp = [-0.919563537338946, 0.19484250355003593, -0.34123203191822293]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [48.69277577421068, -19.16669879176132, -38.524162832162425]
renderView1.CameraFocalPoint = [45.987098693847635, 14.027099609375012, -10.200000002980214]
renderView1.CameraViewUp = [-0.969712958055637, -0.19940193992708477, 0.14105192424175564]
renderView1.CameraParallelScale = 11.315476125271417

# set active source
SetActiveSource(calculator1)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=calculator1Display.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=calculator1Display)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=calculator1Display.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=calculator1Display)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [48.69277577421068, -19.16669879176132, -38.524162832162425]
renderView1.CameraFocalPoint = [45.987098693847635, 14.027099609375012, -10.200000002980214]
renderView1.CameraViewUp = [-0.969712958055637, -0.19940193992708477, 0.14105192424175564]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [48.69277577421068, -19.16669879176132, -38.524162832162425]
renderView1.CameraFocalPoint = [45.987098693847635, 14.027099609375012, -10.200000002980214]
renderView1.CameraViewUp = [-0.969712958055637, -0.19940193992708477, 0.14105192424175564]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on calculator1
calculator1.ResultArrayName = 'velocity'

# Properties modified on glyph1
glyph1.ScaleArray = ['POINTS', 'Result']

# show data in view
glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
glyph1Display.Selection = None
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = [None, '']
glyph1Display.LookupTable = None
glyph1Display.MapScalars = 1
glyph1Display.MultiComponentsMapping = 0
glyph1Display.InterpolateScalarsBeforeMapping = 1
glyph1Display.UseNanColorForMissingArrays = 0
glyph1Display.Opacity = 1.0
glyph1Display.PointSize = 2.0
glyph1Display.LineWidth = 1.0
glyph1Display.RenderLinesAsTubes = 0
glyph1Display.RenderPointsAsSpheres = 0
glyph1Display.DisableLighting = 0
glyph1Display.Diffuse = 1.0
glyph1Display.Interpolation = 'Gouraud'
glyph1Display.Specular = 0.0
glyph1Display.SpecularColor = [1.0, 1.0, 1.0]
glyph1Display.SpecularPower = 100.0
glyph1Display.Luminosity = 0.0
glyph1Display.Ambient = 0.0
glyph1Display.Roughness = 0.3
glyph1Display.Metallic = 0.0
glyph1Display.EdgeTint = [1.0, 1.0, 1.0]
glyph1Display.Anisotropy = 0.0
glyph1Display.AnisotropyRotation = 0.0
glyph1Display.BaseIOR = 1.5
glyph1Display.CoatStrength = 0.0
glyph1Display.CoatIOR = 2.0
glyph1Display.CoatRoughness = 0.0
glyph1Display.CoatColor = [1.0, 1.0, 1.0]
glyph1Display.SelectNormalArray = 'None'
glyph1Display.SelectTangentArray = 'None'
glyph1Display.ComputePointNormals = 0
glyph1Display.Splitting = 1
glyph1Display.FeatureAngle = 30.0
glyph1Display.SelectTCoordArray = 'None'
glyph1Display.Texture = None
glyph1Display.RepeatTextures = 1
glyph1Display.InterpolateTextures = 0
glyph1Display.SeamlessU = 0
glyph1Display.SeamlessV = 0
glyph1Display.UseMipmapTextures = 0
glyph1Display.ShowTexturesOnBackface = 1
glyph1Display.BaseColorTexture = None
glyph1Display.NormalTexture = None
glyph1Display.NormalScale = 1.0
glyph1Display.CoatNormalTexture = None
glyph1Display.CoatNormalScale = 1.0
glyph1Display.MaterialTexture = None
glyph1Display.OcclusionStrength = 1.0
glyph1Display.AnisotropyTexture = None
glyph1Display.EmissiveTexture = None
glyph1Display.EmissiveFactor = [1.0, 1.0, 1.0]
glyph1Display.TextureTransform = 'Transform2'
glyph1Display.EdgeOpacity = 1.0
glyph1Display.BackfaceRepresentation = 'Follow Frontface'
glyph1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
glyph1Display.BackfaceOpacity = 1.0
glyph1Display.Translation = [0.0, 0.0, 0.0]
glyph1Display.Scale = [1.0, 1.0, 1.0]
glyph1Display.Orientation = [0.0, 0.0, 0.0]
glyph1Display.Origin = [0.0, 0.0, 0.0]
glyph1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
glyph1Display.Pickable = 1
glyph1Display.Triangulate = 0
glyph1Display.UseShaderReplacements = 0
glyph1Display.ShaderReplacements = ''
glyph1Display.NonlinearSubdivisionLevel = 1
glyph1Display.MatchBoundariesIgnoringCellOrder = 0
glyph1Display.UseDataPartitions = 0
glyph1Display.OSPRayUseScaleArray = 'All Approximate'
glyph1Display.OSPRayScaleArray = 'SALT'
glyph1Display.OSPRayScaleFunction = 'Piecewise Function'
glyph1Display.OSPRayMaterial = 'None'
glyph1Display.Assembly = ''
glyph1Display.SelectedBlockSelectors = ['']
glyph1Display.BlockSelectors = ['/']
glyph1Display.BlockColors = []
glyph1Display.BlockColorArrayNames = []
glyph1Display.BlockLookupTables = []
glyph1Display.BlockUseSeparateColorMaps = []
glyph1Display.BlockMapScalars = []
glyph1Display.BlockInterpolateScalarsBeforeMappings = []
glyph1Display.BlockOpacities = []
glyph1Display.BlockMapScalarsGUI = 1
glyph1Display.BlockInterpolateScalarsBeforeMappingsGUI = 1
glyph1Display.BlockOpacitiesGUI = 1.0
glyph1Display.Orient = 0
glyph1Display.OrientationMode = 'Direction'
glyph1Display.SelectOrientationVectors = 'velocity'
glyph1Display.Scaling = 0
glyph1Display.ScaleMode = 'No Data Scaling Off'
glyph1Display.ScaleFactor = 1.9939481645822525
glyph1Display.SelectScaleArray = 'None'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.UseGlyphTable = 0
glyph1Display.GlyphTableIndexArray = 'None'
glyph1Display.UseCompositeGlyphTable = 0
glyph1Display.UseGlyphCullingAndLOD = 0
glyph1Display.LODValues = []
glyph1Display.ColorByLODIndex = 0
glyph1Display.GaussianRadius = 0.09969740822911263
glyph1Display.ShaderPreset = 'Sphere'
glyph1Display.CustomTriangleScale = 3
glyph1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
glyph1Display.Emissive = 0
glyph1Display.ScaleByArray = 0
glyph1Display.SetScaleArray = ['POINTS', 'SALT']
glyph1Display.ScaleArrayComponent = ''
glyph1Display.UseScaleFunction = 1
glyph1Display.ScaleTransferFunction = 'Piecewise Function'
glyph1Display.OpacityByArray = 0
glyph1Display.OpacityArray = ['POINTS', 'SALT']
glyph1Display.OpacityArrayComponent = ''
glyph1Display.OpacityTransferFunction = 'Piecewise Function'
glyph1Display.DataAxesGrid = 'Grid Axes Representation'
glyph1Display.SelectionCellLabelBold = 0
glyph1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
glyph1Display.SelectionCellLabelFontFamily = 'Arial'
glyph1Display.SelectionCellLabelFontFile = ''
glyph1Display.SelectionCellLabelFontSize = 18
glyph1Display.SelectionCellLabelItalic = 0
glyph1Display.SelectionCellLabelJustification = 'Left'
glyph1Display.SelectionCellLabelOpacity = 1.0
glyph1Display.SelectionCellLabelShadow = 0
glyph1Display.SelectionPointLabelBold = 0
glyph1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
glyph1Display.SelectionPointLabelFontFamily = 'Arial'
glyph1Display.SelectionPointLabelFontFile = ''
glyph1Display.SelectionPointLabelFontSize = 18
glyph1Display.SelectionPointLabelItalic = 0
glyph1Display.SelectionPointLabelJustification = 'Left'
glyph1Display.SelectionPointLabelOpacity = 1.0
glyph1Display.SelectionPointLabelShadow = 0
glyph1Display.PolarAxes = 'Polar Axes Representation'
glyph1Display.SelectInputVectors = ['POINTS', 'velocity']
glyph1Display.NumberOfSteps = 40
glyph1Display.StepSize = 0.25
glyph1Display.NormalizeVectors = 1
glyph1Display.EnhancedLIC = 1
glyph1Display.ColorMode = 'Blend'
glyph1Display.LICIntensity = 0.8
glyph1Display.MapModeBias = 0.0
glyph1Display.EnhanceContrast = 'Off'
glyph1Display.LowLICContrastEnhancementFactor = 0.0
glyph1Display.HighLICContrastEnhancementFactor = 0.0
glyph1Display.LowColorContrastEnhancementFactor = 0.0
glyph1Display.HighColorContrastEnhancementFactor = 0.0
glyph1Display.AntiAlias = 0
glyph1Display.MaskOnSurface = 1
glyph1Display.MaskThreshold = 0.0
glyph1Display.MaskIntensity = 0.0
glyph1Display.MaskColor = [0.5, 0.5, 0.5]
glyph1Display.GenerateNoiseTexture = 0
glyph1Display.NoiseType = 'Gaussian'
glyph1Display.NoiseTextureSize = 128
glyph1Display.NoiseGrainSize = 2
glyph1Display.MinNoiseValue = 0.0
glyph1Display.MaxNoiseValue = 0.8
glyph1Display.NumberOfNoiseLevels = 1024
glyph1Display.ImpulseNoiseProbability = 1.0
glyph1Display.ImpulseNoiseBackgroundValue = 0.0
glyph1Display.NoiseGeneratorSeed = 1
glyph1Display.CompositeStrategy = 'AUTO'
glyph1Display.UseLICForLOD = 0
glyph1Display.WriteLog = ''

# init the 'Transform2' selected for 'TextureTransform'
glyph1Display.TextureTransform.Translate = [0.0, 0.0, 0.0]
glyph1Display.TextureTransform.Rotate = [0.0, 0.0, 0.0]
glyph1Display.TextureTransform.Scale = [1.0, 1.0, 1.0]

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
glyph1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
glyph1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
glyph1Display.GlyphType.TipResolution = 6
glyph1Display.GlyphType.TipRadius = 0.1
glyph1Display.GlyphType.TipLength = 0.35
glyph1Display.GlyphType.ShaftResolution = 6
glyph1Display.GlyphType.ShaftRadius = 0.03
glyph1Display.GlyphType.Invert = 0

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 40.565799463, 1.0, 0.5, 0.0]
glyph1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 40.565799463, 1.0, 0.5, 0.0]
glyph1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'Grid Axes Representation' selected for 'DataAxesGrid'
glyph1Display.DataAxesGrid.XTitle = 'X Axis'
glyph1Display.DataAxesGrid.YTitle = 'Y Axis'
glyph1Display.DataAxesGrid.ZTitle = 'Z Axis'
glyph1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
glyph1Display.DataAxesGrid.XTitleFontFile = ''
glyph1Display.DataAxesGrid.XTitleBold = 0
glyph1Display.DataAxesGrid.XTitleItalic = 0
glyph1Display.DataAxesGrid.XTitleFontSize = 12
glyph1Display.DataAxesGrid.XTitleShadow = 0
glyph1Display.DataAxesGrid.XTitleOpacity = 1.0
glyph1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
glyph1Display.DataAxesGrid.YTitleFontFile = ''
glyph1Display.DataAxesGrid.YTitleBold = 0
glyph1Display.DataAxesGrid.YTitleItalic = 0
glyph1Display.DataAxesGrid.YTitleFontSize = 12
glyph1Display.DataAxesGrid.YTitleShadow = 0
glyph1Display.DataAxesGrid.YTitleOpacity = 1.0
glyph1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
glyph1Display.DataAxesGrid.ZTitleFontFile = ''
glyph1Display.DataAxesGrid.ZTitleBold = 0
glyph1Display.DataAxesGrid.ZTitleItalic = 0
glyph1Display.DataAxesGrid.ZTitleFontSize = 12
glyph1Display.DataAxesGrid.ZTitleShadow = 0
glyph1Display.DataAxesGrid.ZTitleOpacity = 1.0
glyph1Display.DataAxesGrid.FacesToRender = 63
glyph1Display.DataAxesGrid.CullBackface = 0
glyph1Display.DataAxesGrid.CullFrontface = 1
glyph1Display.DataAxesGrid.ShowGrid = 0
glyph1Display.DataAxesGrid.ShowEdges = 1
glyph1Display.DataAxesGrid.ShowTicks = 1
glyph1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
glyph1Display.DataAxesGrid.AxesToLabel = 63
glyph1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
glyph1Display.DataAxesGrid.XLabelFontFile = ''
glyph1Display.DataAxesGrid.XLabelBold = 0
glyph1Display.DataAxesGrid.XLabelItalic = 0
glyph1Display.DataAxesGrid.XLabelFontSize = 12
glyph1Display.DataAxesGrid.XLabelShadow = 0
glyph1Display.DataAxesGrid.XLabelOpacity = 1.0
glyph1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
glyph1Display.DataAxesGrid.YLabelFontFile = ''
glyph1Display.DataAxesGrid.YLabelBold = 0
glyph1Display.DataAxesGrid.YLabelItalic = 0
glyph1Display.DataAxesGrid.YLabelFontSize = 12
glyph1Display.DataAxesGrid.YLabelShadow = 0
glyph1Display.DataAxesGrid.YLabelOpacity = 1.0
glyph1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
glyph1Display.DataAxesGrid.ZLabelFontFile = ''
glyph1Display.DataAxesGrid.ZLabelBold = 0
glyph1Display.DataAxesGrid.ZLabelItalic = 0
glyph1Display.DataAxesGrid.ZLabelFontSize = 12
glyph1Display.DataAxesGrid.ZLabelShadow = 0
glyph1Display.DataAxesGrid.ZLabelOpacity = 1.0
glyph1Display.DataAxesGrid.XAxisNotation = 'Mixed'
glyph1Display.DataAxesGrid.XAxisPrecision = 2
glyph1Display.DataAxesGrid.XAxisUseCustomLabels = 0
glyph1Display.DataAxesGrid.XAxisLabels = []
glyph1Display.DataAxesGrid.YAxisNotation = 'Mixed'
glyph1Display.DataAxesGrid.YAxisPrecision = 2
glyph1Display.DataAxesGrid.YAxisUseCustomLabels = 0
glyph1Display.DataAxesGrid.YAxisLabels = []
glyph1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
glyph1Display.DataAxesGrid.ZAxisPrecision = 2
glyph1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
glyph1Display.DataAxesGrid.ZAxisLabels = []
glyph1Display.DataAxesGrid.UseCustomBounds = 0
glyph1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'Polar Axes Representation' selected for 'PolarAxes'
glyph1Display.PolarAxes.Visibility = 0
glyph1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
glyph1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
glyph1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
glyph1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
glyph1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
glyph1Display.PolarAxes.EnableCustomRange = 0
glyph1Display.PolarAxes.CustomRange = [0.0, 1.0]
glyph1Display.PolarAxes.AutoPole = 1
glyph1Display.PolarAxes.PolarAxisVisibility = 1
glyph1Display.PolarAxes.RadialAxesVisibility = 1
glyph1Display.PolarAxes.DrawRadialGridlines = 1
glyph1Display.PolarAxes.PolarArcsVisibility = 1
glyph1Display.PolarAxes.DrawPolarArcsGridlines = 1
glyph1Display.PolarAxes.NumberOfRadialAxes = 0
glyph1Display.PolarAxes.DeltaAngleRadialAxes = 45.0
glyph1Display.PolarAxes.NumberOfPolarAxes = 5
glyph1Display.PolarAxes.DeltaRangePolarAxes = 0.0
glyph1Display.PolarAxes.CustomMinRadius = 1
glyph1Display.PolarAxes.MinimumRadius = 0.0
glyph1Display.PolarAxes.CustomMaxRadius = 0
glyph1Display.PolarAxes.MaximumRadius = 1.0
glyph1Display.PolarAxes.CustomAngles = 1
glyph1Display.PolarAxes.MinimumAngle = 0.0
glyph1Display.PolarAxes.MaximumAngle = 90.0
glyph1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
glyph1Display.PolarAxes.PolarArcResolutionPerDegree = 0.2
glyph1Display.PolarAxes.Ratio = 1.0
glyph1Display.PolarAxes.EnableOverallColor = 1
glyph1Display.PolarAxes.OverallColor = [1.0, 1.0, 1.0]
glyph1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
glyph1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
glyph1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
glyph1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
glyph1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
glyph1Display.PolarAxes.PolarAxisTitleVisibility = 1
glyph1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
glyph1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
glyph1Display.PolarAxes.PolarTitleOffset = [20.0, 20.0]
glyph1Display.PolarAxes.PolarLabelVisibility = 1
glyph1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
glyph1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
glyph1Display.PolarAxes.PolarLabelOffset = 10.0
glyph1Display.PolarAxes.PolarExponentOffset = 5.0
glyph1Display.PolarAxes.RadialTitleVisibility = 1
glyph1Display.PolarAxes.RadialTitleFormat = '%-#3.1f'
glyph1Display.PolarAxes.RadialTitleLocation = 'Bottom'
glyph1Display.PolarAxes.RadialTitleOffset = [20.0, 0.0]
glyph1Display.PolarAxes.RadialUnitsVisibility = 1
glyph1Display.PolarAxes.ScreenSize = 10.0
glyph1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
glyph1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
glyph1Display.PolarAxes.PolarAxisTitleFontFile = ''
glyph1Display.PolarAxes.PolarAxisTitleBold = 0
glyph1Display.PolarAxes.PolarAxisTitleItalic = 0
glyph1Display.PolarAxes.PolarAxisTitleShadow = 0
glyph1Display.PolarAxes.PolarAxisTitleFontSize = 12
glyph1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
glyph1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
glyph1Display.PolarAxes.PolarAxisLabelFontFile = ''
glyph1Display.PolarAxes.PolarAxisLabelBold = 0
glyph1Display.PolarAxes.PolarAxisLabelItalic = 0
glyph1Display.PolarAxes.PolarAxisLabelShadow = 0
glyph1Display.PolarAxes.PolarAxisLabelFontSize = 12
glyph1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
glyph1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
glyph1Display.PolarAxes.LastRadialAxisTextFontFile = ''
glyph1Display.PolarAxes.LastRadialAxisTextBold = 0
glyph1Display.PolarAxes.LastRadialAxisTextItalic = 0
glyph1Display.PolarAxes.LastRadialAxisTextShadow = 0
glyph1Display.PolarAxes.LastRadialAxisTextFontSize = 12
glyph1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
glyph1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
glyph1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
glyph1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
glyph1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
glyph1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
glyph1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
glyph1Display.PolarAxes.EnableDistanceLOD = 1
glyph1Display.PolarAxes.DistanceLODThreshold = 0.7
glyph1Display.PolarAxes.EnableViewAngleLOD = 1
glyph1Display.PolarAxes.ViewAngleLODThreshold = 0.7
glyph1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
glyph1Display.PolarAxes.PolarTicksVisibility = 1
glyph1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
glyph1Display.PolarAxes.TickLocation = 'Both'
glyph1Display.PolarAxes.AxisTickVisibility = 1
glyph1Display.PolarAxes.AxisMinorTickVisibility = 0
glyph1Display.PolarAxes.AxisTickMatchesPolarAxes = 1
glyph1Display.PolarAxes.DeltaRangeMajor = 1.0
glyph1Display.PolarAxes.DeltaRangeMinor = 0.5
glyph1Display.PolarAxes.ArcTickVisibility = 1
glyph1Display.PolarAxes.ArcMinorTickVisibility = 0
glyph1Display.PolarAxes.ArcTickMatchesRadialAxes = 1
glyph1Display.PolarAxes.DeltaAngleMajor = 10.0
glyph1Display.PolarAxes.DeltaAngleMinor = 5.0
glyph1Display.PolarAxes.TickRatioRadiusSize = 0.02
glyph1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
glyph1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
glyph1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
glyph1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
glyph1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
glyph1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
glyph1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
glyph1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
glyph1Display.PolarAxes.ArcMajorTickSize = 0.0
glyph1Display.PolarAxes.ArcTickRatioSize = 0.3
glyph1Display.PolarAxes.ArcMajorTickThickness = 1.0
glyph1Display.PolarAxes.ArcTickRatioThickness = 0.5
glyph1Display.PolarAxes.Use2DMode = 0
glyph1Display.PolarAxes.UseLogAxis = 0

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [48.69277577421068, -19.16669879176132, -38.524162832162425]
renderView1.CameraFocalPoint = [45.987098693847635, 14.027099609375012, -10.200000002980214]
renderView1.CameraViewUp = [-0.969712958055637, -0.19940193992708477, 0.14105192424175564]
renderView1.CameraParallelScale = 11.315476125271417

# set active source
SetActiveSource(glyph1)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [48.69277577421068, -19.16669879176132, -38.524162832162425]
renderView1.CameraFocalPoint = [45.987098693847635, 14.027099609375012, -10.200000002980214]
renderView1.CameraViewUp = [-0.969712958055637, -0.19940193992708477, 0.14105192424175564]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [48.69277577421068, -19.16669879176132, -38.524162832162425]
renderView1.CameraFocalPoint = [45.987098693847635, 14.027099609375012, -10.200000002980214]
renderView1.CameraViewUp = [-0.969712958055637, -0.19940193992708477, 0.14105192424175564]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [48.36528909123047, -25.79794077632329, -28.080646228545056]
renderView1.CameraFocalPoint = [45.98709869384763, 14.027099609375014, -10.200000002980216]
renderView1.CameraViewUp = [-0.9735340453342473, -0.13943577376641492, 0.1810776837970298]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on glyph1
glyph1.OrientationArray = ['POINTS', 'velocity']
glyph1.ScaleArray = ['POINTS', 'velocity']

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [48.36528909123047, -25.79794077632329, -28.080646228545056]
renderView1.CameraFocalPoint = [45.98709869384763, 14.027099609375014, -10.200000002980216]
renderView1.CameraViewUp = [-0.9735340453342473, -0.13943577376641492, 0.1810776837970298]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [50.18431049892674, 27.154115377809884, 31.290625574505146]
renderView1.CameraFocalPoint = [45.98709869384762, 14.027099609375018, -10.200000002980248]
renderView1.CameraViewUp = [-0.9160592746953874, 0.3996190229224493, -0.03376450448426173]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [49.45586878068987, 24.875872971717882, 24.089773201553136]
renderView1.CameraFocalPoint = [45.98709869384762, 14.027099609375018, -10.200000002980248]
renderView1.CameraViewUp = [-0.9160592746953874, 0.3996190229224493, -0.03376450448426173]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [48.85385083173377, 22.99302800800548, 18.138655537956424]
renderView1.CameraFocalPoint = [45.98709869384762, 14.027099609375018, -10.200000002980248]
renderView1.CameraViewUp = [-0.9160592746953874, 0.3996190229224493, -0.03376450448426173]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [48.98419175564408, 21.66127459912126, 18.51275575368947]
renderView1.CameraFocalPoint = [45.98709869384763, 14.027099609375021, -10.200000002980246]
renderView1.CameraViewUp = [-0.9237197363356769, 0.38303062880326993, -0.005420894992443595]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [48.46403510855544, 20.33633513809092, 13.529550209143483]
renderView1.CameraFocalPoint = [45.98709869384763, 14.027099609375021, -10.200000002980246]
renderView1.CameraViewUp = [-0.9237197363356769, 0.38303062880326993, -0.005420894992443595]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [48.98419175564408, 21.66127459912126, 18.51275575368947]
renderView1.CameraFocalPoint = [45.98709869384763, 14.027099609375021, -10.200000002980246]
renderView1.CameraViewUp = [-0.9237197363356769, 0.38303062880326993, -0.005420894992443595]
renderView1.CameraParallelScale = 11.315476125271417

# set scalar coloring
ColorBy(glyph1Display, ('POINTS', 'velocity', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
glyph1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# get 2D transfer function for 'velocity'
velocityTF2D = GetTransferFunction2D('velocity')
velocityTF2D.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
velocityTF2D.Boxes = []
velocityTF2D.ScalarRangeInitialized = 0
velocityTF2D.Range = [0.0, 1.0, 0.0, 1.0]
velocityTF2D.OutputDimensions = [10, 10]

# get color transfer function/color map for 'velocity'
velocityLUT = GetColorTransferFunction('velocity')
velocityLUT.InterpretValuesAsCategories = 0
velocityLUT.AnnotationsInitialized = 0
velocityLUT.ShowCategoricalColorsinDataRangeOnly = 0
velocityLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
velocityLUT.RescaleOnVisibilityChange = 0
velocityLUT.TransferFunction2D = velocityTF2D
velocityLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.27048755153672, 0.865003, 0.865003, 0.865003, 0.54097510307344, 0.705882, 0.0156863, 0.14902]
velocityLUT.UseLogScale = 0
velocityLUT.UseOpacityControlPointsFreehandDrawing = 0
velocityLUT.ShowDataHistogram = 0
velocityLUT.AutomaticDataHistogramComputation = 0
velocityLUT.DataHistogramNumberOfBins = 10
velocityLUT.ColorSpace = 'Diverging'
velocityLUT.UseBelowRangeColor = 0
velocityLUT.BelowRangeColor = [0.0, 0.0, 0.0]
velocityLUT.UseAboveRangeColor = 0
velocityLUT.AboveRangeColor = [0.5, 0.5, 0.5]
velocityLUT.NanColor = [1.0, 1.0, 0.0]
velocityLUT.NanOpacity = 1.0
velocityLUT.Discretize = 1
velocityLUT.NumberOfTableValues = 256
velocityLUT.ScalarRangeInitialized = 1.0
velocityLUT.HSVWrap = 0
velocityLUT.VectorComponent = 0
velocityLUT.VectorMode = 'Magnitude'
velocityLUT.AllowDuplicateScalars = 1
velocityLUT.Annotations = []
velocityLUT.ActiveAnnotatedValues = []
velocityLUT.IndexedColors = []
velocityLUT.IndexedOpacities = []
velocityLUT.EnableOpacityMapping = 0

# get opacity transfer function/opacity map for 'velocity'
velocityPWF = GetOpacityTransferFunction('velocity')
velocityPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.54097510307344, 1.0, 0.5, 0.0]
velocityPWF.AllowDuplicateScalars = 1
velocityPWF.UseLogScale = 0
velocityPWF.ScalarRangeInitialized = 1
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [48.98419175564408, 21.66127459912126, 18.51275575368947]
renderView1.CameraFocalPoint = [45.98709869384763, 14.027099609375021, -10.200000002980246]
renderView1.CameraViewUp = [-0.9237197363356769, 0.38303062880326993, -0.005420894992443595]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [49.24544693849157, 19.355567662338988, 19.000618700439027]
renderView1.CameraFocalPoint = [45.98709869384763, 14.027099609375018, -10.200000002980238]
renderView1.CameraViewUp = [-0.8780743425318225, 0.47840501117418927, 0.010681491971243226]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [48.679948482809564, 18.430792215130364, 13.932742727118326]
renderView1.CameraFocalPoint = [45.98709869384763, 14.027099609375018, -10.200000002980238]
renderView1.CameraViewUp = [-0.8780743425318225, 0.47840501117418927, 0.010681491971243226]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [49.312801455932906, 17.152838615745164, 14.052890072871367]
renderView1.CameraFocalPoint = [45.98709869384763, 14.02709960937501, -10.20000000298024]
renderView1.CameraViewUp = [-0.9229787138468519, 0.37686507818662984, 0.07799363197721038]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [50.01119903597082, 17.809243807082897, 19.145996988800206]
renderView1.CameraFocalPoint = [45.98709869384763, 14.02709960937501, -10.20000000298024]
renderView1.CameraViewUp = [-0.9229787138468519, 0.37686507818662984, 0.07799363197721038]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [49.312801455932906, 17.152838615745164, 14.052890072871367]
renderView1.CameraFocalPoint = [45.98709869384763, 14.02709960937501, -10.20000000298024]
renderView1.CameraViewUp = [-0.9229787138468519, 0.37686507818662984, 0.07799363197721038]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [50.01119903597082, 17.809243807082897, 19.145996988800206]
renderView1.CameraFocalPoint = [45.98709869384763, 14.02709960937501, -10.20000000298024]
renderView1.CameraViewUp = [-0.9229787138468519, 0.37686507818662984, 0.07799363197721038]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [46.511461128693476, 20.860349515919985, 18.864020322655232]
renderView1.CameraFocalPoint = [45.98709869384762, 14.027099609375044, -10.200000002980252]
renderView1.CameraViewUp = [-0.9902440582062663, 0.13856496564264778, -0.014712426164187007]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [46.511461128693476, 20.860349515919985, 18.864020322655232]
renderView1.CameraFocalPoint = [45.98709869384762, 14.027099609375044, -10.200000002980252]
renderView1.CameraViewUp = [-0.9902440582062663, 0.13856496564264778, -0.014712426164187007]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [46.511461128693476, 20.860349515919985, 18.864020322655232]
renderView1.CameraFocalPoint = [45.98709869384762, 14.027099609375044, -10.200000002980252]
renderView1.CameraViewUp = [-0.9902440582062663, 0.13856496564264778, -0.014712426164187007]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [46.42045607801775, 19.674413581726235, 13.819851505809398]
renderView1.CameraFocalPoint = [45.98709869384762, 14.027099609375044, -10.200000002980252]
renderView1.CameraViewUp = [-0.9902440582062663, 0.13856496564264778, -0.014712426164187007]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [46.34524529233533, 18.69430123941735, 9.651116946432682]
renderView1.CameraFocalPoint = [45.98709869384762, 14.027099609375044, -10.200000002980252]
renderView1.CameraViewUp = [-0.9902440582062663, 0.13856496564264778, -0.014712426164187007]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [46.42045607801774, 19.674413581726235, 13.819851505809401]
renderView1.CameraFocalPoint = [45.98709869384762, 14.027099609375044, -10.200000002980252]
renderView1.CameraViewUp = [-0.9902440582062663, 0.13856496564264778, -0.014712426164187007]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [47.013649455148894, 35.30633070173013, 2.2568751220923144]
renderView1.CameraFocalPoint = [45.98709869384762, 14.027099609375012, -10.20000000298027]
renderView1.CameraViewUp = [-0.9924879937046283, 0.09383481059984848, -0.07850229723933198]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [46.83548775277429, 31.613241008015606, 0.09493811691442389]
renderView1.CameraFocalPoint = [45.98709869384762, 14.027099609375012, -10.20000000298027]
renderView1.CameraViewUp = [-0.9924879937046283, 0.09383481059984848, -0.07850229723933198]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [46.688246676431646, 28.561100765276326, -1.6917866807532516]
renderView1.CameraFocalPoint = [45.98709869384762, 14.027099609375012, -10.20000000298027]
renderView1.CameraViewUp = [-0.9924879937046283, 0.09383481059984848, -0.07850229723933198]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [45.34269088117568, 16.38526946156714, 6.477597712186142]
renderView1.CameraFocalPoint = [45.98709869384761, 14.027099609375039, -10.200000002980264]
renderView1.CameraViewUp = [-0.9671872151547641, -0.25406061259773893, -0.0014477457075688024]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [45.20736524051457, 16.880485130527482, 9.97989323237109]
renderView1.CameraFocalPoint = [45.98709869384761, 14.027099609375039, -10.200000002980264]
renderView1.CameraViewUp = [-0.9671872151547641, -0.25406061259773893, -0.0014477457075688024]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [45.04362121531463, 17.479696089969497, 14.217670811794878]
renderView1.CameraFocalPoint = [45.98709869384761, 14.027099609375039, -10.200000002980264]
renderView1.CameraViewUp = [-0.9671872151547641, -0.25406061259773893, -0.0014477457075688024]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [48.02183013132412, 13.850576007041285, 14.393940869197966]
renderView1.CameraFocalPoint = [45.9870986938476, 14.027099609375037, -10.200000002980254]
renderView1.CameraViewUp = [-0.9670989580488254, -0.24205958289276833, 0.07827364607999078]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [48.02183013132412, 13.850576007041285, 14.393940869197966]
renderView1.CameraFocalPoint = [45.9870986938476, 14.027099609375037, -10.200000002980254]
renderView1.CameraViewUp = [-0.9670989580488254, -0.24205958289276833, 0.07827364607999078]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on glyph1
glyph1.MaximumNumberOfSamplePoints = 50000

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
velocityLUT.RescaleTransferFunction(0.0, 0.5897840373610078)

# Rescale transfer function
velocityPWF.RescaleTransferFunction(0.0, 0.5897840373610078)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [48.02183013132412, 13.850576007041285, 14.393940869197966]
renderView1.CameraFocalPoint = [45.9870986938476, 14.027099609375037, -10.200000002980254]
renderView1.CameraViewUp = [-0.9670989580488254, -0.24205958289276833, 0.07827364607999078]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [41.97653781260311, 23.46295559622949, 12.248012012390003]
renderView1.CameraFocalPoint = [45.9870986938476, 14.027099609375018, -10.200000002980282]
renderView1.CameraViewUp = [-0.9542539152336634, -0.2953872621279507, -0.04632311122730819]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [41.97653781260311, 23.46295559622949, 12.248012012390003]
renderView1.CameraFocalPoint = [45.9870986938476, 14.027099609375018, -10.200000002980282]
renderView1.CameraViewUp = [-0.9542539152336635, -0.29538726212795074, -0.0463231112273082]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.17904815364544, 20.813896671017044, 13.458054843460463]
renderView1.CameraFocalPoint = [45.987098693847585, 14.027099609375027, -10.200000002980275]
renderView1.CameraViewUp = [-0.9631264783252752, -0.26902536663914184, 0.0035691530408042825]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.79935754020299, 22.23912405396187, 18.42624636121302]
renderView1.CameraFocalPoint = [45.987098693847585, 14.027099609375027, -10.200000002980275]
renderView1.CameraViewUp = [-0.9631264783252752, -0.26902536663914184, 0.0035691530408042825]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.339931897937625, 23.96364918732511, 24.437758097693617]
renderView1.CameraFocalPoint = [45.987098693847585, 14.027099609375027, -10.200000002980275]
renderView1.CameraViewUp = [-0.9631264783252752, -0.26902536663914184, 0.0035691530408042825]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.79935754020299, 22.239124053961874, 18.426246361213018]
renderView1.CameraFocalPoint = [45.987098693847585, 14.027099609375027, -10.200000002980275]
renderView1.CameraViewUp = [-0.9631264783252752, -0.26902536663914184, 0.0035691530408042825]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.17904815364544, 20.813896671017048, 13.45805484346046]
renderView1.CameraFocalPoint = [45.987098693847585, 14.027099609375027, -10.200000002980275]
renderView1.CameraViewUp = [-0.9631264783252752, -0.26902536663914184, 0.0035691530408042825]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [46.217810826075976, 17.18859174661137, 14.274169229238252]
renderView1.CameraFocalPoint = [45.98709869384757, 14.02709960937503, -10.20000000298027]
renderView1.CameraViewUp = [-0.964170674364243, -0.2617899383840261, 0.04290616339046094]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [46.26626037384394, 17.852505095431, 19.413744768004143]
renderView1.CameraFocalPoint = [45.98709869384757, 14.02709960937503, -10.20000000298027]
renderView1.CameraViewUp = [-0.964170674364243, -0.2617899383840261, 0.04290616339046094]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [42.87067518143379, 22.856555446765103, 18.155143301968586]
renderView1.CameraFocalPoint = [45.98709869384757, 14.027099609375016, -10.200000002980284]
renderView1.CameraViewUp = [-0.9601962000470186, -0.27869646593141506, -0.01874932779077099]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.411542072018, 21.324170549366823, 13.234002728382412]
renderView1.CameraFocalPoint = [45.98709869384757, 14.027099609375016, -10.200000002980284]
renderView1.CameraViewUp = [-0.9601962000470186, -0.27869646593141506, -0.01874932779077099]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.21571343990711, 19.93697365664764, 13.694953507259788]
renderView1.CameraFocalPoint = [45.98709869384757, 14.02709960937502, -10.20000000298028]
renderView1.CameraViewUp = [-0.9618704593952973, -0.2734808543321984, -0.003666286460545593]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [48.11788578443913, 13.286873895825979, 14.375293128467968]
renderView1.CameraFocalPoint = [45.98709869384755, 14.027099609375025, -10.20000000298026]
renderView1.CameraViewUp = [-0.9613475853820215, -0.26481917272902356, 0.07537656025099988]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.286733332190785, 18.908605040060774, 13.93115998977807]
renderView1.CameraFocalPoint = [45.98709869384755, 14.02709960937502, -10.200000002980277]
renderView1.CameraViewUp = [-0.9609979251447321, -0.27630279162180216, -0.011821810754653753]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.286733332190785, 18.908605040060774, 13.93115998977807]
renderView1.CameraFocalPoint = [45.98709869384755, 14.02709960937502, -10.200000002980277]
renderView1.CameraViewUp = [-0.9609979251447321, -0.27630279162180216, -0.011821810754653753]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.286733332190785, 18.908605040060774, 13.93115998977807]
renderView1.CameraFocalPoint = [45.98709869384755, 14.02709960937502, -10.200000002980277]
renderView1.CameraViewUp = [-0.9609979251447321, -0.27630279162180216, -0.011821810754653753]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.286733332190785, 18.908605040060774, 13.93115998977807]
renderView1.CameraFocalPoint = [45.98709869384755, 14.02709960937502, -10.200000002980277]
renderView1.CameraViewUp = [-0.9609979251447321, -0.27630279162180216, -0.011821810754653753]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on glyph1
glyph1.MaximumNumberOfSamplePoints = 500

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.286733332190785, 18.908605040060774, 13.93115998977807]
renderView1.CameraFocalPoint = [45.98709869384755, 14.02709960937502, -10.200000002980277]
renderView1.CameraViewUp = [-0.9609979251447321, -0.27630279162180216, -0.011821810754653753]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [45.08458301079883, 28.03695789091287, 10.096368061333948]
renderView1.CameraFocalPoint = [45.98709869384756, 14.027099609374984, -10.200000002980271]
renderView1.CameraViewUp = [-0.9142775912957639, -0.3512465024399171, 0.20179787059863022]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.8950547173586, 30.97902813003583, 14.358605354839934]
renderView1.CameraFocalPoint = [45.98709869384756, 14.027099609374984, -10.200000002980271]
renderView1.CameraViewUp = [-0.9142775912957639, -0.3512465024399171, 0.20179787059863022]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [34.929861032283, 24.330947662044128, 15.553713289291183]
renderView1.CameraFocalPoint = [45.98709869384758, 14.027099609374995, -10.200000002980302]
renderView1.CameraViewUp = [-0.8545831637167915, -0.49046491081624827, -0.17068036662079641]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [48.10852993696217, 21.989906199313957, 18.501546617877988]
renderView1.CameraFocalPoint = [45.98709869384756, 14.027099609375005, -10.200000002980264]
renderView1.CameraViewUp = [-0.9064996535113587, -0.38479422090431015, 0.1737578364921475]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [47.740347655099306, 20.607931501886533, 13.520286460538948]
renderView1.CameraFocalPoint = [45.98709869384756, 14.027099609375005, -10.200000002980264]
renderView1.CameraViewUp = [-0.9064996535113587, -0.38479422090431015, 0.1737578364921475]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.96711664250645, 17.580634875332798, 14.137733660097163]
renderView1.CameraFocalPoint = [45.98709869384757, 14.02709960937502, -10.200000002980284]
renderView1.CameraViewUp = [-0.9129998419643789, -0.4076358052177062, -0.01625850170007481]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.96711664250645, 17.580634875332798, 14.137733660097163]
renderView1.CameraFocalPoint = [45.98709869384757, 14.02709960937502, -10.200000002980284]
renderView1.CameraViewUp = [-0.912999841964379, -0.40763580521770626, -0.016258501700074812]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.96711664250645, 17.580634875332798, 14.137733660097163]
renderView1.CameraFocalPoint = [45.98709869384757, 14.02709960937502, -10.200000002980284]
renderView1.CameraViewUp = [-0.912999841964379, -0.40763580521770626, -0.016258501700074812]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.96711664250645, 17.580634875332798, 14.137733660097163]
renderView1.CameraFocalPoint = [45.98709869384757, 14.02709960937502, -10.200000002980284]
renderView1.CameraViewUp = [-0.912999841964379, -0.40763580521770626, -0.016258501700074812]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.96711664250645, 17.580634875332798, 14.137733660097163]
renderView1.CameraFocalPoint = [45.98709869384757, 14.02709960937502, -10.200000002980284]
renderView1.CameraViewUp = [-0.912999841964379, -0.40763580521770626, -0.016258501700074812]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on glyph1
glyph1.MaximumNumberOfSamplePoints = 5000

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.96711664250645, 17.580634875332798, 14.137733660097163]
renderView1.CameraFocalPoint = [45.98709869384757, 14.02709960937502, -10.200000002980284]
renderView1.CameraViewUp = [-0.912999841964379, -0.40763580521770626, -0.016258501700074812]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on glyph1
glyph1.Seed = 1033

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.96711664250645, 17.580634875332798, 14.137733660097163]
renderView1.CameraFocalPoint = [45.98709869384757, 14.02709960937502, -10.200000002980284]
renderView1.CameraViewUp = [-0.912999841964379, -0.40763580521770626, -0.016258501700074812]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [47.4421637844858, 15.58745577948956, 14.38620129842926]
renderView1.CameraFocalPoint = [45.98709869384756, 14.027099609375025, -10.200000002980273]
renderView1.CameraViewUp = [-0.9132758300305269, -0.3995272438514602, 0.07940553949510054]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [47.74772745351983, 15.915130575213611, 19.54930357172526]
renderView1.CameraFocalPoint = [45.98709869384756, 14.027099609375025, -10.200000002980273]
renderView1.CameraViewUp = [-0.9132758300305269, -0.3995272438514602, 0.07940553949510054]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.02631398325992, 17.289864890723308, 19.417481722765586]
renderView1.CameraFocalPoint = [45.98709869384758, 14.027099609375007, -10.200000002980284]
renderView1.CameraViewUp = [-0.9026296812975345, -0.4302404849761286, -0.012360563426363835]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.02631398325992, 17.289864890723308, 19.417481722765586]
renderView1.CameraFocalPoint = [45.98709869384758, 14.027099609375007, -10.200000002980284]
renderView1.CameraViewUp = [-0.9026296812975345, -0.4302404849761286, -0.012360563426363835]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.02631398325992, 17.289864890723308, 19.417481722765586]
renderView1.CameraFocalPoint = [45.98709869384758, 14.027099609375007, -10.200000002980284]
renderView1.CameraViewUp = [-0.9026296812975345, -0.4302404849761286, -0.012360563426363835]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.02631398325992, 17.289864890723308, 19.417481722765586]
renderView1.CameraFocalPoint = [45.98709869384758, 14.027099609375007, -10.200000002980284]
renderView1.CameraViewUp = [-0.9026296812975345, -0.4302404849761286, -0.012360563426363835]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on glyph1
glyph1.Seed = 10339

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.02631398325992, 17.289864890723308, 19.417481722765586]
renderView1.CameraFocalPoint = [45.98709869384758, 14.027099609375007, -10.200000002980284]
renderView1.CameraViewUp = [-0.9026296812975345, -0.4302404849761286, -0.012360563426363835]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.02631398325992, 17.289864890723308, 19.417481722765586]
renderView1.CameraFocalPoint = [45.98709869384758, 14.027099609375007, -10.200000002980284]
renderView1.CameraViewUp = [-0.9026296812975345, -0.4302404849761286, -0.012360563426363835]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.02631398325992, 17.289864890723308, 19.417481722765586]
renderView1.CameraFocalPoint = [45.98709869384758, 14.027099609375007, -10.200000002980284]
renderView1.CameraViewUp = [-0.9026296812975345, -0.4302404849761286, -0.012360563426363835]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on glyph1
glyph1.ScaleArray = ['POINTS', 'No scale array']

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.02631398325992, 17.289864890723308, 19.417481722765586]
renderView1.CameraFocalPoint = [45.98709869384758, 14.027099609375007, -10.200000002980284]
renderView1.CameraViewUp = [-0.9026296812975345, -0.4302404849761286, -0.012360563426363835]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [50.492685577789295, 12.648827431934093, 19.287041055313114]
renderView1.CameraFocalPoint = [45.98709869384758, 14.027099609375009, -10.20000000298029]
renderView1.CameraViewUp = [-0.7896789864033649, -0.6065357922924224, 0.09231159786916243]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [49.710724217766355, 12.888031694134582, 14.1694554170969]
renderView1.CameraFocalPoint = [45.98709869384758, 14.027099609375009, -10.20000000298029]
renderView1.CameraViewUp = [-0.7896789864033649, -0.6065357922924224, 0.09231159786916243]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [50.492685577789295, 12.648827431934093, 19.28704105531311]
renderView1.CameraFocalPoint = [45.98709869384758, 14.027099609375009, -10.20000000298029]
renderView1.CameraViewUp = [-0.7896789864033649, -0.6065357922924224, 0.09231159786916243]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [51.43885882341706, 12.359390274671501, 25.479319677554727]
renderView1.CameraFocalPoint = [45.98709869384758, 14.027099609375009, -10.20000000298029]
renderView1.CameraViewUp = [-0.7896789864033649, -0.6065357922924224, 0.09231159786916243]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.061073289889904, 14.665504926093748, 25.807604885268184]
renderView1.CameraFocalPoint = [45.98709869384757, 14.027099609375004, -10.200000002980273]
renderView1.CameraViewUp = [-0.7783246693074256, -0.6256921246208185, -0.05215433189077211]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.288050208783744, 20.78285675192184, 25.19197194698944]
renderView1.CameraFocalPoint = [45.987098693847614, 14.027099609375044, -10.200000002980278]
renderView1.CameraViewUp = [-0.99306813475307, -0.10333858146653505, -0.05600729701157491]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.288050208783744, 20.78285675192184, 25.19197194698944]
renderView1.CameraFocalPoint = [45.987098693847614, 14.027099609375044, -10.200000002980278]
renderView1.CameraViewUp = [-0.99306813475307, -0.10333858146653505, -0.05600729701157491]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.288050208783744, 20.78285675192184, 25.19197194698944]
renderView1.CameraFocalPoint = [45.987098693847614, 14.027099609375044, -10.200000002980278]
renderView1.CameraViewUp = [-0.99306813475307, -0.10333858146653505, -0.05600729701157491]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [45.60610962650256, -21.980247769307415, -7.22635276722695]
renderView1.CameraFocalPoint = [45.98709869384761, 14.02709960937504, -10.200000002980193]
renderView1.CameraViewUp = [-0.8540382661555882, -0.03383384760538625, -0.5191087657689593]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [45.60610962650256, -21.980247769307415, -7.22635276722695]
renderView1.CameraFocalPoint = [45.98709869384761, 14.02709960937504, -10.200000002980193]
renderView1.CameraViewUp = [-0.8540382661555882, -0.03383384760538625, -0.5191087657689593]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [45.60610962650256, -21.980247769307415, -7.22635276722695]
renderView1.CameraFocalPoint = [45.98709869384761, 14.02709960937504, -10.200000002980193]
renderView1.CameraViewUp = [-0.8540382661555882, -0.03383384760538625, -0.5191087657689593]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [45.60610962650256, -21.980247769307415, -7.22635276722695]
renderView1.CameraFocalPoint = [45.98709869384761, 14.02709960937504, -10.200000002980193]
renderView1.CameraViewUp = [-0.8540382661555882, -0.03383384760538625, -0.5191087657689593]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [45.60610962650256, -21.980247769307415, -7.22635276722695]
renderView1.CameraFocalPoint = [45.98709869384761, 14.02709960937504, -10.200000002980193]
renderView1.CameraViewUp = [-0.8540382661555882, -0.03383384760538625, -0.5191087657689593]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [45.60610962650256, -21.980247769307415, -7.22635276722695]
renderView1.CameraFocalPoint = [45.98709869384761, 14.02709960937504, -10.200000002980193]
renderView1.CameraViewUp = [-0.8540382661555882, -0.03383384760538625, -0.5191087657689593]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [25.970306021270293, 21.780872950214043, 18.86413263302312]
renderView1.CameraFocalPoint = [45.98709869384766, 14.02709960937505, -10.200000002980289]
renderView1.CameraViewUp = [-0.8216947267725931, 0.014379232943306577, -0.5697464468112774]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [25.970306021270293, 21.780872950214043, 18.86413263302312]
renderView1.CameraFocalPoint = [45.98709869384766, 14.02709960937505, -10.200000002980289]
renderView1.CameraViewUp = [-0.8216947267725931, 0.014379232943306577, -0.5697464468112774]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on glyph1
glyph1.MaximumNumberOfSamplePoints = 500

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [25.970306021270293, 21.780872950214043, 18.86413263302312]
renderView1.CameraFocalPoint = [45.98709869384766, 14.02709960937505, -10.200000002980289]
renderView1.CameraViewUp = [-0.8216947267725931, 0.014379232943306577, -0.5697464468112774]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [46.50686217321356, 21.68238839230409, 25.10783475613133]
renderView1.CameraFocalPoint = [45.98709869384765, 14.027099609375055, -10.200000002980289]
renderView1.CameraViewUp = [-0.9864544872012613, 0.16271647673019218, -0.020757959461600584]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [42.07413891568414, 15.976560074179163, 25.666490562335724]
renderView1.CameraFocalPoint = [45.98709869384765, 14.027099609375071, -10.200000002980275]
renderView1.CameraViewUp = [-0.9814453635920147, 0.15312933242470986, -0.11539673234065582]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [72.4722787331844, 33.177058609496896, -25.60555433831125]
renderView1.CameraFocalPoint = [45.98709869384766, 14.02709960937503, -10.200000002980167]
renderView1.CameraViewUp = [0.6780853539284647, -0.6189088182171826, 0.39642417625659426]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [72.4722787331844, 33.177058609496896, -25.60555433831125]
renderView1.CameraFocalPoint = [45.98709869384766, 14.02709960937503, -10.200000002980167]
renderView1.CameraViewUp = [0.6780853539284647, -0.6189088182171826, 0.39642417625659426]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [40.17457722701003, 1.310299807772058, 23.11687849433365]
renderView1.CameraFocalPoint = [45.98709869384757, 14.027099609374984, -10.20000000298026]
renderView1.CameraViewUp = [0.1714751566533378, -0.9300158957281539, -0.325064154196788]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [40.17457722701003, 1.310299807772058, 23.11687849433365]
renderView1.CameraFocalPoint = [45.98709869384757, 14.027099609374984, -10.20000000298026]
renderView1.CameraViewUp = [0.1714751566533378, -0.9300158957281539, -0.325064154196788]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [40.17457722701003, 1.310299807772058, 23.11687849433365]
renderView1.CameraFocalPoint = [45.98709869384757, 14.027099609374984, -10.20000000298026]
renderView1.CameraViewUp = [0.1714751566533378, -0.9300158957281539, -0.325064154196788]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [40.17457722701003, 1.310299807772058, 23.11687849433365]
renderView1.CameraFocalPoint = [45.98709869384757, 14.027099609374984, -10.20000000298026]
renderView1.CameraViewUp = [0.1714751566533378, -0.9300158957281539, -0.325064154196788]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on glyph1
glyph1.MaximumNumberOfSamplePoints = 5000
glyph1.Seed = 1033

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [40.17457722701003, 1.310299807772058, 23.11687849433365]
renderView1.CameraFocalPoint = [45.98709869384757, 14.027099609374984, -10.20000000298026]
renderView1.CameraViewUp = [0.1714751566533378, -0.9300158957281539, -0.325064154196788]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [37.74350335853752, 3.1601531319529528, 23.25847285526265]
renderView1.CameraFocalPoint = [45.98709869384759, 14.027099609374975, -10.200000002980277]
renderView1.CameraViewUp = [0.14159778564061642, -0.951230798742626, -0.2740620999429512]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [37.74350335853752, 3.1601531319529528, 23.25847285526265]
renderView1.CameraFocalPoint = [45.98709869384759, 14.027099609374975, -10.200000002980277]
renderView1.CameraViewUp = [0.14159778564061642, -0.951230798742626, -0.2740620999429512]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on glyph1
glyph1.Seed = 10339

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [37.74350335853752, 3.1601531319529528, 23.25847285526265]
renderView1.CameraFocalPoint = [45.98709869384759, 14.027099609374975, -10.200000002980277]
renderView1.CameraViewUp = [0.14159778564061642, -0.951230798742626, -0.2740620999429512]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [39.91738726081985, 2.0798208106430494, 23.35499855500546]
renderView1.CameraFocalPoint = [45.9870986938476, 14.027099609374979, -10.200000002980286]
renderView1.CameraViewUp = [0.1658254742001295, -0.938121533133904, -0.3040228629178994]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [39.91738726081985, 2.0798208106430494, 23.35499855500546]
renderView1.CameraFocalPoint = [45.9870986938476, 14.027099609374979, -10.200000002980286]
renderView1.CameraViewUp = [0.1658254742001295, -0.938121533133904, -0.3040228629178994]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on glyph1
glyph1.Seed = 1033

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [39.91738726081985, 2.0798208106430494, 23.35499855500546]
renderView1.CameraFocalPoint = [45.9870986938476, 14.027099609374979, -10.200000002980286]
renderView1.CameraViewUp = [0.1658254742001295, -0.938121533133904, -0.3040228629178994]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [41.777643193130764, 0.5544567626747817, 23.060865513629956]
renderView1.CameraFocalPoint = [45.987098693847585, 14.027099609374977, -10.200000002980286]
renderView1.CameraViewUp = [0.19828095136979604, -0.9169244744429876, -0.3463151346553301]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [41.777643193130764, 0.5544567626747817, 23.060865513629956]
renderView1.CameraFocalPoint = [45.987098693847585, 14.027099609374977, -10.200000002980286]
renderView1.CameraViewUp = [0.19828095136979604, -0.9169244744429876, -0.3463151346553301]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [41.777643193130764, 0.5544567626747817, 23.060865513629956]
renderView1.CameraFocalPoint = [45.987098693847585, 14.027099609374977, -10.200000002980286]
renderView1.CameraViewUp = [0.19828095136979604, -0.9169244744429876, -0.3463151346553301]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [41.777643193130764, 0.5544567626747817, 23.060865513629956]
renderView1.CameraFocalPoint = [45.987098693847585, 14.027099609374977, -10.200000002980286]
renderView1.CameraViewUp = [0.19828095136979604, -0.9169244744429876, -0.3463151346553301]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on glyph1
glyph1.Seed = 10339

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [41.777643193130764, 0.5544567626747817, 23.060865513629956]
renderView1.CameraFocalPoint = [45.987098693847585, 14.027099609374977, -10.200000002980286]
renderView1.CameraViewUp = [0.19828095136979604, -0.9169244744429876, -0.3463151346553301]
renderView1.CameraParallelScale = 11.315476125271417

# hide data in view
Hide(glyph1, renderView1)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [41.777643193130764, 0.5544567626747817, 23.060865513629956]
renderView1.CameraFocalPoint = [45.987098693847585, 14.027099609374977, -10.200000002980286]
renderView1.CameraViewUp = [0.19828095136979604, -0.9169244744429876, -0.3463151346553301]
renderView1.CameraParallelScale = 11.315476125271417

# set active source
SetActiveSource(calculator1)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=calculator1Display.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=calculator1Display)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=calculator1Display.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=calculator1Display)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [41.777643193130764, 0.5544567626747817, 23.060865513629956]
renderView1.CameraFocalPoint = [45.987098693847585, 14.027099609374977, -10.200000002980286]
renderView1.CameraViewUp = [0.19828095136979604, -0.9169244744429876, -0.3463151346553301]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [41.777643193130764, 0.5544567626747817, 23.060865513629956]
renderView1.CameraFocalPoint = [45.987098693847585, 14.027099609374977, -10.200000002980286]
renderView1.CameraViewUp = [0.19828095136979604, -0.9169244744429876, -0.3463151346553301]
renderView1.CameraParallelScale = 11.315476125271417

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(registrationName='StreamTracer1', Input=calculator1,
    SeedType='Line')
streamTracer1.Vectors = ['POINTS', 'velocity']
streamTracer1.InterpolatorType = 'Interpolator with Point Locator'
streamTracer1.SurfaceStreamlines = 0
streamTracer1.IntegrationDirection = 'BOTH'
streamTracer1.IntegratorType = 'Runge-Kutta 4-5'
streamTracer1.IntegrationStepUnit = 'Cell Length'
streamTracer1.InitialStepLength = 0.2
streamTracer1.MinimumStepLength = 0.01
streamTracer1.MaximumStepLength = 0.5
streamTracer1.MaximumSteps = 2000
streamTracer1.MaximumStreamlineLength = 19.6
streamTracer1.TerminalSpeed = 1e-12
streamTracer1.MaximumError = 1e-06
streamTracer1.ComputeVorticity = 1

# init the 'Line' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [41.9871, 10.0271, -20.0]
streamTracer1.SeedType.Point2 = [49.9871, 18.0271, -0.3999999999999986]
streamTracer1.SeedType.Resolution = 1000
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [41.777643193130764, 0.5544567626747817, 23.060865513629956]
renderView1.CameraFocalPoint = [45.987098693847585, 14.027099609374977, -10.200000002980286]
renderView1.CameraViewUp = [0.19828095136979604, -0.9169244744429876, -0.3463151346553301]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [41.777643193130764, 0.5544567626747817, 23.060865513629956]
renderView1.CameraFocalPoint = [45.987098693847585, 14.027099609374977, -10.200000002980286]
renderView1.CameraViewUp = [0.19828095136979604, -0.9169244744429876, -0.3463151346553301]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [41.777643193130764, 0.5544567626747817, 23.060865513629956]
renderView1.CameraFocalPoint = [45.987098693847585, 14.027099609374977, -10.200000002980286]
renderView1.CameraViewUp = [0.19828095136979604, -0.9169244744429876, -0.3463151346553301]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.165083872052435, 8.262600003608298, 20.098829976814834]
renderView1.CameraFocalPoint = [45.9870986938476, 14.027099609374961, -10.2000000029803]
renderView1.CameraViewUp = [0.10902048533691928, -0.9867682208936517, -0.12001254939080373]
renderView1.CameraParallelScale = 11.315476125271417

# show data in view
streamTracer1Display = Show(streamTracer1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
streamTracer1Display.Selection = None
streamTracer1Display.Representation = 'Surface'
streamTracer1Display.ColorArrayName = [None, '']
streamTracer1Display.LookupTable = None
streamTracer1Display.MapScalars = 1
streamTracer1Display.MultiComponentsMapping = 0
streamTracer1Display.InterpolateScalarsBeforeMapping = 1
streamTracer1Display.UseNanColorForMissingArrays = 0
streamTracer1Display.Opacity = 1.0
streamTracer1Display.PointSize = 2.0
streamTracer1Display.LineWidth = 1.0
streamTracer1Display.RenderLinesAsTubes = 0
streamTracer1Display.RenderPointsAsSpheres = 0
streamTracer1Display.DisableLighting = 0
streamTracer1Display.Diffuse = 1.0
streamTracer1Display.Interpolation = 'Gouraud'
streamTracer1Display.Specular = 0.0
streamTracer1Display.SpecularColor = [1.0, 1.0, 1.0]
streamTracer1Display.SpecularPower = 100.0
streamTracer1Display.Luminosity = 0.0
streamTracer1Display.Ambient = 0.0
streamTracer1Display.Roughness = 0.3
streamTracer1Display.Metallic = 0.0
streamTracer1Display.EdgeTint = [1.0, 1.0, 1.0]
streamTracer1Display.Anisotropy = 0.0
streamTracer1Display.AnisotropyRotation = 0.0
streamTracer1Display.BaseIOR = 1.5
streamTracer1Display.CoatStrength = 0.0
streamTracer1Display.CoatIOR = 2.0
streamTracer1Display.CoatRoughness = 0.0
streamTracer1Display.CoatColor = [1.0, 1.0, 1.0]
streamTracer1Display.SelectNormalArray = 'None'
streamTracer1Display.SelectTangentArray = 'None'
streamTracer1Display.ComputePointNormals = 0
streamTracer1Display.Splitting = 1
streamTracer1Display.FeatureAngle = 30.0
streamTracer1Display.SelectTCoordArray = 'None'
streamTracer1Display.Texture = None
streamTracer1Display.RepeatTextures = 1
streamTracer1Display.InterpolateTextures = 0
streamTracer1Display.SeamlessU = 0
streamTracer1Display.SeamlessV = 0
streamTracer1Display.UseMipmapTextures = 0
streamTracer1Display.ShowTexturesOnBackface = 1
streamTracer1Display.BaseColorTexture = None
streamTracer1Display.NormalTexture = None
streamTracer1Display.NormalScale = 1.0
streamTracer1Display.CoatNormalTexture = None
streamTracer1Display.CoatNormalScale = 1.0
streamTracer1Display.MaterialTexture = None
streamTracer1Display.OcclusionStrength = 1.0
streamTracer1Display.AnisotropyTexture = None
streamTracer1Display.EmissiveTexture = None
streamTracer1Display.EmissiveFactor = [1.0, 1.0, 1.0]
streamTracer1Display.TextureTransform = 'Transform2'
streamTracer1Display.EdgeOpacity = 1.0
streamTracer1Display.BackfaceRepresentation = 'Follow Frontface'
streamTracer1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
streamTracer1Display.BackfaceOpacity = 1.0
streamTracer1Display.Translation = [0.0, 0.0, 0.0]
streamTracer1Display.Scale = [1.0, 1.0, 1.0]
streamTracer1Display.Orientation = [0.0, 0.0, 0.0]
streamTracer1Display.Origin = [0.0, 0.0, 0.0]
streamTracer1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
streamTracer1Display.Pickable = 1
streamTracer1Display.Triangulate = 0
streamTracer1Display.UseShaderReplacements = 0
streamTracer1Display.ShaderReplacements = ''
streamTracer1Display.NonlinearSubdivisionLevel = 1
streamTracer1Display.MatchBoundariesIgnoringCellOrder = 0
streamTracer1Display.UseDataPartitions = 0
streamTracer1Display.OSPRayUseScaleArray = 'All Approximate'
streamTracer1Display.OSPRayScaleArray = 'AngularVelocity'
streamTracer1Display.OSPRayScaleFunction = 'Piecewise Function'
streamTracer1Display.OSPRayMaterial = 'None'
streamTracer1Display.Assembly = ''
streamTracer1Display.SelectedBlockSelectors = ['']
streamTracer1Display.BlockSelectors = ['/']
streamTracer1Display.BlockColors = []
streamTracer1Display.BlockColorArrayNames = []
streamTracer1Display.BlockLookupTables = []
streamTracer1Display.BlockUseSeparateColorMaps = []
streamTracer1Display.BlockMapScalars = []
streamTracer1Display.BlockInterpolateScalarsBeforeMappings = []
streamTracer1Display.BlockOpacities = []
streamTracer1Display.BlockMapScalarsGUI = 1
streamTracer1Display.BlockInterpolateScalarsBeforeMappingsGUI = 1
streamTracer1Display.BlockOpacitiesGUI = 1.0
streamTracer1Display.Orient = 0
streamTracer1Display.OrientationMode = 'Direction'
streamTracer1Display.SelectOrientationVectors = 'Normals'
streamTracer1Display.Scaling = 0
streamTracer1Display.ScaleMode = 'No Data Scaling Off'
streamTracer1Display.ScaleFactor = 1.9599999994039536
streamTracer1Display.SelectScaleArray = 'AngularVelocity'
streamTracer1Display.GlyphType = 'Arrow'
streamTracer1Display.UseGlyphTable = 0
streamTracer1Display.GlyphTableIndexArray = 'AngularVelocity'
streamTracer1Display.UseCompositeGlyphTable = 0
streamTracer1Display.UseGlyphCullingAndLOD = 0
streamTracer1Display.LODValues = []
streamTracer1Display.ColorByLODIndex = 0
streamTracer1Display.GaussianRadius = 0.09799999997019768
streamTracer1Display.ShaderPreset = 'Sphere'
streamTracer1Display.CustomTriangleScale = 3
streamTracer1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
streamTracer1Display.Emissive = 0
streamTracer1Display.ScaleByArray = 0
streamTracer1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.ScaleArrayComponent = ''
streamTracer1Display.UseScaleFunction = 1
streamTracer1Display.ScaleTransferFunction = 'Piecewise Function'
streamTracer1Display.OpacityByArray = 0
streamTracer1Display.OpacityArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.OpacityArrayComponent = ''
streamTracer1Display.OpacityTransferFunction = 'Piecewise Function'
streamTracer1Display.DataAxesGrid = 'Grid Axes Representation'
streamTracer1Display.SelectionCellLabelBold = 0
streamTracer1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
streamTracer1Display.SelectionCellLabelFontFamily = 'Arial'
streamTracer1Display.SelectionCellLabelFontFile = ''
streamTracer1Display.SelectionCellLabelFontSize = 18
streamTracer1Display.SelectionCellLabelItalic = 0
streamTracer1Display.SelectionCellLabelJustification = 'Left'
streamTracer1Display.SelectionCellLabelOpacity = 1.0
streamTracer1Display.SelectionCellLabelShadow = 0
streamTracer1Display.SelectionPointLabelBold = 0
streamTracer1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
streamTracer1Display.SelectionPointLabelFontFamily = 'Arial'
streamTracer1Display.SelectionPointLabelFontFile = ''
streamTracer1Display.SelectionPointLabelFontSize = 18
streamTracer1Display.SelectionPointLabelItalic = 0
streamTracer1Display.SelectionPointLabelJustification = 'Left'
streamTracer1Display.SelectionPointLabelOpacity = 1.0
streamTracer1Display.SelectionPointLabelShadow = 0
streamTracer1Display.PolarAxes = 'Polar Axes Representation'
streamTracer1Display.SelectInputVectors = ['POINTS', 'Normals']
streamTracer1Display.NumberOfSteps = 40
streamTracer1Display.StepSize = 0.25
streamTracer1Display.NormalizeVectors = 1
streamTracer1Display.EnhancedLIC = 1
streamTracer1Display.ColorMode = 'Blend'
streamTracer1Display.LICIntensity = 0.8
streamTracer1Display.MapModeBias = 0.0
streamTracer1Display.EnhanceContrast = 'Off'
streamTracer1Display.LowLICContrastEnhancementFactor = 0.0
streamTracer1Display.HighLICContrastEnhancementFactor = 0.0
streamTracer1Display.LowColorContrastEnhancementFactor = 0.0
streamTracer1Display.HighColorContrastEnhancementFactor = 0.0
streamTracer1Display.AntiAlias = 0
streamTracer1Display.MaskOnSurface = 1
streamTracer1Display.MaskThreshold = 0.0
streamTracer1Display.MaskIntensity = 0.0
streamTracer1Display.MaskColor = [0.5, 0.5, 0.5]
streamTracer1Display.GenerateNoiseTexture = 0
streamTracer1Display.NoiseType = 'Gaussian'
streamTracer1Display.NoiseTextureSize = 128
streamTracer1Display.NoiseGrainSize = 2
streamTracer1Display.MinNoiseValue = 0.0
streamTracer1Display.MaxNoiseValue = 0.8
streamTracer1Display.NumberOfNoiseLevels = 1024
streamTracer1Display.ImpulseNoiseProbability = 1.0
streamTracer1Display.ImpulseNoiseBackgroundValue = 0.0
streamTracer1Display.NoiseGeneratorSeed = 1
streamTracer1Display.CompositeStrategy = 'AUTO'
streamTracer1Display.UseLICForLOD = 0
streamTracer1Display.WriteLog = ''

# init the 'Transform2' selected for 'TextureTransform'
streamTracer1Display.TextureTransform.Translate = [0.0, 0.0, 0.0]
streamTracer1Display.TextureTransform.Rotate = [0.0, 0.0, 0.0]
streamTracer1Display.TextureTransform.Scale = [1.0, 1.0, 1.0]

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
streamTracer1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
streamTracer1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
streamTracer1Display.GlyphType.TipResolution = 6
streamTracer1Display.GlyphType.TipRadius = 0.1
streamTracer1Display.GlyphType.TipLength = 0.35
streamTracer1Display.GlyphType.ShaftResolution = 6
streamTracer1Display.GlyphType.ShaftRadius = 0.03
streamTracer1Display.GlyphType.Invert = 0

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
streamTracer1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
streamTracer1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
streamTracer1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
streamTracer1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'Grid Axes Representation' selected for 'DataAxesGrid'
streamTracer1Display.DataAxesGrid.XTitle = 'X Axis'
streamTracer1Display.DataAxesGrid.YTitle = 'Y Axis'
streamTracer1Display.DataAxesGrid.ZTitle = 'Z Axis'
streamTracer1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
streamTracer1Display.DataAxesGrid.XTitleFontFile = ''
streamTracer1Display.DataAxesGrid.XTitleBold = 0
streamTracer1Display.DataAxesGrid.XTitleItalic = 0
streamTracer1Display.DataAxesGrid.XTitleFontSize = 12
streamTracer1Display.DataAxesGrid.XTitleShadow = 0
streamTracer1Display.DataAxesGrid.XTitleOpacity = 1.0
streamTracer1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
streamTracer1Display.DataAxesGrid.YTitleFontFile = ''
streamTracer1Display.DataAxesGrid.YTitleBold = 0
streamTracer1Display.DataAxesGrid.YTitleItalic = 0
streamTracer1Display.DataAxesGrid.YTitleFontSize = 12
streamTracer1Display.DataAxesGrid.YTitleShadow = 0
streamTracer1Display.DataAxesGrid.YTitleOpacity = 1.0
streamTracer1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
streamTracer1Display.DataAxesGrid.ZTitleFontFile = ''
streamTracer1Display.DataAxesGrid.ZTitleBold = 0
streamTracer1Display.DataAxesGrid.ZTitleItalic = 0
streamTracer1Display.DataAxesGrid.ZTitleFontSize = 12
streamTracer1Display.DataAxesGrid.ZTitleShadow = 0
streamTracer1Display.DataAxesGrid.ZTitleOpacity = 1.0
streamTracer1Display.DataAxesGrid.FacesToRender = 63
streamTracer1Display.DataAxesGrid.CullBackface = 0
streamTracer1Display.DataAxesGrid.CullFrontface = 1
streamTracer1Display.DataAxesGrid.ShowGrid = 0
streamTracer1Display.DataAxesGrid.ShowEdges = 1
streamTracer1Display.DataAxesGrid.ShowTicks = 1
streamTracer1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
streamTracer1Display.DataAxesGrid.AxesToLabel = 63
streamTracer1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
streamTracer1Display.DataAxesGrid.XLabelFontFile = ''
streamTracer1Display.DataAxesGrid.XLabelBold = 0
streamTracer1Display.DataAxesGrid.XLabelItalic = 0
streamTracer1Display.DataAxesGrid.XLabelFontSize = 12
streamTracer1Display.DataAxesGrid.XLabelShadow = 0
streamTracer1Display.DataAxesGrid.XLabelOpacity = 1.0
streamTracer1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
streamTracer1Display.DataAxesGrid.YLabelFontFile = ''
streamTracer1Display.DataAxesGrid.YLabelBold = 0
streamTracer1Display.DataAxesGrid.YLabelItalic = 0
streamTracer1Display.DataAxesGrid.YLabelFontSize = 12
streamTracer1Display.DataAxesGrid.YLabelShadow = 0
streamTracer1Display.DataAxesGrid.YLabelOpacity = 1.0
streamTracer1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
streamTracer1Display.DataAxesGrid.ZLabelFontFile = ''
streamTracer1Display.DataAxesGrid.ZLabelBold = 0
streamTracer1Display.DataAxesGrid.ZLabelItalic = 0
streamTracer1Display.DataAxesGrid.ZLabelFontSize = 12
streamTracer1Display.DataAxesGrid.ZLabelShadow = 0
streamTracer1Display.DataAxesGrid.ZLabelOpacity = 1.0
streamTracer1Display.DataAxesGrid.XAxisNotation = 'Mixed'
streamTracer1Display.DataAxesGrid.XAxisPrecision = 2
streamTracer1Display.DataAxesGrid.XAxisUseCustomLabels = 0
streamTracer1Display.DataAxesGrid.XAxisLabels = []
streamTracer1Display.DataAxesGrid.YAxisNotation = 'Mixed'
streamTracer1Display.DataAxesGrid.YAxisPrecision = 2
streamTracer1Display.DataAxesGrid.YAxisUseCustomLabels = 0
streamTracer1Display.DataAxesGrid.YAxisLabels = []
streamTracer1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
streamTracer1Display.DataAxesGrid.ZAxisPrecision = 2
streamTracer1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
streamTracer1Display.DataAxesGrid.ZAxisLabels = []
streamTracer1Display.DataAxesGrid.UseCustomBounds = 0
streamTracer1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'Polar Axes Representation' selected for 'PolarAxes'
streamTracer1Display.PolarAxes.Visibility = 0
streamTracer1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
streamTracer1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
streamTracer1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
streamTracer1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
streamTracer1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
streamTracer1Display.PolarAxes.EnableCustomRange = 0
streamTracer1Display.PolarAxes.CustomRange = [0.0, 1.0]
streamTracer1Display.PolarAxes.AutoPole = 1
streamTracer1Display.PolarAxes.PolarAxisVisibility = 1
streamTracer1Display.PolarAxes.RadialAxesVisibility = 1
streamTracer1Display.PolarAxes.DrawRadialGridlines = 1
streamTracer1Display.PolarAxes.PolarArcsVisibility = 1
streamTracer1Display.PolarAxes.DrawPolarArcsGridlines = 1
streamTracer1Display.PolarAxes.NumberOfRadialAxes = 0
streamTracer1Display.PolarAxes.DeltaAngleRadialAxes = 45.0
streamTracer1Display.PolarAxes.NumberOfPolarAxes = 5
streamTracer1Display.PolarAxes.DeltaRangePolarAxes = 0.0
streamTracer1Display.PolarAxes.CustomMinRadius = 1
streamTracer1Display.PolarAxes.MinimumRadius = 0.0
streamTracer1Display.PolarAxes.CustomMaxRadius = 0
streamTracer1Display.PolarAxes.MaximumRadius = 1.0
streamTracer1Display.PolarAxes.CustomAngles = 1
streamTracer1Display.PolarAxes.MinimumAngle = 0.0
streamTracer1Display.PolarAxes.MaximumAngle = 90.0
streamTracer1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
streamTracer1Display.PolarAxes.PolarArcResolutionPerDegree = 0.2
streamTracer1Display.PolarAxes.Ratio = 1.0
streamTracer1Display.PolarAxes.EnableOverallColor = 1
streamTracer1Display.PolarAxes.OverallColor = [1.0, 1.0, 1.0]
streamTracer1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
streamTracer1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
streamTracer1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
streamTracer1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
streamTracer1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
streamTracer1Display.PolarAxes.PolarAxisTitleVisibility = 1
streamTracer1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
streamTracer1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
streamTracer1Display.PolarAxes.PolarTitleOffset = [20.0, 20.0]
streamTracer1Display.PolarAxes.PolarLabelVisibility = 1
streamTracer1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
streamTracer1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
streamTracer1Display.PolarAxes.PolarLabelOffset = 10.0
streamTracer1Display.PolarAxes.PolarExponentOffset = 5.0
streamTracer1Display.PolarAxes.RadialTitleVisibility = 1
streamTracer1Display.PolarAxes.RadialTitleFormat = '%-#3.1f'
streamTracer1Display.PolarAxes.RadialTitleLocation = 'Bottom'
streamTracer1Display.PolarAxes.RadialTitleOffset = [20.0, 0.0]
streamTracer1Display.PolarAxes.RadialUnitsVisibility = 1
streamTracer1Display.PolarAxes.ScreenSize = 10.0
streamTracer1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
streamTracer1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
streamTracer1Display.PolarAxes.PolarAxisTitleFontFile = ''
streamTracer1Display.PolarAxes.PolarAxisTitleBold = 0
streamTracer1Display.PolarAxes.PolarAxisTitleItalic = 0
streamTracer1Display.PolarAxes.PolarAxisTitleShadow = 0
streamTracer1Display.PolarAxes.PolarAxisTitleFontSize = 12
streamTracer1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
streamTracer1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
streamTracer1Display.PolarAxes.PolarAxisLabelFontFile = ''
streamTracer1Display.PolarAxes.PolarAxisLabelBold = 0
streamTracer1Display.PolarAxes.PolarAxisLabelItalic = 0
streamTracer1Display.PolarAxes.PolarAxisLabelShadow = 0
streamTracer1Display.PolarAxes.PolarAxisLabelFontSize = 12
streamTracer1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
streamTracer1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
streamTracer1Display.PolarAxes.LastRadialAxisTextFontFile = ''
streamTracer1Display.PolarAxes.LastRadialAxisTextBold = 0
streamTracer1Display.PolarAxes.LastRadialAxisTextItalic = 0
streamTracer1Display.PolarAxes.LastRadialAxisTextShadow = 0
streamTracer1Display.PolarAxes.LastRadialAxisTextFontSize = 12
streamTracer1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
streamTracer1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
streamTracer1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
streamTracer1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
streamTracer1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
streamTracer1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
streamTracer1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
streamTracer1Display.PolarAxes.EnableDistanceLOD = 1
streamTracer1Display.PolarAxes.DistanceLODThreshold = 0.7
streamTracer1Display.PolarAxes.EnableViewAngleLOD = 1
streamTracer1Display.PolarAxes.ViewAngleLODThreshold = 0.7
streamTracer1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
streamTracer1Display.PolarAxes.PolarTicksVisibility = 1
streamTracer1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
streamTracer1Display.PolarAxes.TickLocation = 'Both'
streamTracer1Display.PolarAxes.AxisTickVisibility = 1
streamTracer1Display.PolarAxes.AxisMinorTickVisibility = 0
streamTracer1Display.PolarAxes.AxisTickMatchesPolarAxes = 1
streamTracer1Display.PolarAxes.DeltaRangeMajor = 1.0
streamTracer1Display.PolarAxes.DeltaRangeMinor = 0.5
streamTracer1Display.PolarAxes.ArcTickVisibility = 1
streamTracer1Display.PolarAxes.ArcMinorTickVisibility = 0
streamTracer1Display.PolarAxes.ArcTickMatchesRadialAxes = 1
streamTracer1Display.PolarAxes.DeltaAngleMajor = 10.0
streamTracer1Display.PolarAxes.DeltaAngleMinor = 5.0
streamTracer1Display.PolarAxes.TickRatioRadiusSize = 0.02
streamTracer1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
streamTracer1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
streamTracer1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
streamTracer1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
streamTracer1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
streamTracer1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
streamTracer1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
streamTracer1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
streamTracer1Display.PolarAxes.ArcMajorTickSize = 0.0
streamTracer1Display.PolarAxes.ArcTickRatioSize = 0.3
streamTracer1Display.PolarAxes.ArcMajorTickThickness = 1.0
streamTracer1Display.PolarAxes.ArcTickRatioThickness = 0.5
streamTracer1Display.PolarAxes.Use2DMode = 0
streamTracer1Display.PolarAxes.UseLogAxis = 0

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.165083872052435, 8.262600003608298, 20.098829976814834]
renderView1.CameraFocalPoint = [45.9870986938476, 14.027099609374961, -10.2000000029803]
renderView1.CameraViewUp = [0.10902048533691928, -0.9867682208936517, -0.12001254939080373]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.165083872052435, 8.262600003608298, 20.098829976814834]
renderView1.CameraFocalPoint = [45.9870986938476, 14.027099609374961, -10.2000000029803]
renderView1.CameraViewUp = [0.10902048533691928, -0.9867682208936517, -0.12001254939080373]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.165083872052435, 8.262600003608298, 20.098829976814834]
renderView1.CameraFocalPoint = [45.9870986938476, 14.027099609374961, -10.2000000029803]
renderView1.CameraViewUp = [0.10902048533691928, -0.9867682208936517, -0.12001254939080373]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.165083872052435, 8.262600003608298, 20.098829976814834]
renderView1.CameraFocalPoint = [45.9870986938476, 14.027099609374961, -10.2000000029803]
renderView1.CameraViewUp = [0.10902048533691928, -0.9867682208936517, -0.12001254939080373]
renderView1.CameraParallelScale = 11.315476125271417

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.165083872052435, 8.262600003608298, 20.098829976814834]
renderView1.CameraFocalPoint = [45.9870986938476, 14.027099609374961, -10.2000000029803]
renderView1.CameraViewUp = [0.10902048533691928, -0.9867682208936517, -0.12001254939080373]
renderView1.CameraParallelScale = 11.315476125271417

# set scalar coloring
ColorBy(streamTracer1Display, ('POINTS', 'velocity', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
streamTracer1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, True)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.165083872052435, 8.262600003608298, 20.098829976814834]
renderView1.CameraFocalPoint = [45.9870986938476, 14.027099609374961, -10.2000000029803]
renderView1.CameraViewUp = [0.10902048533691928, -0.9867682208936517, -0.12001254939080373]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [40.25431245195003, 0.971086716170893, 22.999284402538123]
renderView1.CameraFocalPoint = [45.98709869384761, 14.027099609374963, -10.2000000029803]
renderView1.CameraViewUp = [0.5376309336608107, -0.8121722935179749, -0.2265593626685008]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [33.93246673917735, 13.571029353068251, 23.858694102344067]
renderView1.CameraFocalPoint = [45.987098693847614, 14.027099609374945, -10.200000002980287]
renderView1.CameraViewUp = [0.4417162175386144, -0.8854442112787828, 0.1444829812686386]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [33.93246673917735, 13.571029353068251, 23.858694102344067]
renderView1.CameraFocalPoint = [45.987098693847614, 14.027099609374945, -10.200000002980287]
renderView1.CameraViewUp = [0.4417162175386144, -0.8854442112787828, 0.1444829812686386]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [33.93246673917735, 13.571029353068251, 23.858694102344067]
renderView1.CameraFocalPoint = [45.987098693847614, 14.027099609374945, -10.200000002980287]
renderView1.CameraViewUp = [0.4417162175386144, -0.8854442112787828, 0.1444829812686386]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [33.93246673917735, 13.571029353068251, 23.858694102344067]
renderView1.CameraFocalPoint = [45.987098693847614, 14.027099609374945, -10.200000002980287]
renderView1.CameraViewUp = [0.4417162175386144, -0.8854442112787828, 0.1444829812686386]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [33.93246673917735, 13.571029353068251, 23.858694102344067]
renderView1.CameraFocalPoint = [45.987098693847614, 14.027099609374945, -10.200000002980287]
renderView1.CameraViewUp = [0.4417162175386144, -0.8854442112787828, 0.1444829812686386]
renderView1.CameraParallelScale = 11.315476125271417

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [33.93246673917735, 13.571029353068251, 23.858694102344067]
renderView1.CameraFocalPoint = [45.987098693847614, 14.027099609374945, -10.200000002980287]
renderView1.CameraViewUp = [0.4417162175386144, -0.8854442112787828, 0.1444829812686386]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [33.93246673917735, 13.571029353068251, 23.858694102344067]
renderView1.CameraFocalPoint = [45.987098693847614, 14.027099609374945, -10.200000002980287]
renderView1.CameraViewUp = [0.4417162175386144, -0.8854442112787828, 0.1444829812686386]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [52.78035325200158, -11.75905281364736, -34.581198323121846]
renderView1.CameraFocalPoint = [45.98709869384771, 14.027099609375096, -10.200000002980234]
renderView1.CameraViewUp = [0.9756220743911299, 0.2148844217065139, 0.04456740141185803]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [42.505453088113114, -9.726635219002238, -37.20287061668553]
renderView1.CameraFocalPoint = [45.987098693847734, 14.027099609375083, -10.20000000298024]
renderView1.CameraViewUp = [0.9879388929867671, 0.02826280856360684, -0.15224308646430615]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [42.505453088113114, -9.726635219002238, -37.20287061668553]
renderView1.CameraFocalPoint = [45.987098693847734, 14.027099609375083, -10.20000000298024]
renderView1.CameraViewUp = [0.9879388929867671, 0.02826280856360684, -0.15224308646430615]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [42.505453088113114, -9.726635219002238, -37.20287061668553]
renderView1.CameraFocalPoint = [45.987098693847734, 14.027099609375083, -10.20000000298024]
renderView1.CameraViewUp = [0.9879388929867671, 0.02826280856360684, -0.15224308646430615]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.01714426425304, -16.9602901101424, -28.677493169461734]
renderView1.CameraFocalPoint = [45.987098693847756, 14.027099609375073, -10.200000002980254]
renderView1.CameraViewUp = [0.9983618632587437, -0.05572012679884583, -0.012994516537762341]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.35903718178601, -11.582313381961677, -25.47065551246908]
renderView1.CameraFocalPoint = [45.987098693847756, 14.027099609375073, -10.200000002980254]
renderView1.CameraViewUp = [0.9983618632587437, -0.05572012679884583, -0.012994516537762341]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.64159331197854, -7.137704515696617, -22.82037645710325]
renderView1.CameraFocalPoint = [45.987098693847756, 14.027099609375073, -10.200000002980254]
renderView1.CameraViewUp = [0.9983618632587437, -0.05572012679884583, -0.012994516537762341]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.87511077494758, -3.464474047708963, -20.63006318820587]
renderView1.CameraFocalPoint = [45.987098693847756, 14.027099609375073, -10.200000002980254]
renderView1.CameraViewUp = [0.9983618632587437, -0.05572012679884583, -0.012994516537762341]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [46.02093145684244, 9.777810215092892, -30.14793922407682]
renderView1.CameraFocalPoint = [45.98709869384775, 14.02709960937508, -10.200000002980191]
renderView1.CameraViewUp = [0.9999924067690851, -0.0031033005288440933, 0.0023571020343529877]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [48.93154152869321, 7.016394604453336, -29.125066869627403]
renderView1.CameraFocalPoint = [45.98709869384775, 14.027099609375092, -10.20000000298019]
renderView1.CameraViewUp = [0.98941578509239, 0.03626287918594785, 0.14050412023551104]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [48.76972347790933, 7.010692451448336, -29.14742500180513]
renderView1.CameraFocalPoint = [45.98709869384775, 14.02709960937509, -10.20000000298019]
renderView1.CameraViewUp = [0.9905409944222608, 0.033506942199159874, 0.13306323005782195]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [48.76972347790933, 7.010692451448336, -29.14742500180513]
renderView1.CameraFocalPoint = [45.98709869384775, 14.02709960937509, -10.20000000298019]
renderView1.CameraViewUp = [0.9905409944222608, 0.033506942199159874, 0.13306323005782195]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [48.76972347790933, 7.010692451448336, -29.14742500180513]
renderView1.CameraFocalPoint = [45.98709869384775, 14.02709960937509, -10.20000000298019]
renderView1.CameraViewUp = [0.9905409944222608, 0.033506942199159874, 0.13306323005782195]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [48.76972347790933, 7.010692451448336, -29.14742500180513]
renderView1.CameraFocalPoint = [45.98709869384775, 14.02709960937509, -10.20000000298019]
renderView1.CameraViewUp = [0.9905409944222608, 0.033506942199159874, 0.13306323005782195]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [48.76972347790933, 7.010692451448336, -29.14742500180513]
renderView1.CameraFocalPoint = [45.98709869384775, 14.02709960937509, -10.20000000298019]
renderView1.CameraViewUp = [0.9905409944222608, 0.033506942199159874, 0.13306323005782195]
renderView1.CameraParallelScale = 11.315476125271417

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [48.76972347790933, 7.010692451448336, -29.14742500180513]
renderView1.CameraFocalPoint = [45.98709869384775, 14.02709960937509, -10.20000000298019]
renderView1.CameraViewUp = [0.9905409944222608, 0.033506942199159874, 0.13306323005782195]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [50.686410783644206, 8.576168712743737, -29.283545334590315]
renderView1.CameraFocalPoint = [45.9870986938477, 14.02709960937508, -10.20000000298017]
renderView1.CameraViewUp = [0.9586211224656161, -0.10287901299280314, 0.2654457614059585]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [46.54529899822878, 7.361673478898329, -29.467547618079635]
renderView1.CameraFocalPoint = [45.98709869384772, 14.027099609375082, -10.200000002980184]
renderView1.CameraViewUp = [0.9834456775602656, -0.16054180222381306, 0.08402933432296335]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [46.54529899822878, 7.361673478898329, -29.467547618079635]
renderView1.CameraFocalPoint = [45.98709869384772, 14.027099609375082, -10.200000002980184]
renderView1.CameraViewUp = [0.9834456775602656, -0.16054180222381306, 0.08402933432296335]
renderView1.CameraParallelScale = 11.315476125271417

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=streamTracer1.SeedType)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [46.54529899822878, 7.361673478898329, -29.467547618079635]
renderView1.CameraFocalPoint = [45.98709869384772, 14.027099609375082, -10.200000002980184]
renderView1.CameraViewUp = [0.9834456775602656, -0.16054180222381306, 0.08402933432296335]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [46.54529899822878, 7.361673478898329, -29.467547618079635]
renderView1.CameraFocalPoint = [45.98709869384772, 14.027099609375082, -10.200000002980184]
renderView1.CameraViewUp = [0.9834456775602656, -0.16054180222381306, 0.08402933432296335]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [50.53430982930354, 20.559251178559133, -28.97849171417922]
renderView1.CameraFocalPoint = [45.987098693847656, 14.027099609375044, -10.200000002980138]
renderView1.CameraViewUp = [0.9742962271573742, -0.10444807588902977, 0.19959323933937784]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [50.53430982930354, 20.559251178559133, -28.97849171417922]
renderView1.CameraFocalPoint = [45.987098693847656, 14.027099609375044, -10.200000002980138]
renderView1.CameraViewUp = [0.9742962271573742, -0.10444807588902977, 0.19959323933937784]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on streamTracer1
streamTracer1.SeedType = 'Point Cloud'

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [50.53430982930354, 20.559251178559133, -28.97849171417922]
renderView1.CameraFocalPoint = [45.987098693847656, 14.027099609375044, -10.200000002980138]
renderView1.CameraViewUp = [0.9742962271573742, -0.10444807588902977, 0.19959323933937784]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [53.24349201956792, 3.121513777436859, -25.833004760398115]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375073, -10.200000002980213]
renderView1.CameraViewUp = [0.6704995238328483, -0.42529318302268215, 0.6079112575157326]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [47.623754295882954, 5.393044141775064, -28.605225587131955]
renderView1.CameraFocalPoint = [45.987098693847706, 14.027099609375062, -10.200000002980211]
renderView1.CameraViewUp = [0.744613748134387, -0.5764057692645199, 0.336610687958414]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [47.623754295882954, 5.393044141775064, -28.605225587131955]
renderView1.CameraFocalPoint = [45.987098693847706, 14.027099609375062, -10.200000002980211]
renderView1.CameraViewUp = [0.744613748134387, -0.5764057692645199, 0.336610687958414]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [47.623754295882954, 5.393044141775064, -28.605225587131955]
renderView1.CameraFocalPoint = [45.987098693847706, 14.027099609375062, -10.200000002980211]
renderView1.CameraViewUp = [0.744613748134387, -0.5764057692645199, 0.336610687958414]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [47.623754295882954, 5.393044141775064, -28.605225587131955]
renderView1.CameraFocalPoint = [45.987098693847706, 14.027099609375062, -10.200000002980211]
renderView1.CameraViewUp = [0.744613748134387, -0.5764057692645199, 0.336610687958414]
renderView1.CameraParallelScale = 11.315476125271417

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [47.623754295882954, 5.393044141775064, -28.605225587131955]
renderView1.CameraFocalPoint = [45.987098693847706, 14.027099609375062, -10.200000002980211]
renderView1.CameraViewUp = [0.744613748134387, -0.5764057692645199, 0.336610687958414]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [47.623754295882954, 5.393044141775064, -28.605225587131955]
renderView1.CameraFocalPoint = [45.987098693847706, 14.027099609375062, -10.200000002980211]
renderView1.CameraViewUp = [0.744613748134387, -0.5764057692645199, 0.336610687958414]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [47.623754295882954, 5.393044141775064, -28.605225587131955]
renderView1.CameraFocalPoint = [45.987098693847706, 14.027099609375062, -10.200000002980211]
renderView1.CameraViewUp = [0.744613748134387, -0.5764057692645199, 0.336610687958414]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [47.623754295882954, 5.393044141775064, -28.605225587131955]
renderView1.CameraFocalPoint = [45.987098693847706, 14.027099609375062, -10.200000002980211]
renderView1.CameraViewUp = [0.744613748134387, -0.5764057692645199, 0.336610687958414]
renderView1.CameraParallelScale = 11.315476125271417

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [47.623754295882954, 5.393044141775064, -28.605225587131955]
renderView1.CameraFocalPoint = [45.987098693847706, 14.027099609375062, -10.200000002980211]
renderView1.CameraViewUp = [0.744613748134387, -0.5764057692645199, 0.336610687958414]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [46.53545628728542, 3.225924384066297, -27.491957725652252]
renderView1.CameraFocalPoint = [45.98709869384772, 14.027099609375048, -10.200000002980222]
renderView1.CameraViewUp = [0.7370547090385249, -0.5624503287529167, 0.37469985797951905]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [46.53545628728542, 3.225924384066297, -27.491957725652252]
renderView1.CameraFocalPoint = [45.98709869384772, 14.027099609375048, -10.200000002980222]
renderView1.CameraViewUp = [0.7370547090385249, -0.5624503287529167, 0.37469985797951905]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [46.53545628728542, 3.225924384066297, -27.491957725652252]
renderView1.CameraFocalPoint = [45.98709869384772, 14.027099609375048, -10.200000002980222]
renderView1.CameraViewUp = [0.7370547090385249, -0.5624503287529167, 0.37469985797951905]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [46.53545628728542, 3.225924384066297, -27.491957725652252]
renderView1.CameraFocalPoint = [45.98709869384772, 14.027099609375048, -10.200000002980222]
renderView1.CameraViewUp = [0.7370547090385249, -0.5624503287529167, 0.37469985797951905]
renderView1.CameraParallelScale = 11.315476125271417

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [46.53545628728542, 3.225924384066297, -27.491957725652252]
renderView1.CameraFocalPoint = [45.98709869384772, 14.027099609375048, -10.200000002980222]
renderView1.CameraViewUp = [0.7370547090385249, -0.5624503287529167, 0.37469985797951905]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [49.57125496285226, -6.044311901122857, -10.71975763533355]
renderView1.CameraFocalPoint = [45.98709869384771, 14.027099609375066, -10.200000002980223]
renderView1.CameraViewUp = [0.353789256000039, 0.03897662460957366, 0.9345126992572028]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [49.57125496285226, -6.044311901122857, -10.71975763533355]
renderView1.CameraFocalPoint = [45.98709869384771, 14.027099609375066, -10.200000002980223]
renderView1.CameraViewUp = [0.353789256000039, 0.03897662460957366, 0.9345126992572028]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [49.57125496285226, -6.044311901122857, -10.71975763533355]
renderView1.CameraFocalPoint = [45.98709869384771, 14.027099609375066, -10.200000002980223]
renderView1.CameraViewUp = [0.353789256000039, 0.03897662460957366, 0.9345126992572028]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [49.57125496285226, -6.044311901122857, -10.71975763533355]
renderView1.CameraFocalPoint = [45.98709869384771, 14.027099609375066, -10.200000002980223]
renderView1.CameraViewUp = [0.353789256000039, 0.03897662460957366, 0.9345126992572028]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [49.57125496285226, -6.044311901122857, -10.71975763533355]
renderView1.CameraFocalPoint = [45.98709869384771, 14.027099609375066, -10.200000002980223]
renderView1.CameraViewUp = [0.353789256000039, 0.03897662460957366, 0.9345126992572028]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [49.57125496285226, -6.044311901122857, -10.71975763533355]
renderView1.CameraFocalPoint = [45.98709869384771, 14.027099609375066, -10.200000002980223]
renderView1.CameraViewUp = [0.353789256000039, 0.03897662460957366, 0.9345126992572028]
renderView1.CameraParallelScale = 11.315476125271417

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [49.57125496285226, -6.044311901122857, -10.71975763533355]
renderView1.CameraFocalPoint = [45.98709869384771, 14.027099609375066, -10.200000002980223]
renderView1.CameraViewUp = [0.353789256000039, 0.03897662460957366, 0.9345126992572028]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [49.57125496285226, -6.044311901122857, -10.71975763533355]
renderView1.CameraFocalPoint = [45.98709869384771, 14.027099609375066, -10.200000002980223]
renderView1.CameraViewUp = [0.353789256000039, 0.03897662460957366, 0.9345126992572028]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [49.57125496285226, -6.044311901122857, -10.71975763533355]
renderView1.CameraFocalPoint = [45.98709869384771, 14.027099609375066, -10.200000002980223]
renderView1.CameraViewUp = [0.353789256000039, 0.03897662460957366, 0.9345126992572028]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [64.8876850814244, 6.8478278060796915, -12.883984868984223]
renderView1.CameraFocalPoint = [45.987098693847635, 14.027099609375082, -10.200000002980204]
renderView1.CameraViewUp = [0.17996077758796278, 0.10826129609660781, 0.9776981181824064]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [61.15987730886224, 20.114518192867084, 1.9945893000628183]
renderView1.CameraFocalPoint = [45.98709869384758, 14.027099609375028, -10.200000002980246]
renderView1.CameraViewUp = [-0.5815285847753544, -0.15166952335263614, 0.7992626982257822]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [36.00936654741067, 31.744952573101443, -8.618724647291396]
renderView1.CameraFocalPoint = [45.987098693847635, 14.027099609374922, -10.200000002980248]
renderView1.CameraViewUp = [-0.4878718032586053, -0.34625726812775637, 0.8013033182596337]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [37.91894688677935, 3.5045957232884857, -25.69708755407132]
renderView1.CameraFocalPoint = [45.987098693847706, 14.02709960937495, -10.200000002980154]
renderView1.CameraViewUp = [-0.9153824355318124, 0.2888169869431113, 0.2804634464113819]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.23023002207169, -0.4046756063941718, -24.504375584334063]
renderView1.CameraFocalPoint = [45.98709869384768, 14.02709960937497, -10.200000002980138]
renderView1.CameraViewUp = [-0.9961954131369266, 0.07051138433875936, 0.051213704450857475]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.23023002207169, -0.4046756063941718, -24.504375584334063]
renderView1.CameraFocalPoint = [45.98709869384768, 14.02709960937497, -10.200000002980138]
renderView1.CameraViewUp = [-0.9961954131369267, 0.07051138433875938, 0.05121370445085748]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.23023002207169, -0.4046756063941718, -24.504375584334063]
renderView1.CameraFocalPoint = [45.98709869384768, 14.02709960937497, -10.200000002980138]
renderView1.CameraViewUp = [-0.9961954131369267, 0.07051138433875938, 0.05121370445085748]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.23023002207169, -0.4046756063941718, -24.504375584334063]
renderView1.CameraFocalPoint = [45.98709869384768, 14.02709960937497, -10.200000002980138]
renderView1.CameraViewUp = [-0.9961954131369267, 0.07051138433875938, 0.05121370445085748]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.23023002207169, -0.4046756063941718, -24.504375584334063]
renderView1.CameraFocalPoint = [45.98709869384768, 14.02709960937497, -10.200000002980138]
renderView1.CameraViewUp = [-0.9961954131369267, 0.07051138433875938, 0.05121370445085748]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.23023002207169, -0.4046756063941718, -24.504375584334063]
renderView1.CameraFocalPoint = [45.98709869384768, 14.02709960937497, -10.200000002980138]
renderView1.CameraViewUp = [-0.9961954131369267, 0.07051138433875938, 0.05121370445085748]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.23023002207169, -0.4046756063941718, -24.504375584334063]
renderView1.CameraFocalPoint = [45.98709869384768, 14.02709960937497, -10.200000002980138]
renderView1.CameraViewUp = [-0.9961954131369267, 0.07051138433875938, 0.05121370445085748]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.23023002207169, -0.4046756063941718, -24.504375584334063]
renderView1.CameraFocalPoint = [45.98709869384768, 14.02709960937497, -10.200000002980138]
renderView1.CameraViewUp = [-0.9961954131369267, 0.07051138433875938, 0.05121370445085748]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.23023002207169, -0.4046756063941718, -24.504375584334063]
renderView1.CameraFocalPoint = [45.98709869384768, 14.02709960937497, -10.200000002980138]
renderView1.CameraViewUp = [-0.9961954131369267, 0.07051138433875938, 0.05121370445085748]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.23023002207169, -0.4046756063941718, -24.504375584334063]
renderView1.CameraFocalPoint = [45.98709869384768, 14.02709960937497, -10.200000002980138]
renderView1.CameraViewUp = [-0.9961954131369267, 0.07051138433875938, 0.05121370445085748]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.23023002207169, -0.4046756063941718, -24.504375584334063]
renderView1.CameraFocalPoint = [45.98709869384768, 14.02709960937497, -10.200000002980138]
renderView1.CameraViewUp = [-0.9961954131369267, 0.07051138433875938, 0.05121370445085748]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.23023002207169, -0.4046756063941718, -24.504375584334063]
renderView1.CameraFocalPoint = [45.98709869384768, 14.02709960937497, -10.200000002980138]
renderView1.CameraViewUp = [-0.9961954131369267, 0.07051138433875938, 0.05121370445085748]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.23023002207169, -0.4046756063941718, -24.504375584334063]
renderView1.CameraFocalPoint = [45.98709869384768, 14.02709960937497, -10.200000002980138]
renderView1.CameraViewUp = [-0.9961954131369267, 0.07051138433875938, 0.05121370445085748]
renderView1.CameraParallelScale = 11.315476125271417

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.23023002207169, -0.4046756063941718, -24.504375584334063]
renderView1.CameraFocalPoint = [45.98709869384768, 14.02709960937497, -10.200000002980138]
renderView1.CameraViewUp = [-0.9961954131369267, 0.07051138433875938, 0.05121370445085748]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [44.23023002207169, -0.4046756063941718, -24.504375584334063]
renderView1.CameraFocalPoint = [45.98709869384768, 14.02709960937497, -10.200000002980138]
renderView1.CameraViewUp = [-0.9961954131369267, 0.07051138433875938, 0.05121370445085748]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [59.09586604724114, 2.4182661534763357, 0.25815893865956946]
renderView1.CameraFocalPoint = [45.987098693847614, 14.027099609375098, -10.200000002980204]
renderView1.CameraViewUp = [-0.7611714975839743, -0.5502196662163994, 0.3433311377875357]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [61.84870719145378, -0.019588872262403356, 2.454372316403921]
renderView1.CameraFocalPoint = [45.987098693847614, 14.027099609375098, -10.200000002980204]
renderView1.CameraViewUp = [-0.7611714975839743, -0.5502196662163994, 0.3433311377875357]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [65.17964497595108, -2.9693934534062816, 5.111790503474589]
renderView1.CameraFocalPoint = [45.987098693847614, 14.027099609375098, -10.200000002980204]
renderView1.CameraViewUp = [-0.7611714975839743, -0.5502196662163994, 0.3433311377875357]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [69.2100796951928, -6.538656996590371, 8.327266509830096]
renderView1.CameraFocalPoint = [45.987098693847614, 14.027099609375098, -10.200000002980204]
renderView1.CameraViewUp = [-0.7611714975839743, -0.5502196662163994, 0.3433311377875357]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [45.448733234720976, -12.349858884703288, 14.487709875326466]
renderView1.CameraFocalPoint = [45.98709869384767, 14.027099609375103, -10.200000002980222]
renderView1.CameraViewUp = [-0.9903712835369899, -0.08328553729202158, -0.1105813728585183]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [45.33567648830437, -17.88902016845975, 19.67212894977087]
renderView1.CameraFocalPoint = [45.98709869384767, 14.027099609375103, -10.200000002980222]
renderView1.CameraViewUp = [-0.9903712835369899, -0.08328553729202158, -0.1105813728585183]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [45.19887782514028, -24.591405321805073, 25.945276029848603]
renderView1.CameraFocalPoint = [45.98709869384767, 14.027099609375103, -10.200000002980222]
renderView1.CameraViewUp = [-0.9903712835369899, -0.08328553729202158, -0.1105813728585183]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [36.7274745602181, -24.983022539394728, 24.31030172836973]
renderView1.CameraFocalPoint = [45.987098693847656, 14.027099609375098, -10.200000002980216]
renderView1.CameraViewUp = [-0.9676209782562353, 0.006459709717306167, -0.25232501776243793]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [51.31736318388538, -23.765699263628647, 26.430367570356832]
renderView1.CameraFocalPoint = [45.98709869384763, 14.027099609375096, -10.200000002980214]
renderView1.CameraViewUp = [-0.9782430020194184, -0.19800144660098384, -0.06193590351285859]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [33.71211083159409, -35.57043257807801, 3.5076864773467618]
renderView1.CameraFocalPoint = [45.98709869384764, 14.027099609375089, -10.200000002980177]
renderView1.CameraViewUp = [-0.9396263146525131, 0.1471651749433805, -0.3089414185511885]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [33.71211083159409, -35.57043257807801, 3.5076864773467618]
renderView1.CameraFocalPoint = [45.98709869384764, 14.027099609375089, -10.200000002980177]
renderView1.CameraViewUp = [-0.9396263146525131, 0.1471651749433805, -0.3089414185511885]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [33.71211083159409, -35.57043257807801, 3.5076864773467618]
renderView1.CameraFocalPoint = [45.98709869384764, 14.027099609375089, -10.200000002980177]
renderView1.CameraViewUp = [-0.9396263146525131, 0.1471651749433805, -0.3089414185511885]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [33.71211083159409, -35.57043257807801, 3.5076864773467618]
renderView1.CameraFocalPoint = [45.98709869384764, 14.027099609375089, -10.200000002980177]
renderView1.CameraViewUp = [-0.9396263146525131, 0.1471651749433805, -0.3089414185511885]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [33.71211083159409, -35.57043257807801, 3.5076864773467618]
renderView1.CameraFocalPoint = [45.98709869384764, 14.027099609375089, -10.200000002980177]
renderView1.CameraViewUp = [-0.9396263146525131, 0.1471651749433805, -0.3089414185511885]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [33.71211083159409, -35.57043257807801, 3.5076864773467618]
renderView1.CameraFocalPoint = [45.98709869384764, 14.027099609375089, -10.200000002980177]
renderView1.CameraViewUp = [-0.9396263146525131, 0.1471651749433805, -0.3089414185511885]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [33.71211083159409, -35.57043257807801, 3.5076864773467618]
renderView1.CameraFocalPoint = [45.98709869384764, 14.027099609375089, -10.200000002980177]
renderView1.CameraViewUp = [-0.9396263146525131, 0.1471651749433805, -0.3089414185511885]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [33.71211083159409, -35.57043257807801, 3.5076864773467618]
renderView1.CameraFocalPoint = [45.98709869384764, 14.027099609375089, -10.200000002980177]
renderView1.CameraViewUp = [-0.9396263146525131, 0.1471651749433805, -0.3089414185511885]
renderView1.CameraParallelScale = 11.315476125271417

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [33.71211083159409, -35.57043257807801, 3.5076864773467618]
renderView1.CameraFocalPoint = [45.98709869384764, 14.027099609375089, -10.200000002980177]
renderView1.CameraViewUp = [-0.9396263146525131, 0.1471651749433805, -0.3089414185511885]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [11.967957535906868, -26.26621221835655, -14.399791852125356]
renderView1.CameraFocalPoint = [45.987098693847614, 14.027099609375071, -10.200000002980172]
renderView1.CameraViewUp = [-0.5905541206431943, 0.5592393232173742, -0.5818051305709815]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [17.872106001334608, -19.273158099494026, -13.670902357645613]
renderView1.CameraFocalPoint = [45.987098693847614, 14.027099609375071, -10.200000002980172]
renderView1.CameraViewUp = [-0.5905541206431943, 0.5592393232173742, -0.5818051305709815]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.561348388896896, -22.1291407960417, 14.25913235972898]
renderView1.CameraFocalPoint = [45.987098693847614, 14.027099609375089, -10.20000000298019]
renderView1.CameraViewUp = [-0.9756293755390597, -0.074230054859694, -0.206487821773565]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.98234637570653, -15.854090808324731, 10.0141589744654]
renderView1.CameraFocalPoint = [45.987098693847614, 14.027099609375089, -10.20000000298019]
renderView1.CameraViewUp = [-0.9756293755390597, -0.074230054859694, -0.206487821773565]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.98234637570653, -15.854090808324731, 10.0141589744654]
renderView1.CameraFocalPoint = [45.987098693847614, 14.027099609375089, -10.20000000298019]
renderView1.CameraViewUp = [-0.9756293755390597, -0.074230054859694, -0.206487821773565]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.98234637570653, -15.854090808324731, 10.0141589744654]
renderView1.CameraFocalPoint = [45.987098693847614, 14.027099609375089, -10.20000000298019]
renderView1.CameraViewUp = [-0.9756293755390597, -0.074230054859694, -0.206487821773565]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [47.52592044217667, -21.389903716497795, -3.2153955873130506]
renderView1.CameraFocalPoint = [45.98709869384763, 14.027099609375075, -10.200000002980154]
renderView1.CameraViewUp = [-0.9748451748837398, -0.08313822698858293, -0.2067968090157236]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.64246619181395, -12.62353537100212, 14.085039617627286]
renderView1.CameraFocalPoint = [45.98709869384763, 14.027099609375103, -10.200000002980216]
renderView1.CameraViewUp = [-0.9668457810493476, -0.12022965619493939, -0.22528662951521058]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.64246619181395, -12.62353537100212, 14.085039617627286]
renderView1.CameraFocalPoint = [45.98709869384763, 14.027099609375103, -10.200000002980216]
renderView1.CameraViewUp = [-0.9668457810493476, -0.12022965619493939, -0.22528662951521058]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.64246619181395, -12.62353537100212, 14.085039617627286]
renderView1.CameraFocalPoint = [45.98709869384763, 14.027099609375103, -10.200000002980216]
renderView1.CameraViewUp = [-0.9668457810493476, -0.12022965619493939, -0.22528662951521058]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.64246619181395, -12.62353537100212, 14.085039617627286]
renderView1.CameraFocalPoint = [45.98709869384763, 14.027099609375103, -10.200000002980216]
renderView1.CameraViewUp = [-0.9668457810493476, -0.12022965619493939, -0.22528662951521058]
renderView1.CameraParallelScale = 11.315476125271417

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.64246619181395, -12.62353537100212, 14.085039617627286]
renderView1.CameraFocalPoint = [45.98709869384763, 14.027099609375103, -10.200000002980216]
renderView1.CameraViewUp = [-0.9668457810493476, -0.12022965619493939, -0.22528662951521058]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [51.40420780512384, -14.457995501990638, 11.358550068264336]
renderView1.CameraFocalPoint = [45.98709869384766, 14.027099609375133, -10.200000002980207]
renderView1.CameraViewUp = [-0.8298574852366503, -0.4283946305968167, -0.3575116706801608]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on streamTracer1
streamTracer1.IntegrationDirection = 'FORWARD'

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on streamTracer1
streamTracer1.IntegrationDirection = 'BACKWARD'

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on streamTracer1
streamTracer1.IntegrationDirection = 'BOTH'

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on streamTracer1
streamTracer1.IntegratorType = 'Runge-Kutta 4'

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on streamTracer1
streamTracer1.IntegratorType = 'Runge-Kutta 2'

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417

# set active source
SetActiveSource(calculator1)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=calculator1Display.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=calculator1Display)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=calculator1Display.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=calculator1Display)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=streamTracer1.SeedType)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417

# hide data in view
Hide(streamTracer1, renderView1)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417

# set active source
SetActiveSource(streamTracer1)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=streamTracer1.SeedType)

# show data in view
streamTracer1Display = Show(streamTracer1, renderView1, 'GeometryRepresentation')

# show color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, True)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417

# hide data in view
Hide(streamTracer1, renderView1)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=streamTracer1)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.UseDual = 0
slice1.Crinkleslice = 0
slice1.Triangulatetheslice = 1
slice1.SliceOffsetValues = [0.0]
slice1.PointMergeMethod = 'Uniform Binning'

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [45.992937088012695, 14.01739501953125, -10.705812215805054]
slice1.SliceType.Normal = [1.0, 0.0, 0.0]
slice1.SliceType.Offset = 0.0

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [45.992937088012695, 14.01739501953125, -10.705812215805054]
slice1.HyperTreeGridSlicer.Normal = [1.0, 0.0, 0.0]
slice1.HyperTreeGridSlicer.Offset = 0.0

# init the 'Uniform Binning' selected for 'PointMergeMethod'
slice1.PointMergeMethod.Divisions = [50, 50, 50]
slice1.PointMergeMethod.Numberofpointsperbucket = 8
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.37095520677982, -20.266284782685883, 0.8741309333418409]
renderView1.CameraFocalPoint = [45.98709869384768, 14.027099609375131, -10.200000002980154]
renderView1.CameraViewUp = [-0.8377637879353499, -0.10887537619684348, -0.535068208812867]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [54.2993318596307, -20.367308411678255, -2.8891674593951384]
renderView1.CameraFocalPoint = [45.98709869384764, 14.027099609375139, -10.200000002980133]
renderView1.CameraViewUp = [-0.7927602588885768, -0.3038994755036555, -0.5283713473642567]
renderView1.CameraParallelScale = 11.315476125271417

# show data in view
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice1Display.Selection = None
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['POINTS', 'velocity']
slice1Display.LookupTable = velocityLUT
slice1Display.MapScalars = 1
slice1Display.MultiComponentsMapping = 0
slice1Display.InterpolateScalarsBeforeMapping = 1
slice1Display.UseNanColorForMissingArrays = 0
slice1Display.Opacity = 1.0
slice1Display.PointSize = 2.0
slice1Display.LineWidth = 1.0
slice1Display.RenderLinesAsTubes = 0
slice1Display.RenderPointsAsSpheres = 0
slice1Display.DisableLighting = 0
slice1Display.Diffuse = 1.0
slice1Display.Interpolation = 'Gouraud'
slice1Display.Specular = 0.0
slice1Display.SpecularColor = [1.0, 1.0, 1.0]
slice1Display.SpecularPower = 100.0
slice1Display.Luminosity = 0.0
slice1Display.Ambient = 0.0
slice1Display.Roughness = 0.3
slice1Display.Metallic = 0.0
slice1Display.EdgeTint = [1.0, 1.0, 1.0]
slice1Display.Anisotropy = 0.0
slice1Display.AnisotropyRotation = 0.0
slice1Display.BaseIOR = 1.5
slice1Display.CoatStrength = 0.0
slice1Display.CoatIOR = 2.0
slice1Display.CoatRoughness = 0.0
slice1Display.CoatColor = [1.0, 1.0, 1.0]
slice1Display.SelectNormalArray = 'None'
slice1Display.SelectTangentArray = 'None'
slice1Display.ComputePointNormals = 0
slice1Display.Splitting = 1
slice1Display.FeatureAngle = 30.0
slice1Display.SelectTCoordArray = 'None'
slice1Display.Texture = None
slice1Display.RepeatTextures = 1
slice1Display.InterpolateTextures = 0
slice1Display.SeamlessU = 0
slice1Display.SeamlessV = 0
slice1Display.UseMipmapTextures = 0
slice1Display.ShowTexturesOnBackface = 1
slice1Display.BaseColorTexture = None
slice1Display.NormalTexture = None
slice1Display.NormalScale = 1.0
slice1Display.CoatNormalTexture = None
slice1Display.CoatNormalScale = 1.0
slice1Display.MaterialTexture = None
slice1Display.OcclusionStrength = 1.0
slice1Display.AnisotropyTexture = None
slice1Display.EmissiveTexture = None
slice1Display.EmissiveFactor = [1.0, 1.0, 1.0]
slice1Display.TextureTransform = 'Transform2'
slice1Display.EdgeOpacity = 1.0
slice1Display.BackfaceRepresentation = 'Follow Frontface'
slice1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
slice1Display.BackfaceOpacity = 1.0
slice1Display.Translation = [0.0, 0.0, 0.0]
slice1Display.Scale = [1.0, 1.0, 1.0]
slice1Display.Orientation = [0.0, 0.0, 0.0]
slice1Display.Origin = [0.0, 0.0, 0.0]
slice1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
slice1Display.Pickable = 1
slice1Display.Triangulate = 0
slice1Display.UseShaderReplacements = 0
slice1Display.ShaderReplacements = ''
slice1Display.NonlinearSubdivisionLevel = 1
slice1Display.MatchBoundariesIgnoringCellOrder = 0
slice1Display.UseDataPartitions = 0
slice1Display.OSPRayUseScaleArray = 'All Approximate'
slice1Display.OSPRayScaleArray = 'AngularVelocity'
slice1Display.OSPRayScaleFunction = 'Piecewise Function'
slice1Display.OSPRayMaterial = 'None'
slice1Display.Assembly = ''
slice1Display.SelectedBlockSelectors = ['']
slice1Display.BlockSelectors = ['/']
slice1Display.BlockColors = []
slice1Display.BlockColorArrayNames = []
slice1Display.BlockLookupTables = []
slice1Display.BlockUseSeparateColorMaps = []
slice1Display.BlockMapScalars = []
slice1Display.BlockInterpolateScalarsBeforeMappings = []
slice1Display.BlockOpacities = []
slice1Display.BlockMapScalarsGUI = 1
slice1Display.BlockInterpolateScalarsBeforeMappingsGUI = 1
slice1Display.BlockOpacitiesGUI = 1.0
slice1Display.Orient = 0
slice1Display.OrientationMode = 'Direction'
slice1Display.SelectOrientationVectors = 'Normals'
slice1Display.Scaling = 0
slice1Display.ScaleMode = 'No Data Scaling Off'
slice1Display.ScaleFactor = 1.0293911457061768
slice1Display.SelectScaleArray = 'AngularVelocity'
slice1Display.GlyphType = 'Arrow'
slice1Display.UseGlyphTable = 0
slice1Display.GlyphTableIndexArray = 'AngularVelocity'
slice1Display.UseCompositeGlyphTable = 0
slice1Display.UseGlyphCullingAndLOD = 0
slice1Display.LODValues = []
slice1Display.ColorByLODIndex = 0
slice1Display.GaussianRadius = 0.05146955728530884
slice1Display.ShaderPreset = 'Sphere'
slice1Display.CustomTriangleScale = 3
slice1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
slice1Display.Emissive = 0
slice1Display.ScaleByArray = 0
slice1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
slice1Display.ScaleArrayComponent = ''
slice1Display.UseScaleFunction = 1
slice1Display.ScaleTransferFunction = 'Piecewise Function'
slice1Display.OpacityByArray = 0
slice1Display.OpacityArray = ['POINTS', 'AngularVelocity']
slice1Display.OpacityArrayComponent = ''
slice1Display.OpacityTransferFunction = 'Piecewise Function'
slice1Display.DataAxesGrid = 'Grid Axes Representation'
slice1Display.SelectionCellLabelBold = 0
slice1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
slice1Display.SelectionCellLabelFontFamily = 'Arial'
slice1Display.SelectionCellLabelFontFile = ''
slice1Display.SelectionCellLabelFontSize = 18
slice1Display.SelectionCellLabelItalic = 0
slice1Display.SelectionCellLabelJustification = 'Left'
slice1Display.SelectionCellLabelOpacity = 1.0
slice1Display.SelectionCellLabelShadow = 0
slice1Display.SelectionPointLabelBold = 0
slice1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
slice1Display.SelectionPointLabelFontFamily = 'Arial'
slice1Display.SelectionPointLabelFontFile = ''
slice1Display.SelectionPointLabelFontSize = 18
slice1Display.SelectionPointLabelItalic = 0
slice1Display.SelectionPointLabelJustification = 'Left'
slice1Display.SelectionPointLabelOpacity = 1.0
slice1Display.SelectionPointLabelShadow = 0
slice1Display.PolarAxes = 'Polar Axes Representation'
slice1Display.SelectInputVectors = ['POINTS', 'Normals']
slice1Display.NumberOfSteps = 40
slice1Display.StepSize = 0.25
slice1Display.NormalizeVectors = 1
slice1Display.EnhancedLIC = 1
slice1Display.ColorMode = 'Blend'
slice1Display.LICIntensity = 0.8
slice1Display.MapModeBias = 0.0
slice1Display.EnhanceContrast = 'Off'
slice1Display.LowLICContrastEnhancementFactor = 0.0
slice1Display.HighLICContrastEnhancementFactor = 0.0
slice1Display.LowColorContrastEnhancementFactor = 0.0
slice1Display.HighColorContrastEnhancementFactor = 0.0
slice1Display.AntiAlias = 0
slice1Display.MaskOnSurface = 1
slice1Display.MaskThreshold = 0.0
slice1Display.MaskIntensity = 0.0
slice1Display.MaskColor = [0.5, 0.5, 0.5]
slice1Display.GenerateNoiseTexture = 0
slice1Display.NoiseType = 'Gaussian'
slice1Display.NoiseTextureSize = 128
slice1Display.NoiseGrainSize = 2
slice1Display.MinNoiseValue = 0.0
slice1Display.MaxNoiseValue = 0.8
slice1Display.NumberOfNoiseLevels = 1024
slice1Display.ImpulseNoiseProbability = 1.0
slice1Display.ImpulseNoiseBackgroundValue = 0.0
slice1Display.NoiseGeneratorSeed = 1
slice1Display.CompositeStrategy = 'AUTO'
slice1Display.UseLICForLOD = 0
slice1Display.WriteLog = ''

# init the 'Transform2' selected for 'TextureTransform'
slice1Display.TextureTransform.Translate = [0.0, 0.0, 0.0]
slice1Display.TextureTransform.Rotate = [0.0, 0.0, 0.0]
slice1Display.TextureTransform.Scale = [1.0, 1.0, 1.0]

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
slice1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
slice1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
slice1Display.GlyphType.TipResolution = 6
slice1Display.GlyphType.TipRadius = 0.1
slice1Display.GlyphType.TipLength = 0.35
slice1Display.GlyphType.ShaftResolution = 6
slice1Display.GlyphType.ShaftRadius = 0.03
slice1Display.GlyphType.Invert = 0

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [-0.035372445353739554, 0.0, 0.5, 0.0, 0.061625386912687846, 1.0, 0.5, 0.0]
slice1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [-0.035372445353739554, 0.0, 0.5, 0.0, 0.061625386912687846, 1.0, 0.5, 0.0]
slice1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'Grid Axes Representation' selected for 'DataAxesGrid'
slice1Display.DataAxesGrid.XTitle = 'X Axis'
slice1Display.DataAxesGrid.YTitle = 'Y Axis'
slice1Display.DataAxesGrid.ZTitle = 'Z Axis'
slice1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
slice1Display.DataAxesGrid.XTitleFontFile = ''
slice1Display.DataAxesGrid.XTitleBold = 0
slice1Display.DataAxesGrid.XTitleItalic = 0
slice1Display.DataAxesGrid.XTitleFontSize = 12
slice1Display.DataAxesGrid.XTitleShadow = 0
slice1Display.DataAxesGrid.XTitleOpacity = 1.0
slice1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
slice1Display.DataAxesGrid.YTitleFontFile = ''
slice1Display.DataAxesGrid.YTitleBold = 0
slice1Display.DataAxesGrid.YTitleItalic = 0
slice1Display.DataAxesGrid.YTitleFontSize = 12
slice1Display.DataAxesGrid.YTitleShadow = 0
slice1Display.DataAxesGrid.YTitleOpacity = 1.0
slice1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
slice1Display.DataAxesGrid.ZTitleFontFile = ''
slice1Display.DataAxesGrid.ZTitleBold = 0
slice1Display.DataAxesGrid.ZTitleItalic = 0
slice1Display.DataAxesGrid.ZTitleFontSize = 12
slice1Display.DataAxesGrid.ZTitleShadow = 0
slice1Display.DataAxesGrid.ZTitleOpacity = 1.0
slice1Display.DataAxesGrid.FacesToRender = 63
slice1Display.DataAxesGrid.CullBackface = 0
slice1Display.DataAxesGrid.CullFrontface = 1
slice1Display.DataAxesGrid.ShowGrid = 0
slice1Display.DataAxesGrid.ShowEdges = 1
slice1Display.DataAxesGrid.ShowTicks = 1
slice1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
slice1Display.DataAxesGrid.AxesToLabel = 63
slice1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
slice1Display.DataAxesGrid.XLabelFontFile = ''
slice1Display.DataAxesGrid.XLabelBold = 0
slice1Display.DataAxesGrid.XLabelItalic = 0
slice1Display.DataAxesGrid.XLabelFontSize = 12
slice1Display.DataAxesGrid.XLabelShadow = 0
slice1Display.DataAxesGrid.XLabelOpacity = 1.0
slice1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
slice1Display.DataAxesGrid.YLabelFontFile = ''
slice1Display.DataAxesGrid.YLabelBold = 0
slice1Display.DataAxesGrid.YLabelItalic = 0
slice1Display.DataAxesGrid.YLabelFontSize = 12
slice1Display.DataAxesGrid.YLabelShadow = 0
slice1Display.DataAxesGrid.YLabelOpacity = 1.0
slice1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
slice1Display.DataAxesGrid.ZLabelFontFile = ''
slice1Display.DataAxesGrid.ZLabelBold = 0
slice1Display.DataAxesGrid.ZLabelItalic = 0
slice1Display.DataAxesGrid.ZLabelFontSize = 12
slice1Display.DataAxesGrid.ZLabelShadow = 0
slice1Display.DataAxesGrid.ZLabelOpacity = 1.0
slice1Display.DataAxesGrid.XAxisNotation = 'Mixed'
slice1Display.DataAxesGrid.XAxisPrecision = 2
slice1Display.DataAxesGrid.XAxisUseCustomLabels = 0
slice1Display.DataAxesGrid.XAxisLabels = []
slice1Display.DataAxesGrid.YAxisNotation = 'Mixed'
slice1Display.DataAxesGrid.YAxisPrecision = 2
slice1Display.DataAxesGrid.YAxisUseCustomLabels = 0
slice1Display.DataAxesGrid.YAxisLabels = []
slice1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
slice1Display.DataAxesGrid.ZAxisPrecision = 2
slice1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
slice1Display.DataAxesGrid.ZAxisLabels = []
slice1Display.DataAxesGrid.UseCustomBounds = 0
slice1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'Polar Axes Representation' selected for 'PolarAxes'
slice1Display.PolarAxes.Visibility = 0
slice1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
slice1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
slice1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
slice1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
slice1Display.PolarAxes.EnableCustomRange = 0
slice1Display.PolarAxes.CustomRange = [0.0, 1.0]
slice1Display.PolarAxes.AutoPole = 1
slice1Display.PolarAxes.PolarAxisVisibility = 1
slice1Display.PolarAxes.RadialAxesVisibility = 1
slice1Display.PolarAxes.DrawRadialGridlines = 1
slice1Display.PolarAxes.PolarArcsVisibility = 1
slice1Display.PolarAxes.DrawPolarArcsGridlines = 1
slice1Display.PolarAxes.NumberOfRadialAxes = 0
slice1Display.PolarAxes.DeltaAngleRadialAxes = 45.0
slice1Display.PolarAxes.NumberOfPolarAxes = 5
slice1Display.PolarAxes.DeltaRangePolarAxes = 0.0
slice1Display.PolarAxes.CustomMinRadius = 1
slice1Display.PolarAxes.MinimumRadius = 0.0
slice1Display.PolarAxes.CustomMaxRadius = 0
slice1Display.PolarAxes.MaximumRadius = 1.0
slice1Display.PolarAxes.CustomAngles = 1
slice1Display.PolarAxes.MinimumAngle = 0.0
slice1Display.PolarAxes.MaximumAngle = 90.0
slice1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
slice1Display.PolarAxes.PolarArcResolutionPerDegree = 0.2
slice1Display.PolarAxes.Ratio = 1.0
slice1Display.PolarAxes.EnableOverallColor = 1
slice1Display.PolarAxes.OverallColor = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.PolarAxisTitleVisibility = 1
slice1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
slice1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
slice1Display.PolarAxes.PolarTitleOffset = [20.0, 20.0]
slice1Display.PolarAxes.PolarLabelVisibility = 1
slice1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
slice1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
slice1Display.PolarAxes.PolarLabelOffset = 10.0
slice1Display.PolarAxes.PolarExponentOffset = 5.0
slice1Display.PolarAxes.RadialTitleVisibility = 1
slice1Display.PolarAxes.RadialTitleFormat = '%-#3.1f'
slice1Display.PolarAxes.RadialTitleLocation = 'Bottom'
slice1Display.PolarAxes.RadialTitleOffset = [20.0, 0.0]
slice1Display.PolarAxes.RadialUnitsVisibility = 1
slice1Display.PolarAxes.ScreenSize = 10.0
slice1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
slice1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
slice1Display.PolarAxes.PolarAxisTitleFontFile = ''
slice1Display.PolarAxes.PolarAxisTitleBold = 0
slice1Display.PolarAxes.PolarAxisTitleItalic = 0
slice1Display.PolarAxes.PolarAxisTitleShadow = 0
slice1Display.PolarAxes.PolarAxisTitleFontSize = 12
slice1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
slice1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
slice1Display.PolarAxes.PolarAxisLabelFontFile = ''
slice1Display.PolarAxes.PolarAxisLabelBold = 0
slice1Display.PolarAxes.PolarAxisLabelItalic = 0
slice1Display.PolarAxes.PolarAxisLabelShadow = 0
slice1Display.PolarAxes.PolarAxisLabelFontSize = 12
slice1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
slice1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
slice1Display.PolarAxes.LastRadialAxisTextFontFile = ''
slice1Display.PolarAxes.LastRadialAxisTextBold = 0
slice1Display.PolarAxes.LastRadialAxisTextItalic = 0
slice1Display.PolarAxes.LastRadialAxisTextShadow = 0
slice1Display.PolarAxes.LastRadialAxisTextFontSize = 12
slice1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
slice1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
slice1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
slice1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
slice1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
slice1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
slice1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
slice1Display.PolarAxes.EnableDistanceLOD = 1
slice1Display.PolarAxes.DistanceLODThreshold = 0.7
slice1Display.PolarAxes.EnableViewAngleLOD = 1
slice1Display.PolarAxes.ViewAngleLODThreshold = 0.7
slice1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
slice1Display.PolarAxes.PolarTicksVisibility = 1
slice1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
slice1Display.PolarAxes.TickLocation = 'Both'
slice1Display.PolarAxes.AxisTickVisibility = 1
slice1Display.PolarAxes.AxisMinorTickVisibility = 0
slice1Display.PolarAxes.AxisTickMatchesPolarAxes = 1
slice1Display.PolarAxes.DeltaRangeMajor = 1.0
slice1Display.PolarAxes.DeltaRangeMinor = 0.5
slice1Display.PolarAxes.ArcTickVisibility = 1
slice1Display.PolarAxes.ArcMinorTickVisibility = 0
slice1Display.PolarAxes.ArcTickMatchesRadialAxes = 1
slice1Display.PolarAxes.DeltaAngleMajor = 10.0
slice1Display.PolarAxes.DeltaAngleMinor = 5.0
slice1Display.PolarAxes.TickRatioRadiusSize = 0.02
slice1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
slice1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
slice1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
slice1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
slice1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
slice1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
slice1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
slice1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
slice1Display.PolarAxes.ArcMajorTickSize = 0.0
slice1Display.PolarAxes.ArcTickRatioSize = 0.3
slice1Display.PolarAxes.ArcMajorTickThickness = 1.0
slice1Display.PolarAxes.ArcTickRatioThickness = 0.5
slice1Display.PolarAxes.Use2DMode = 0
slice1Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(streamTracer1, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [54.2993318596307, -20.367308411678255, -2.8891674593951384]
renderView1.CameraFocalPoint = [45.98709869384764, 14.027099609375139, -10.200000002980133]
renderView1.CameraViewUp = [-0.7927602588885768, -0.3038994755036555, -0.5283713473642567]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [54.2993318596307, -20.367308411678255, -2.8891674593951384]
renderView1.CameraFocalPoint = [45.98709869384764, 14.027099609375139, -10.200000002980133]
renderView1.CameraViewUp = [-0.7927602588885768, -0.3038994755036555, -0.5283713473642567]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [16.61454908739075, -5.576064061978774, -2.5523794912312616]
renderView1.CameraFocalPoint = [45.987098693847784, 14.027099609375142, -10.200000002980142]
renderView1.CameraViewUp = [-0.3432520450532227, 0.15277480896532472, -0.9267350707253874]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [16.61454908739075, -5.576064061978774, -2.5523794912312616]
renderView1.CameraFocalPoint = [45.987098693847784, 14.027099609375142, -10.200000002980142]
renderView1.CameraViewUp = [-0.3432520450532227, 0.15277480896532472, -0.9267350707253874]
renderView1.CameraParallelScale = 11.315476125271417

# change representation type
slice1Display.SetRepresentationType('Surface LIC')
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [16.61454908739075, -5.576064061978774, -2.5523794912312616]
renderView1.CameraFocalPoint = [45.987098693847784, 14.027099609375142, -10.200000002980142]
renderView1.CameraViewUp = [-0.3432520450532227, 0.15277480896532472, -0.9267350707253874]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [13.647130492803958, 13.900542230203923, -26.312952426004497]
renderView1.CameraFocalPoint = [45.98709869384786, 14.027099609375107, -10.200000002980216]
renderView1.CameraViewUp = [-0.0392780967828633, -0.9954639562690262, 0.08665300273120569]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [13.647130492803958, 13.900542230203923, -26.312952426004497]
renderView1.CameraFocalPoint = [45.98709869384786, 14.027099609375107, -10.200000002980216]
renderView1.CameraViewUp = [-0.0392780967828633, -0.9954639562690262, 0.08665300273120569]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [56.87327162638512, 13.752439682156384, -44.651888145847686]
renderView1.CameraFocalPoint = [45.98709869384766, 14.027099609375112, -10.200000002980032]
renderView1.CameraViewUp = [-0.07979084976789895, -0.9966620680628617, -0.01726679987653461]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [35.655707248010216, 17.863496850417146, -44.61019039482756]
renderView1.CameraFocalPoint = [45.98709869384778, 14.027099609375078, -10.200000002980053]
renderView1.CameraViewUp = [-0.08085651413082598, -0.9929713399491176, -0.08642998416212774]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [35.655707248010216, 17.863496850417146, -44.61019039482756]
renderView1.CameraFocalPoint = [45.98709869384778, 14.027099609375078, -10.200000002980053]
renderView1.CameraViewUp = [-0.08085651413082598, -0.9929713399491176, -0.08642998416212774]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [35.655707248010216, 17.863496850417146, -44.61019039482756]
renderView1.CameraFocalPoint = [45.98709869384778, 14.027099609375078, -10.200000002980053]
renderView1.CameraViewUp = [-0.08085651413082598, -0.9929713399491176, -0.08642998416212774]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [35.655707248010216, 17.863496850417146, -44.61019039482756]
renderView1.CameraFocalPoint = [45.98709869384778, 14.027099609375078, -10.200000002980053]
renderView1.CameraViewUp = [-0.08085651413082598, -0.9929713399491176, -0.08642998416212774]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [35.655707248010216, 17.863496850417146, -44.61019039482756]
renderView1.CameraFocalPoint = [45.98709869384778, 14.027099609375078, -10.200000002980053]
renderView1.CameraViewUp = [-0.08085651413082598, -0.9929713399491176, -0.08642998416212774]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [35.655707248010216, 17.863496850417146, -44.61019039482756]
renderView1.CameraFocalPoint = [45.98709869384778, 14.027099609375078, -10.200000002980053]
renderView1.CameraViewUp = [-0.08085651413082598, -0.9929713399491176, -0.08642998416212774]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [35.655707248010216, 17.863496850417146, -44.61019039482756]
renderView1.CameraFocalPoint = [45.98709869384778, 14.027099609375078, -10.200000002980053]
renderView1.CameraViewUp = [-0.08085651413082598, -0.9929713399491176, -0.08642998416212774]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [35.655707248010216, 17.863496850417146, -44.61019039482756]
renderView1.CameraFocalPoint = [45.98709869384778, 14.027099609375078, -10.200000002980053]
renderView1.CameraViewUp = [-0.08085651413082598, -0.9929713399491176, -0.08642998416212774]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [43.514093444611404, 14.01739501953125, -10.705812215805054]

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [35.655707248010216, 17.863496850417146, -44.61019039482756]
renderView1.CameraFocalPoint = [45.98709869384778, 14.027099609375078, -10.200000002980053]
renderView1.CameraViewUp = [-0.08085651413082598, -0.9929713399491176, -0.08642998416212774]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [70.58460834759916, 6.126923510591283, -35.45997886764259]
renderView1.CameraFocalPoint = [45.98709869384758, 14.027099609375135, -10.200000002980053]
renderView1.CameraViewUp = [-0.23589241014017676, -0.9690065793061191, 0.0733554367427034]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [70.58460834759916, 6.126923510591283, -35.45997886764259]
renderView1.CameraFocalPoint = [45.98709869384758, 14.027099609375135, -10.200000002980053]
renderView1.CameraViewUp = [-0.23589241014017676, -0.9690065793061191, 0.0733554367427034]
renderView1.CameraParallelScale = 11.315476125271417

# hide data in view
Hide(slice1, renderView1)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [70.58460834759916, 6.126923510591283, -35.45997886764259]
renderView1.CameraFocalPoint = [45.98709869384758, 14.027099609375135, -10.200000002980053]
renderView1.CameraViewUp = [-0.23589241014017676, -0.9690065793061191, 0.0733554367427034]
renderView1.CameraParallelScale = 11.315476125271417

# set active source
SetActiveSource(streamTracer1)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=slice1.SliceType)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=streamTracer1.SeedType)

# destroy slice1
Delete(slice1)
del slice1

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# set active source
SetActiveSource(streamTracer1)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [70.58460834759916, 6.126923510591283, -35.45997886764259]
renderView1.CameraFocalPoint = [45.98709869384758, 14.027099609375135, -10.200000002980053]
renderView1.CameraViewUp = [-0.23589241014017676, -0.9690065793061191, 0.0733554367427034]
renderView1.CameraParallelScale = 11.315476125271417

# set active source
SetActiveSource(calculator1)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=calculator1Display.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=calculator1Display)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=calculator1Display.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=calculator1Display)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=streamTracer1.SeedType)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [70.58460834759916, 6.126923510591283, -35.45997886764259]
renderView1.CameraFocalPoint = [45.98709869384758, 14.027099609375135, -10.200000002980053]
renderView1.CameraViewUp = [-0.23589241014017676, -0.9690065793061191, 0.0733554367427034]
renderView1.CameraParallelScale = 11.315476125271417

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=calculator1)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.UseDual = 0
slice1.Crinkleslice = 0
slice1.Triangulatetheslice = 1
slice1.SliceOffsetValues = [0.0]
slice1.PointMergeMethod = 'Uniform Binning'

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [45.9871, 14.0271, -10.2]
slice1.SliceType.Normal = [1.0, 0.0, 0.0]
slice1.SliceType.Offset = 0.0

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [45.9871, 14.0271, -10.2]
slice1.HyperTreeGridSlicer.Normal = [1.0, 0.0, 0.0]
slice1.HyperTreeGridSlicer.Offset = 0.0

# init the 'Uniform Binning' selected for 'PointMergeMethod'
slice1.PointMergeMethod.Divisions = [50, 50, 50]
slice1.PointMergeMethod.Numberofpointsperbucket = 8
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [70.58460834759916, 6.126923510591283, -35.45997886764259]
renderView1.CameraFocalPoint = [45.98709869384758, 14.027099609375135, -10.200000002980053]
renderView1.CameraViewUp = [-0.23589241014017676, -0.9690065793061191, 0.0733554367427034]
renderView1.CameraParallelScale = 11.315476125271417

# show data in view
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice1Display.Selection = None
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = [None, '']
slice1Display.LookupTable = None
slice1Display.MapScalars = 1
slice1Display.MultiComponentsMapping = 0
slice1Display.InterpolateScalarsBeforeMapping = 1
slice1Display.UseNanColorForMissingArrays = 0
slice1Display.Opacity = 1.0
slice1Display.PointSize = 2.0
slice1Display.LineWidth = 1.0
slice1Display.RenderLinesAsTubes = 0
slice1Display.RenderPointsAsSpheres = 0
slice1Display.DisableLighting = 0
slice1Display.Diffuse = 1.0
slice1Display.Interpolation = 'Gouraud'
slice1Display.Specular = 0.0
slice1Display.SpecularColor = [1.0, 1.0, 1.0]
slice1Display.SpecularPower = 100.0
slice1Display.Luminosity = 0.0
slice1Display.Ambient = 0.0
slice1Display.Roughness = 0.3
slice1Display.Metallic = 0.0
slice1Display.EdgeTint = [1.0, 1.0, 1.0]
slice1Display.Anisotropy = 0.0
slice1Display.AnisotropyRotation = 0.0
slice1Display.BaseIOR = 1.5
slice1Display.CoatStrength = 0.0
slice1Display.CoatIOR = 2.0
slice1Display.CoatRoughness = 0.0
slice1Display.CoatColor = [1.0, 1.0, 1.0]
slice1Display.SelectNormalArray = 'None'
slice1Display.SelectTangentArray = 'None'
slice1Display.ComputePointNormals = 0
slice1Display.Splitting = 1
slice1Display.FeatureAngle = 30.0
slice1Display.SelectTCoordArray = 'None'
slice1Display.Texture = None
slice1Display.RepeatTextures = 1
slice1Display.InterpolateTextures = 0
slice1Display.SeamlessU = 0
slice1Display.SeamlessV = 0
slice1Display.UseMipmapTextures = 0
slice1Display.ShowTexturesOnBackface = 1
slice1Display.BaseColorTexture = None
slice1Display.NormalTexture = None
slice1Display.NormalScale = 1.0
slice1Display.CoatNormalTexture = None
slice1Display.CoatNormalScale = 1.0
slice1Display.MaterialTexture = None
slice1Display.OcclusionStrength = 1.0
slice1Display.AnisotropyTexture = None
slice1Display.EmissiveTexture = None
slice1Display.EmissiveFactor = [1.0, 1.0, 1.0]
slice1Display.TextureTransform = 'Transform2'
slice1Display.EdgeOpacity = 1.0
slice1Display.BackfaceRepresentation = 'Follow Frontface'
slice1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
slice1Display.BackfaceOpacity = 1.0
slice1Display.Translation = [0.0, 0.0, 0.0]
slice1Display.Scale = [1.0, 1.0, 1.0]
slice1Display.Orientation = [0.0, 0.0, 0.0]
slice1Display.Origin = [0.0, 0.0, 0.0]
slice1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
slice1Display.Pickable = 1
slice1Display.Triangulate = 0
slice1Display.UseShaderReplacements = 0
slice1Display.ShaderReplacements = ''
slice1Display.NonlinearSubdivisionLevel = 1
slice1Display.MatchBoundariesIgnoringCellOrder = 0
slice1Display.UseDataPartitions = 0
slice1Display.OSPRayUseScaleArray = 'All Approximate'
slice1Display.OSPRayScaleArray = 'SALT'
slice1Display.OSPRayScaleFunction = 'Piecewise Function'
slice1Display.OSPRayMaterial = 'None'
slice1Display.Assembly = ''
slice1Display.SelectedBlockSelectors = ['']
slice1Display.BlockSelectors = ['/']
slice1Display.BlockColors = []
slice1Display.BlockColorArrayNames = []
slice1Display.BlockLookupTables = []
slice1Display.BlockUseSeparateColorMaps = []
slice1Display.BlockMapScalars = []
slice1Display.BlockInterpolateScalarsBeforeMappings = []
slice1Display.BlockOpacities = []
slice1Display.BlockMapScalarsGUI = 1
slice1Display.BlockInterpolateScalarsBeforeMappingsGUI = 1
slice1Display.BlockOpacitiesGUI = 1.0
slice1Display.Orient = 0
slice1Display.OrientationMode = 'Direction'
slice1Display.SelectOrientationVectors = 'velocity'
slice1Display.Scaling = 0
slice1Display.ScaleMode = 'No Data Scaling Off'
slice1Display.ScaleFactor = 1.9599999994039536
slice1Display.SelectScaleArray = 'None'
slice1Display.GlyphType = 'Arrow'
slice1Display.UseGlyphTable = 0
slice1Display.GlyphTableIndexArray = 'None'
slice1Display.UseCompositeGlyphTable = 0
slice1Display.UseGlyphCullingAndLOD = 0
slice1Display.LODValues = []
slice1Display.ColorByLODIndex = 0
slice1Display.GaussianRadius = 0.09799999997019768
slice1Display.ShaderPreset = 'Sphere'
slice1Display.CustomTriangleScale = 3
slice1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
slice1Display.Emissive = 0
slice1Display.ScaleByArray = 0
slice1Display.SetScaleArray = ['POINTS', 'SALT']
slice1Display.ScaleArrayComponent = ''
slice1Display.UseScaleFunction = 1
slice1Display.ScaleTransferFunction = 'Piecewise Function'
slice1Display.OpacityByArray = 0
slice1Display.OpacityArray = ['POINTS', 'SALT']
slice1Display.OpacityArrayComponent = ''
slice1Display.OpacityTransferFunction = 'Piecewise Function'
slice1Display.DataAxesGrid = 'Grid Axes Representation'
slice1Display.SelectionCellLabelBold = 0
slice1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
slice1Display.SelectionCellLabelFontFamily = 'Arial'
slice1Display.SelectionCellLabelFontFile = ''
slice1Display.SelectionCellLabelFontSize = 18
slice1Display.SelectionCellLabelItalic = 0
slice1Display.SelectionCellLabelJustification = 'Left'
slice1Display.SelectionCellLabelOpacity = 1.0
slice1Display.SelectionCellLabelShadow = 0
slice1Display.SelectionPointLabelBold = 0
slice1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
slice1Display.SelectionPointLabelFontFamily = 'Arial'
slice1Display.SelectionPointLabelFontFile = ''
slice1Display.SelectionPointLabelFontSize = 18
slice1Display.SelectionPointLabelItalic = 0
slice1Display.SelectionPointLabelJustification = 'Left'
slice1Display.SelectionPointLabelOpacity = 1.0
slice1Display.SelectionPointLabelShadow = 0
slice1Display.PolarAxes = 'Polar Axes Representation'
slice1Display.SelectInputVectors = ['POINTS', 'velocity']
slice1Display.NumberOfSteps = 40
slice1Display.StepSize = 0.25
slice1Display.NormalizeVectors = 1
slice1Display.EnhancedLIC = 1
slice1Display.ColorMode = 'Blend'
slice1Display.LICIntensity = 0.8
slice1Display.MapModeBias = 0.0
slice1Display.EnhanceContrast = 'Off'
slice1Display.LowLICContrastEnhancementFactor = 0.0
slice1Display.HighLICContrastEnhancementFactor = 0.0
slice1Display.LowColorContrastEnhancementFactor = 0.0
slice1Display.HighColorContrastEnhancementFactor = 0.0
slice1Display.AntiAlias = 0
slice1Display.MaskOnSurface = 1
slice1Display.MaskThreshold = 0.0
slice1Display.MaskIntensity = 0.0
slice1Display.MaskColor = [0.5, 0.5, 0.5]
slice1Display.GenerateNoiseTexture = 0
slice1Display.NoiseType = 'Gaussian'
slice1Display.NoiseTextureSize = 128
slice1Display.NoiseGrainSize = 2
slice1Display.MinNoiseValue = 0.0
slice1Display.MaxNoiseValue = 0.8
slice1Display.NumberOfNoiseLevels = 1024
slice1Display.ImpulseNoiseProbability = 1.0
slice1Display.ImpulseNoiseBackgroundValue = 0.0
slice1Display.NoiseGeneratorSeed = 1
slice1Display.CompositeStrategy = 'AUTO'
slice1Display.UseLICForLOD = 0
slice1Display.WriteLog = ''

# init the 'Transform2' selected for 'TextureTransform'
slice1Display.TextureTransform.Translate = [0.0, 0.0, 0.0]
slice1Display.TextureTransform.Rotate = [0.0, 0.0, 0.0]
slice1Display.TextureTransform.Scale = [1.0, 1.0, 1.0]

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
slice1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
slice1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
slice1Display.GlyphType.TipResolution = 6
slice1Display.GlyphType.TipRadius = 0.1
slice1Display.GlyphType.TipLength = 0.35
slice1Display.GlyphType.ShaftResolution = 6
slice1Display.GlyphType.ShaftRadius = 0.03
slice1Display.GlyphType.Invert = 0

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 36.341708263, 1.0, 0.5, 0.0]
slice1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 36.341708263, 1.0, 0.5, 0.0]
slice1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'Grid Axes Representation' selected for 'DataAxesGrid'
slice1Display.DataAxesGrid.XTitle = 'X Axis'
slice1Display.DataAxesGrid.YTitle = 'Y Axis'
slice1Display.DataAxesGrid.ZTitle = 'Z Axis'
slice1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
slice1Display.DataAxesGrid.XTitleFontFile = ''
slice1Display.DataAxesGrid.XTitleBold = 0
slice1Display.DataAxesGrid.XTitleItalic = 0
slice1Display.DataAxesGrid.XTitleFontSize = 12
slice1Display.DataAxesGrid.XTitleShadow = 0
slice1Display.DataAxesGrid.XTitleOpacity = 1.0
slice1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
slice1Display.DataAxesGrid.YTitleFontFile = ''
slice1Display.DataAxesGrid.YTitleBold = 0
slice1Display.DataAxesGrid.YTitleItalic = 0
slice1Display.DataAxesGrid.YTitleFontSize = 12
slice1Display.DataAxesGrid.YTitleShadow = 0
slice1Display.DataAxesGrid.YTitleOpacity = 1.0
slice1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
slice1Display.DataAxesGrid.ZTitleFontFile = ''
slice1Display.DataAxesGrid.ZTitleBold = 0
slice1Display.DataAxesGrid.ZTitleItalic = 0
slice1Display.DataAxesGrid.ZTitleFontSize = 12
slice1Display.DataAxesGrid.ZTitleShadow = 0
slice1Display.DataAxesGrid.ZTitleOpacity = 1.0
slice1Display.DataAxesGrid.FacesToRender = 63
slice1Display.DataAxesGrid.CullBackface = 0
slice1Display.DataAxesGrid.CullFrontface = 1
slice1Display.DataAxesGrid.ShowGrid = 0
slice1Display.DataAxesGrid.ShowEdges = 1
slice1Display.DataAxesGrid.ShowTicks = 1
slice1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
slice1Display.DataAxesGrid.AxesToLabel = 63
slice1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
slice1Display.DataAxesGrid.XLabelFontFile = ''
slice1Display.DataAxesGrid.XLabelBold = 0
slice1Display.DataAxesGrid.XLabelItalic = 0
slice1Display.DataAxesGrid.XLabelFontSize = 12
slice1Display.DataAxesGrid.XLabelShadow = 0
slice1Display.DataAxesGrid.XLabelOpacity = 1.0
slice1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
slice1Display.DataAxesGrid.YLabelFontFile = ''
slice1Display.DataAxesGrid.YLabelBold = 0
slice1Display.DataAxesGrid.YLabelItalic = 0
slice1Display.DataAxesGrid.YLabelFontSize = 12
slice1Display.DataAxesGrid.YLabelShadow = 0
slice1Display.DataAxesGrid.YLabelOpacity = 1.0
slice1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
slice1Display.DataAxesGrid.ZLabelFontFile = ''
slice1Display.DataAxesGrid.ZLabelBold = 0
slice1Display.DataAxesGrid.ZLabelItalic = 0
slice1Display.DataAxesGrid.ZLabelFontSize = 12
slice1Display.DataAxesGrid.ZLabelShadow = 0
slice1Display.DataAxesGrid.ZLabelOpacity = 1.0
slice1Display.DataAxesGrid.XAxisNotation = 'Mixed'
slice1Display.DataAxesGrid.XAxisPrecision = 2
slice1Display.DataAxesGrid.XAxisUseCustomLabels = 0
slice1Display.DataAxesGrid.XAxisLabels = []
slice1Display.DataAxesGrid.YAxisNotation = 'Mixed'
slice1Display.DataAxesGrid.YAxisPrecision = 2
slice1Display.DataAxesGrid.YAxisUseCustomLabels = 0
slice1Display.DataAxesGrid.YAxisLabels = []
slice1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
slice1Display.DataAxesGrid.ZAxisPrecision = 2
slice1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
slice1Display.DataAxesGrid.ZAxisLabels = []
slice1Display.DataAxesGrid.UseCustomBounds = 0
slice1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'Polar Axes Representation' selected for 'PolarAxes'
slice1Display.PolarAxes.Visibility = 0
slice1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
slice1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
slice1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
slice1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
slice1Display.PolarAxes.EnableCustomRange = 0
slice1Display.PolarAxes.CustomRange = [0.0, 1.0]
slice1Display.PolarAxes.AutoPole = 1
slice1Display.PolarAxes.PolarAxisVisibility = 1
slice1Display.PolarAxes.RadialAxesVisibility = 1
slice1Display.PolarAxes.DrawRadialGridlines = 1
slice1Display.PolarAxes.PolarArcsVisibility = 1
slice1Display.PolarAxes.DrawPolarArcsGridlines = 1
slice1Display.PolarAxes.NumberOfRadialAxes = 0
slice1Display.PolarAxes.DeltaAngleRadialAxes = 45.0
slice1Display.PolarAxes.NumberOfPolarAxes = 5
slice1Display.PolarAxes.DeltaRangePolarAxes = 0.0
slice1Display.PolarAxes.CustomMinRadius = 1
slice1Display.PolarAxes.MinimumRadius = 0.0
slice1Display.PolarAxes.CustomMaxRadius = 0
slice1Display.PolarAxes.MaximumRadius = 1.0
slice1Display.PolarAxes.CustomAngles = 1
slice1Display.PolarAxes.MinimumAngle = 0.0
slice1Display.PolarAxes.MaximumAngle = 90.0
slice1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
slice1Display.PolarAxes.PolarArcResolutionPerDegree = 0.2
slice1Display.PolarAxes.Ratio = 1.0
slice1Display.PolarAxes.EnableOverallColor = 1
slice1Display.PolarAxes.OverallColor = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.PolarAxisTitleVisibility = 1
slice1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
slice1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
slice1Display.PolarAxes.PolarTitleOffset = [20.0, 20.0]
slice1Display.PolarAxes.PolarLabelVisibility = 1
slice1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
slice1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
slice1Display.PolarAxes.PolarLabelOffset = 10.0
slice1Display.PolarAxes.PolarExponentOffset = 5.0
slice1Display.PolarAxes.RadialTitleVisibility = 1
slice1Display.PolarAxes.RadialTitleFormat = '%-#3.1f'
slice1Display.PolarAxes.RadialTitleLocation = 'Bottom'
slice1Display.PolarAxes.RadialTitleOffset = [20.0, 0.0]
slice1Display.PolarAxes.RadialUnitsVisibility = 1
slice1Display.PolarAxes.ScreenSize = 10.0
slice1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
slice1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
slice1Display.PolarAxes.PolarAxisTitleFontFile = ''
slice1Display.PolarAxes.PolarAxisTitleBold = 0
slice1Display.PolarAxes.PolarAxisTitleItalic = 0
slice1Display.PolarAxes.PolarAxisTitleShadow = 0
slice1Display.PolarAxes.PolarAxisTitleFontSize = 12
slice1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
slice1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
slice1Display.PolarAxes.PolarAxisLabelFontFile = ''
slice1Display.PolarAxes.PolarAxisLabelBold = 0
slice1Display.PolarAxes.PolarAxisLabelItalic = 0
slice1Display.PolarAxes.PolarAxisLabelShadow = 0
slice1Display.PolarAxes.PolarAxisLabelFontSize = 12
slice1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
slice1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
slice1Display.PolarAxes.LastRadialAxisTextFontFile = ''
slice1Display.PolarAxes.LastRadialAxisTextBold = 0
slice1Display.PolarAxes.LastRadialAxisTextItalic = 0
slice1Display.PolarAxes.LastRadialAxisTextShadow = 0
slice1Display.PolarAxes.LastRadialAxisTextFontSize = 12
slice1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
slice1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
slice1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
slice1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
slice1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
slice1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
slice1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
slice1Display.PolarAxes.EnableDistanceLOD = 1
slice1Display.PolarAxes.DistanceLODThreshold = 0.7
slice1Display.PolarAxes.EnableViewAngleLOD = 1
slice1Display.PolarAxes.ViewAngleLODThreshold = 0.7
slice1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
slice1Display.PolarAxes.PolarTicksVisibility = 1
slice1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
slice1Display.PolarAxes.TickLocation = 'Both'
slice1Display.PolarAxes.AxisTickVisibility = 1
slice1Display.PolarAxes.AxisMinorTickVisibility = 0
slice1Display.PolarAxes.AxisTickMatchesPolarAxes = 1
slice1Display.PolarAxes.DeltaRangeMajor = 1.0
slice1Display.PolarAxes.DeltaRangeMinor = 0.5
slice1Display.PolarAxes.ArcTickVisibility = 1
slice1Display.PolarAxes.ArcMinorTickVisibility = 0
slice1Display.PolarAxes.ArcTickMatchesRadialAxes = 1
slice1Display.PolarAxes.DeltaAngleMajor = 10.0
slice1Display.PolarAxes.DeltaAngleMinor = 5.0
slice1Display.PolarAxes.TickRatioRadiusSize = 0.02
slice1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
slice1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
slice1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
slice1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
slice1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
slice1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
slice1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
slice1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
slice1Display.PolarAxes.ArcMajorTickSize = 0.0
slice1Display.PolarAxes.ArcTickRatioSize = 0.3
slice1Display.PolarAxes.ArcMajorTickThickness = 1.0
slice1Display.PolarAxes.ArcTickRatioThickness = 0.5
slice1Display.PolarAxes.Use2DMode = 0
slice1Display.PolarAxes.UseLogAxis = 0

# update the view to ensure updated data information
renderView1.Update()
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [70.58460834759916, 6.126923510591283, -35.45997886764259]
renderView1.CameraFocalPoint = [45.98709869384758, 14.027099609375135, -10.200000002980053]
renderView1.CameraViewUp = [-0.23589241014017676, -0.9690065793061191, 0.0733554367427034]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [70.58460834759916, 6.126923510591283, -35.45997886764259]
renderView1.CameraFocalPoint = [45.98709869384758, 14.027099609375135, -10.200000002980053]
renderView1.CameraViewUp = [-0.23589241014017676, -0.9690065793061191, 0.0733554367427034]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [32.7046690873484, 35.39464264289878, 15.733028440691296]
renderView1.CameraFocalPoint = [45.987098693847756, 14.027099609374972, -10.200000002980444]
renderView1.CameraViewUp = [-0.7889779777572006, -0.6068844576135123, 0.09594272104392032]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [23.653734067126486, 22.42400127289539, 16.933552339174774]
renderView1.CameraFocalPoint = [45.98709869384773, 14.027099609375059, -10.200000002980408]
renderView1.CameraViewUp = [-0.5113278640940395, -0.8444467005549393, -0.15954179804334753]
renderView1.CameraParallelScale = 11.315476125271417

# change representation type
slice1Display.SetRepresentationType('Surface LIC')
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [23.653734067126486, 22.42400127289539, 16.933552339174774]
renderView1.CameraFocalPoint = [45.98709869384773, 14.027099609375059, -10.200000002980408]
renderView1.CameraViewUp = [-0.5113278640940395, -0.8444467005549393, -0.15954179804334753]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [24.24885142889873, 7.3292994869217125, 17.873205641708466]
renderView1.CameraFocalPoint = [45.9870986938477, 14.027099609375119, -10.200000002980392]
renderView1.CameraViewUp = [-0.12313393882374958, -0.939549018439269, -0.31950848980826085]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [28.02160508645186, 8.491727607347512, 13.00099639758891]
renderView1.CameraFocalPoint = [45.9870986938477, 14.027099609375119, -10.200000002980392]
renderView1.CameraViewUp = [-0.12313393882374958, -0.939549018439269, -0.31950848980826085]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [24.24885142889873, 7.3292994869217125, 17.873205641708466]
renderView1.CameraFocalPoint = [45.9870986938477, 14.027099609375119, -10.200000002980392]
renderView1.CameraViewUp = [-0.12313393882374958, -0.939549018439269, -0.31950848980826085]
renderView1.CameraParallelScale = 11.315476125271417

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'velocity', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [24.24885142889873, 7.3292994869217125, 17.873205641708466]
renderView1.CameraFocalPoint = [45.9870986938477, 14.027099609375119, -10.200000002980392]
renderView1.CameraViewUp = [-0.12313393882374958, -0.939549018439269, -0.31950848980826085]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [24.24885142889873, 7.3292994869217125, 17.873205641708466]
renderView1.CameraFocalPoint = [45.9870986938477, 14.027099609375119, -10.200000002980392]
renderView1.CameraViewUp = [-0.12313393882374958, -0.939549018439269, -0.31950848980826085]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [24.24885142889873, 7.3292994869217125, 17.873205641708466]
renderView1.CameraFocalPoint = [45.9870986938477, 14.027099609375119, -10.200000002980392]
renderView1.CameraViewUp = [-0.12313393882374958, -0.939549018439269, -0.31950848980826085]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [24.24885142889873, 7.3292994869217125, 17.873205641708466]
renderView1.CameraFocalPoint = [45.9870986938477, 14.027099609375119, -10.200000002980392]
renderView1.CameraViewUp = [-0.12313393882374958, -0.939549018439269, -0.31950848980826085]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [72.1928341652794, 16.30733922329583, 14.570481048178744]
renderView1.CameraFocalPoint = [45.98709869384751, 14.02709960937509, -10.20000000298031]
renderView1.CameraViewUp = [-0.24428750138223004, -0.9074019561794578, 0.3419726693613396]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [72.1928341652794, 16.30733922329583, 14.570481048178744]
renderView1.CameraFocalPoint = [45.98709869384751, 14.02709960937509, -10.20000000298031]
renderView1.CameraViewUp = [-0.24428750138223007, -0.907401956179458, 0.34197266936133963]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [72.1928341652794, 16.30733922329583, 14.570481048178744]
renderView1.CameraFocalPoint = [45.98709869384751, 14.02709960937509, -10.20000000298031]
renderView1.CameraViewUp = [-0.24428750138223007, -0.907401956179458, 0.34197266936133963]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [72.1928341652794, 16.30733922329583, 14.570481048178744]
renderView1.CameraFocalPoint = [45.98709869384751, 14.02709960937509, -10.20000000298031]
renderView1.CameraViewUp = [-0.24428750138223007, -0.907401956179458, 0.34197266936133963]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [72.1928341652794, 16.30733922329583, 14.570481048178744]
renderView1.CameraFocalPoint = [45.98709869384751, 14.02709960937509, -10.20000000298031]
renderView1.CameraViewUp = [-0.24428750138223007, -0.907401956179458, 0.34197266936133963]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [72.1928341652794, 16.30733922329583, 14.570481048178744]
renderView1.CameraFocalPoint = [45.98709869384751, 14.02709960937509, -10.20000000298031]
renderView1.CameraViewUp = [-0.24428750138223007, -0.907401956179458, 0.34197266936133963]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on renderView1
renderView1.UseColorPaletteForBackground = 0
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [72.1928341652794, 16.30733922329583, 14.570481048178744]
renderView1.CameraFocalPoint = [45.98709869384751, 14.02709960937509, -10.20000000298031]
renderView1.CameraViewUp = [-0.24428750138223007, -0.907401956179458, 0.34197266936133963]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on renderView1
renderView1.UseColorPaletteForBackground = 1
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [72.1928341652794, 16.30733922329583, 14.570481048178744]
renderView1.CameraFocalPoint = [45.98709869384751, 14.02709960937509, -10.20000000298031]
renderView1.CameraViewUp = [-0.24428750138223007, -0.907401956179458, 0.34197266936133963]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [72.1928341652794, 16.30733922329583, 14.570481048178744]
renderView1.CameraFocalPoint = [45.98709869384751, 14.02709960937509, -10.20000000298031]
renderView1.CameraViewUp = [-0.24428750138223007, -0.907401956179458, 0.34197266936133963]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [72.1928341652794, 16.30733922329583, 14.570481048178744]
renderView1.CameraFocalPoint = [45.98709869384751, 14.02709960937509, -10.20000000298031]
renderView1.CameraViewUp = [-0.24428750138223007, -0.907401956179458, 0.34197266936133963]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [72.1928341652794, 16.30733922329583, 14.570481048178744]
renderView1.CameraFocalPoint = [45.98709869384751, 14.02709960937509, -10.20000000298031]
renderView1.CameraViewUp = [-0.24428750138223007, -0.907401956179458, 0.34197266936133963]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [67.09952684803449, 17.100349365392457, 18.960543702047165]
renderView1.CameraFocalPoint = [45.987098693847514, 14.027099609375085, -10.200000002980335]
renderView1.CameraViewUp = [-0.2774868366720108, -0.9136083774480355, 0.2971881359181905]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [36.28784539923873, 9.923624332830624, 24.363026079571956]
renderView1.CameraFocalPoint = [45.98709869384762, 14.027099609375103, -10.200000002980389]
renderView1.CameraViewUp = [-0.17588749585077756, -0.9705538335662949, -0.1645868918022075]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.0452120792725, 29.051889656861, 22.527935816092207]
renderView1.CameraFocalPoint = [45.9870986938476, 14.027099609375018, -10.200000002980417]
renderView1.CameraViewUp = [-0.2827625394848688, -0.8811032809888683, 0.37908093396360576]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.0452120792725, 29.051889656861, 22.527935816092207]
renderView1.CameraFocalPoint = [45.9870986938476, 14.027099609375018, -10.200000002980417]
renderView1.CameraViewUp = [-0.2827625394848688, -0.8811032809888683, 0.37908093396360576]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.0452120792725, 29.051889656861, 22.527935816092207]
renderView1.CameraFocalPoint = [45.9870986938476, 14.027099609375018, -10.200000002980417]
renderView1.CameraViewUp = [-0.2827625394848688, -0.8811032809888683, 0.37908093396360576]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.0452120792725, 29.051889656861, 22.527935816092207]
renderView1.CameraFocalPoint = [45.9870986938476, 14.027099609375018, -10.200000002980417]
renderView1.CameraViewUp = [-0.2827625394848688, -0.8811032809888683, 0.37908093396360576]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.0452120792725, 29.051889656861, 22.527935816092207]
renderView1.CameraFocalPoint = [45.9870986938476, 14.027099609375018, -10.200000002980417]
renderView1.CameraViewUp = [-0.2827625394848688, -0.8811032809888683, 0.37908093396360576]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on renderView1
renderView1.OrientationAxesVisibility = 0
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [43.0452120792725, 29.051889656861, 22.527935816092207]
renderView1.CameraFocalPoint = [45.9870986938476, 14.027099609375018, -10.200000002980417]
renderView1.CameraViewUp = [-0.2827625394848688, -0.8811032809888683, 0.37908093396360576]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [12.482233268438804, 8.405838399191504, 2.102122213674411]
renderView1.CameraFocalPoint = [45.98709869384772, 14.027099609375066, -10.200000002980381]
renderView1.CameraViewUp = [0.2147140026970595, -0.9661028841863084, 0.14332869291493447]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [12.482233268438804, 8.405838399191504, 2.102122213674411]
renderView1.CameraFocalPoint = [45.98709869384772, 14.027099609375066, -10.200000002980381]
renderView1.CameraViewUp = [0.2147140026970595, -0.9661028841863084, 0.14332869291493447]
renderView1.CameraParallelScale = 11.315476125271417

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=slice1.SliceType)
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [12.482233268438804, 8.405838399191504, 2.102122213674411]
renderView1.CameraFocalPoint = [45.98709869384772, 14.027099609375066, -10.200000002980381]
renderView1.CameraViewUp = [0.2147140026970595, -0.9661028841863084, 0.14332869291493447]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [16.528063259784776, 9.360482993177305, 10.193742087510033]
renderView1.CameraFocalPoint = [45.9870986938477, 14.027099609375062, -10.200000002980394]
renderView1.CameraViewUp = [0.2237725721777043, -0.9693491270271912, 0.10143030056445947]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [18.90162925319072, 9.637233209383336, 13.307939378659396]
renderView1.CameraFocalPoint = [45.98709869384767, 14.027099609375059, -10.200000002980397]
renderView1.CameraViewUp = [0.23616515135235047, -0.9673997307635732, 0.09145371619178466]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [23.7987416664796, 11.389803424224798, 9.639257235932527]
renderView1.CameraFocalPoint = [50.88421110713655, 15.779669824216523, -13.868682145707266]
renderView1.CameraViewUp = [0.23616515135235047, -0.9673997307635732, 0.09145371619178466]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [29.795678305209904, 4.155066931525007, 12.8923260630483]
renderView1.CameraFocalPoint = [49.49802844928488, 17.252802748350472, -14.416711105521093]
renderView1.CameraViewUp = [0.43102578397180136, -0.8945798117184804, -0.11808358911052022]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [28.188397676087263, 8.905581680651594, 13.24890066890742]
renderView1.CameraFocalPoint = [49.93422576343099, 16.311936740448015, -14.639836508048276]
renderView1.CameraViewUp = [0.34038013532437883, -0.9401563171076899, 0.015730952897470618]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [28.188397676087263, 8.905581680651594, 13.24890066890742]
renderView1.CameraFocalPoint = [49.93422576343099, 16.311936740448015, -14.639836508048276]
renderView1.CameraViewUp = [0.34038013532437883, -0.9401563171076899, 0.015730952897470618]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [28.188397676087263, 8.905581680651594, 13.24890066890742]
renderView1.CameraFocalPoint = [49.93422576343099, 16.311936740448015, -14.639836508048276]
renderView1.CameraViewUp = [0.34038013532437883, -0.9401563171076899, 0.015730952897470618]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [28.188397676087263, 8.905581680651594, 13.24890066890742]
renderView1.CameraFocalPoint = [49.93422576343099, 16.311936740448015, -14.639836508048276]
renderView1.CameraViewUp = [0.34038013532437883, -0.9401563171076899, 0.015730952897470618]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on slice1Display
slice1Display.NumberOfSteps = 4
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [28.188397676087263, 8.905581680651594, 13.24890066890742]
renderView1.CameraFocalPoint = [49.93422576343099, 16.311936740448015, -14.639836508048276]
renderView1.CameraViewUp = [0.34038013532437883, -0.9401563171076899, 0.015730952897470618]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.20684180731828, 7.539052358776718, 12.117747210479386]
renderView1.CameraFocalPoint = [50.08647342056422, 16.58244195305845, -14.344610161636702]
renderView1.CameraViewUp = [0.36252212119036736, -0.9319614677663993, -0.005053142223941876]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.20684180731828, 7.539052358776718, 12.117747210479386]
renderView1.CameraFocalPoint = [50.08647342056422, 16.58244195305845, -14.344610161636702]
renderView1.CameraViewUp = [0.36252212119036736, -0.9319614677663993, -0.005053142223941876]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.20684180731828, 7.539052358776718, 12.117747210479386]
renderView1.CameraFocalPoint = [50.08647342056422, 16.58244195305845, -14.344610161636702]
renderView1.CameraViewUp = [0.36252212119036736, -0.9319614677663993, -0.005053142223941876]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.20684180731828, 7.539052358776718, 12.117747210479386]
renderView1.CameraFocalPoint = [50.08647342056422, 16.58244195305845, -14.344610161636702]
renderView1.CameraViewUp = [0.36252212119036736, -0.9319614677663993, -0.005053142223941876]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.20684180731828, 7.539052358776718, 12.117747210479386]
renderView1.CameraFocalPoint = [50.08647342056422, 16.58244195305845, -14.344610161636702]
renderView1.CameraViewUp = [0.36252212119036736, -0.9319614677663993, -0.005053142223941876]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.20684180731828, 7.539052358776718, 12.117747210479386]
renderView1.CameraFocalPoint = [50.08647342056422, 16.58244195305845, -14.344610161636702]
renderView1.CameraViewUp = [0.36252212119036736, -0.9319614677663993, -0.005053142223941876]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.20684180731828, 7.539052358776718, 12.117747210479386]
renderView1.CameraFocalPoint = [50.08647342056422, 16.58244195305845, -14.344610161636702]
renderView1.CameraViewUp = [0.36252212119036736, -0.9319614677663993, -0.005053142223941876]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on slice1Display
slice1Display.NumberOfSteps = 100
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.20684180731828, 7.539052358776718, 12.117747210479386]
renderView1.CameraFocalPoint = [50.08647342056422, 16.58244195305845, -14.344610161636702]
renderView1.CameraViewUp = [0.36252212119036736, -0.9319614677663993, -0.005053142223941876]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.20684180731828, 7.539052358776718, 12.117747210479386]
renderView1.CameraFocalPoint = [50.08647342056422, 16.58244195305845, -14.344610161636702]
renderView1.CameraViewUp = [0.36252212119036736, -0.9319614677663993, -0.005053142223941876]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.20684180731828, 7.539052358776718, 12.117747210479386]
renderView1.CameraFocalPoint = [50.08647342056422, 16.58244195305845, -14.344610161636702]
renderView1.CameraViewUp = [0.36252212119036736, -0.9319614677663993, -0.005053142223941876]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.20684180731828, 7.539052358776718, 12.117747210479386]
renderView1.CameraFocalPoint = [50.08647342056422, 16.58244195305845, -14.344610161636702]
renderView1.CameraViewUp = [0.36252212119036736, -0.9319614677663993, -0.005053142223941876]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on slice1Display
slice1Display.NumberOfSteps = 40
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.20684180731828, 7.539052358776718, 12.117747210479386]
renderView1.CameraFocalPoint = [50.08647342056422, 16.58244195305845, -14.344610161636702]
renderView1.CameraViewUp = [0.36252212119036736, -0.9319614677663993, -0.005053142223941876]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.20684180731828, 7.539052358776718, 12.117747210479386]
renderView1.CameraFocalPoint = [50.08647342056422, 16.58244195305845, -14.344610161636702]
renderView1.CameraViewUp = [0.36252212119036736, -0.9319614677663993, -0.005053142223941876]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on slice1Display
slice1Display.StepSize = 0.0
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.20684180731828, 7.539052358776718, 12.117747210479386]
renderView1.CameraFocalPoint = [50.08647342056422, 16.58244195305845, -14.344610161636702]
renderView1.CameraViewUp = [0.36252212119036736, -0.9319614677663993, -0.005053142223941876]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.20684180731828, 7.539052358776718, 12.117747210479386]
renderView1.CameraFocalPoint = [50.08647342056422, 16.58244195305845, -14.344610161636702]
renderView1.CameraViewUp = [0.36252212119036736, -0.9319614677663993, -0.005053142223941876]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.20684180731828, 7.539052358776718, 12.117747210479386]
renderView1.CameraFocalPoint = [50.08647342056422, 16.58244195305845, -14.344610161636702]
renderView1.CameraViewUp = [0.36252212119036736, -0.9319614677663993, -0.005053142223941876]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.20684180731828, 7.539052358776718, 12.117747210479386]
renderView1.CameraFocalPoint = [50.08647342056422, 16.58244195305845, -14.344610161636702]
renderView1.CameraViewUp = [0.36252212119036736, -0.9319614677663993, -0.005053142223941876]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on slice1Display
slice1Display.StepSize = 0.5
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.20684180731828, 7.539052358776718, 12.117747210479386]
renderView1.CameraFocalPoint = [50.08647342056422, 16.58244195305845, -14.344610161636702]
renderView1.CameraViewUp = [0.36252212119036736, -0.9319614677663993, -0.005053142223941876]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.331592172311225, 7.586937989601789, 12.235931920388289]
renderView1.CameraFocalPoint = [50.06324776327312, 16.573560761871533, -14.372886938106852]
renderView1.CameraViewUp = [0.3625221211903674, -0.9319614677663993, -0.005053142223941792]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.331592172311225, 7.586937989601789, 12.235931920388289]
renderView1.CameraFocalPoint = [50.06324776327312, 16.573560761871533, -14.372886938106852]
renderView1.CameraViewUp = [0.3625221211903674, -0.9319614677663993, -0.005053142223941792]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.331592172311225, 7.586937989601789, 12.235931920388289]
renderView1.CameraFocalPoint = [50.06324776327312, 16.573560761871533, -14.372886938106852]
renderView1.CameraViewUp = [0.3625221211903674, -0.9319614677663993, -0.005053142223941792]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.331592172311225, 7.586937989601789, 12.235931920388289]
renderView1.CameraFocalPoint = [50.06324776327312, 16.573560761871533, -14.372886938106852]
renderView1.CameraViewUp = [0.3625221211903674, -0.9319614677663993, -0.005053142223941792]
renderView1.CameraParallelScale = 11.315476125271417

# Properties modified on slice1Display
slice1Display.StepSize = 1.0
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.331592172311225, 7.586937989601789, 12.235931920388289]
renderView1.CameraFocalPoint = [50.06324776327312, 16.573560761871533, -14.372886938106852]
renderView1.CameraViewUp = [0.3625221211903674, -0.9319614677663993, -0.005053142223941792]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.331592172311225, 7.586937989601789, 12.235931920388289]
renderView1.CameraFocalPoint = [50.06324776327312, 16.573560761871533, -14.372886938106852]
renderView1.CameraViewUp = [0.3625221211903674, -0.9319614677663993, -0.005053142223941792]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.331592172311225, 7.586937989601789, 12.235931920388289]
renderView1.CameraFocalPoint = [50.06324776327312, 16.573560761871533, -14.372886938106852]
renderView1.CameraViewUp = [0.3625221211903674, -0.9319614677663993, -0.005053142223941792]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.331592172311225, 7.586937989601789, 12.235931920388289]
renderView1.CameraFocalPoint = [50.06324776327312, 16.573560761871533, -14.372886938106852]
renderView1.CameraViewUp = [0.3625221211903674, -0.9319614677663993, -0.005053142223941792]
renderView1.CameraParallelScale = 11.315476125271417
# Adjust camera

# current camera placement for renderView1
renderView1.CameraPosition = [27.331592172311225, 7.586937989601789, 12.235931920388289]
renderView1.CameraFocalPoint = [50.06324776327312, 16.573560761871533, -14.372886938106852]
renderView1.CameraViewUp = [0.3625221211903674, -0.9319614677663993, -0.005053142223941792]
renderView1.CameraParallelScale = 11.315476125271417

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1052, 784)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [27.331592172311225, 7.586937989601789, 12.235931920388289]
renderView1.CameraFocalPoint = [50.06324776327312, 16.573560761871533, -14.372886938106852]
renderView1.CameraViewUp = [0.3625221211903674, -0.9319614677663993, -0.005053142223941792]
renderView1.CameraParallelScale = 11.315476125271417


##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://www.paraview.org/paraview-docs/latest/python/paraview.simple.html
##--------------------------------------------