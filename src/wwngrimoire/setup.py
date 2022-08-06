from setuptools import setup, find_packages

setup(
    name='wwngrimoire',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'wg = wwngrimoire.__init__:main'
        ]
    }
)