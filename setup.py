from setuptools import setup

requires = [
    "avral",
]

setup(
    name="avral_hello",
    version="0.0.1",
    description="Extension for NextGIS Distributed Geo Task",
    classifiers=[
        "Programming Language :: Python",
    ],
    author="nextgis",
    author_email="info@nextgis.com",
    url="https://nextgis.com",
    keywords="geo processing server",
    packages=["avral_hello"],
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points={
        "avral_operations": [
            "hello = avral_hello.operations:HelloWorld",
        ],
    },
)
