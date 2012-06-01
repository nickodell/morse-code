from distutils.core import setup, Extension
 
module1 = Extension('gz_dsp', sources = ['gz_dsp.c'])
 
setup (name = 'gz_dsp',
        version = '1.0',
        description = 'This is a demo package',
        ext_modules = [module1])