from setuptools import setup

setup(
    name='Ham',
    version='1.0.0.13',
    packages=['Ham', 'Ham.rbn', 'Ham.adif', 'Ham.calc', 'Ham.dxcc', 'Ham.mode', 'Ham.mode.morse',
              'Ham.radio', 'Ham.beacon', 'Ham.qsosvr', 'Ham.telnet', 'Ham.antenna', 'Ham.antenna.quad',
              'Ham.antenna.wind_force', 'Ham.HamTest', 'Ham.rotator', 'Ham.rbn'],
    url='',
    license='',
    author='tim seed',
    author_email='tim@sy-edm.com',
    description='My Ham Radio Library. import Ham .... and you are ready to go'
)
