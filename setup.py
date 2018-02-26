from setuptools import setup

setup(
    name='notes',
    version='0.0.1',
    packages=['notes'],
    entry_points={
        'console_scripts': [
            'notes = notes.__main__:main'
        ]
    }
)
