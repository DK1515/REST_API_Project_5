from setuptools import setup

setup(
    name="myhello",
    version='0.1',
    py_modules=['colors'],
    include_package_data=True,
    install_requires=[
        'Click',
        'colorama',
    ],
    entry_points='''
        [console_scripts]
        myhello=hello:cli
    ''',
)
