
"""
MAP Client Plugin - Generated from MAP Client v0.20.0
"""

__version__ = '0.1.0'
__author__ = 'Mabelle Lin'
__stepname__ = 'Data Downsampler'
__location__ = 'https://github.com/mapclient-plugins/mapclientplugins.datadownsamplerstep'

# import class that derives itself from the step mountpoint.
from mapclientplugins.datadownsamplerstep import step

# Import the resource file when the module is loaded,
# this enables the framework to use the step icon.
from . import resources_rc
