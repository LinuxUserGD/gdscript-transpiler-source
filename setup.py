#!/usr/bin/env python
from setuptools import setup, find_packages
# Parse version number from gds/version.py:
with open('gds/version.py') as f:
    info = {}
    for line in f:
        if line.startswith('__version__'):
            exec(line, info)
            break
setup_info = dict(
    name='gds',
    version=info['__version__'],
    author='LinuxUserGD',
    author_email='hugegameartgd@gmail.com',
    url='https://codeberg.org/LinuxUserGD/gdscript-transpiler-bin',
    download_url='https://linuxusergd.itch.io/gdscript-transpiler-bin',
    project_urls={
        'Documentation': 'https://codeberg.org/LinuxUserGD/gdscript-transpiler-bin/wiki',
        'Source': 'https://codeberg.org/LinuxUserGD/gdscript-transpiler-bin',
        'Tracker': 'https://codeberg.org/LinuxUserGD/gdscript-transpiler-bin/issues',
    },
    description='GDScript and Python runtime environment',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Bootstrapping',
        'Topic :: Python :: GDScript :: Python Modules',
    ],
    # Package info
    packages=['gds'] + ['gds.' + pkg for pkg in find_packages('gds')],
    # Add _ prefix to the names of temporary build dirs
    options={'build': {'build_base': '_build'}, },
    zip_safe=True,
)
setup(**setup_info)
