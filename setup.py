from setuptools import setup

setup(
    name='example',
    packages=['src'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
