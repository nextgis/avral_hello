import os

from setuptools import setup

# here = os.path.abspath(os.path.dirname(__file__))
# with open(os.path.join(here, 'README.txt')) as f:
#     README = f.read()
# with open(os.path.join(here, 'CHANGES.txt')) as f:
#     CHANGES = f.read()

requires = [
    'avral',
]

setup(
    name='avral_helloworld',
    version='0.0.1',
    description='Extension for NextGIS Distributed Geo Task',
    # long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
    ],
    author='nextgis',
    author_email='info@nextgis.com',
    url='http://nextgis.com',
    keywords='geo processing server',
    packages=['avral_helloworld'],
    include_package_data=True,
    zip_safe=False,
    # test_suite='avral_web',
    install_requires=requires,
    entry_points={
        'avral_operations': [
            'hello = avral_helloworld.operations:HelloWorld',
        ],
    }
)
