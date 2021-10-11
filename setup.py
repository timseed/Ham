from setuptools import setup, find_packages

requirements = 'wheel', 'ephem', 'pyserial', 'pyyaml', 'geojson','PyQt5'
for p in find_packages():
    print("Installing package "+str(p))
setup(
    name='ham',
    version='1.13.0',
    packages=find_packages(),
    include_package_data=True, #Uses Manifest.IN
    url='',
    license='Public',
    author='tim',
    author_email='tim@sy-edm.com',
    description='Some Ham radio utils, which I use.',
    install_requires=requirements,
    extras_require={
        'dev': [
            'bumpversion',
            'pytest',
            'pytest-pep8',
            'pytest-cov',
            'sphinx',
            'recommonmark',
            'black',
            'pylint',
            'mock_pyserial',
            'mock'
        ]},
    #Dev can be triggered by
    #python setup.py sdist
    #pip install dist/ham-1.13.0.tar.gz[dev]
    #
)

