from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'requests',
]

setup(
    name='tempo_client',
    version='0.0.1',
    description="A Python client to Tempo Timesheet REST API",
    long_description=readme + '\n\n' + history,
    author="Henrik Palmlund Wahlgren @ Palmlund Wahlgren Innovative Technology AB",
    author_email='henrik@pwit.se',
    url='https://github.com/pwitab/tempo-client',
    packages=[
        'tempo_client',
    ],

    include_package_data=True,
    install_requires=requirements,

    license="MIT",
    zip_safe=False,
    keywords=['Tempo', 'Tempo Timesheets', 'Timesheets'],
    classifiers=[

    ],
)