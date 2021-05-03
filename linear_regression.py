import os, sys
import otbApplication as otb



def temp(x, y):
    """


    """
    
    # Computing the statistics of X and Y
    for image in [x, y]:
        output_stats = os.path.join(os.path.dirname(image), 'ndvi_stats.xml')
        app = otb.Registry.CreateApplication('ComputeImagesStatistics')
        app.SetParameterStringList('il', [image])
        app.SetParameterString('out', output_stats)
        app.ExecuteAndWriteOutput()

    # Computing the statistics of X*Y
    output_xy_stats = 'xy_stats.xml'
    app1 = otb.Registry.CreateApplication('BandMath')
    app2 = otb.Registry.CreateApplication('ComputeImagesStatistics')

    app1.SetParameterStringList('il', [x, y])
    app1.SetParameterString('exp', 'im1b1 * im1b1')
    app1.Execute()

    # Connection between app1.out and app2.in
    app2.AddImageToParameterInputImageList("il", app1.GetParameterOutputImage("out"))
    app2.SetParameterString('out', output_xy_stats)

    app2.ExecuteAndWriteOutput()




if __name__ == '__main__':
    temp('/home/nicolas/Downloads/S2B_MSIL1C_20210328T103629_N0209_R008_T31TEJ_20210328T124650.SAFE/ndvi.tif', '/home/nicolas/Downloads/S2A_MSIL1C_20200318T104021_N0209_R008_T31TEJ_20200318T110354.SAFE/ndvi.tif')

