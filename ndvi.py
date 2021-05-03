import os, sys
import otbApplication as otb


def ndvi(s2_folder, ndvi_outpath=None):
    """
    Computes the NDVI from a S2 L1C image folder.

    Parameters
    ----------
    s2_folder : path of the Sentinel-2 image folder, 
                e.g. 'S2B_MSIL1C_20210424T102549_N0300_R108_T31TGL_20210424T113038.SAFE'
    ndvi_outpath : optional,
                   path of the NDVI to compute. If not specified,
                   the results is written as ndvi.tif inside s2_folder

    """
    # deduce output path if not specified
    if ndvi_outpath is None:
        ndvi_outpath = os.path.join(s2_folder, 'ndvi.tif')

    # Search for the red & NIR bands inside the folder
    for root, subdirs, files in os.walk(s2_folder):
        for file in files:
            if file.lower().endswith('b08.jp2'):
                nir = os.path.join(root, file)
            elif file.lower().endswith('b04.jp2'):
                red = os.path.join(root, file)

    # Compute the NDVI
    app = otb.Registry.CreateApplication("BandMath")

    app.SetParameterStringList("il", [nir, red]) 
    app.SetParameterString("out", ndvi_outpath)
    app.SetParameterString("exp", '(im1b1 - im2b1) / (im1b1 + im2b1)')

    app.ExecuteAndWriteOutput()



if __name__ == '__main__':
    # command line interface
    if len(sys.argv) == 2:
        s2_folder = sys.argv[1]
        ndvi(s2_folder)
    elif len(sys.argv) == 3:
        s2_folder = sys.argv[1]
        ndvi_outpath = sys.argv[2]
        ndvi(s2_folder, ndvi_outpath)

    else:
        print('Usage : python script.py [s2_folder] (ndvi_outpath)')
        print('Ex    : python script.py /home/images/S2B_MSIL1C_20210424T102549_N0300_R108_T31TGL_20210424T113038.SAFE /home/images/ndvi_test.tif')
        
