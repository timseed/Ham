from setuptools import setup

setup(
    name='ham',
    version='1.0.0.14',
    packages=['ham', 'ham.rbn', 'ham.adif', 'ham.calc', 'ham.dxcc', 'ham.mode', 'ham.mode.morse', 'ham.radio',
              'ham.beacon', 'ham.qsosvr', 'ham.telnet', 'ham.antenna', 'ham.antenna.quad', 'ham.antenna.wind_force',
              'ham.HamTest', 'ham.rotator',],
    url='https://github.com/timseed/ham.git',
    license='GNU',
    author='tim seed',
    author_email='tim@sy-edm.com',
    description='My ham Radio Library. import ham .... and you are ready to go'
)
