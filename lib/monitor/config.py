#  Some constant values for use by the monitor
space    = ' '
gresLine = 'GLOBAL UPDATETIME=%s  STATE=idle ARES=%s:%d CRES=%s:%s\n'
gresDir  = '/opt/moab/licenses'
gresFile = gresDir + '/license.txt'
lmstat   = '/usr/local/bin/lmstat'
toAddr   = 'Flux License Monitors <cac-systems@umich.edu>'
fromAddr = 'HPC Systems <hpc-systems@umich.edu>'
subjText = '%s license server did not respond'
errMsgText  = '''\
The license server daemon for %s did not respond within
five tries.  The ADEF has been set to 0.  Please investigate
this problem.

%s

Generated this output:

%s'''

#  Format for daemons[]
#  [ 'feature monitored', 'port@license-server', 'gres_name' ]

daemons = [
     ['abaqus', '27000@flux-license-abaqus.arc-ts.umich.edu', 'abaqus', '0'],
     ['aa_r_hpc', '1055@flux-license-ansys.arc-ts.umich.edu', 'aa_r_hpc', '0'],
     ['aa_r', '1055@flux-license-ansys.arc-ts.umich.edu', 'aa_r', '0'],
     ['aa_r', '1055@flux-license-ansys.arc-ts.umich.edu', 'ansys', '0'],
     ['anshpc', '1055@flux-license-ansys.arc-ts.umich.edu', 'anshpc', '0'],
     ['anshpc', '1055@flux-license-ansys.arc-ts.umich.edu', 'ansys_hpc', '0'],
     ['CFD++_SOLV_Ser', '29029@license18.engin.umich.edu', 'cfd_solv_ser', '0'],
     ['CHEMKIN_PRO', '1723@license-chemkin.engin.umich.edu', 'CHEMKIN_PRO', '2'],
     ['CHEMKIN', '1723@license-chemkin.engin.umich.edu', 'CHEMKIN', '20'],
#     ['DYTRAN', '27500@flux-license-msc.arc-ts.umich.edu', 'DYTRAN', '0'],
     ['helios', '27001@caen-license21.engin.umich.edu', 'helios', '0'],
#     ['MARC', '27500@flux-license-msc.arc-ts.umich.edu', 'MARC', '0'],
     ['MS_castep_MP', '1715@flux-license-msi.arc-ts.umich.edu', 'MS_castep_MP', '0'],
     ['MS_compass_MP', '1715@flux-license-msi.arc-ts.umich.edu', 'MS_compass_MP', '0'],
     ['MS_dmol_MP', '1715@flux-license-msi.arc-ts.umich.edu', 'MS_dmol_MP', '0'],
     ['MS_dsolid_MP', '1715@flux-license-msi.arc-ts.umich.edu', 'MS_dsolid_MP', '0'],
     ['MS_forciteplus_MP', '1715@flux-license-msi.arc-ts.umich.edu', 'MS_forciteplus_MP', '0'],
     ['MS_sorption', '1715@flux-license-msi.arc-ts.umich.edu', 'MS_sorption', '0'],
     ['MATLAB', '1709@flux-license-matlab.arc-ts.umich.edu', 'MATLAB', '0'],
     ['Communication_Toolbox', '1709@flux-license-matlab.arc-ts.umich.edu', 'Communication_Toolbox', '0'],
     ['Distrib_Computing_Toolbox', '1709@flux-license-matlab.arc-ts.umich.edu', 'Distrib_Computing_Toolbox', '0'],
     ['GADS_Toolbox', '1709@flux-license-matlab.arc-ts.umich.edu', 'GADS_Toolbox', '0'],
     ['Image_Toolbox', '1709@flux-license-matlab.arc-ts.umich.edu', 'Image_Toolbox', '0'],
     ['MAP_Toolbox', '1709@flux-license-matlab.arc-ts.umich.edu', 'MAP_Toolbox', '0'],
     ['MATLAB_Distrib_Comp_Engine', '1709@flux-license-matlab.arc-ts.umich.edu', 'MATLAB_Distrib_Comp_Engine', '0'],
     ['Neural_Network_Toolbox', '1709@flux-license-matlab.arc-ts.umich.edu', 'Neural_Network_Toolbox', '0'],
     ['Optimization_Toolbox', '1709@flux-license-matlab.arc-ts.umich.edu', 'Optimization_Toolbox', '0'],
     ['PDE_Toolbox', '1709@flux-license-matlab.arc-ts.umich.edu', 'PDE_Toolbox', '0'],
     ['SIMULINK', '1709@flux-license-matlab.arc-ts.umich.edu', 'SIMULINK', '0'],
     ['Statistics_Toolbox', '1709@flux-license-matlab.arc-ts.umich.edu','Statistics_Toolbox', '0'],
     ['Symbolic_Toolbox', '1709@flux-license-matlab.arc-ts.umich.edu','Symbolic_Toolbox', '0']
]

