from setuptools import find_packages
import os
from distutils.core import setup

# Serious description from README.md
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''

setup(
    name='seriousity',
    packages=find_packages('.'),
    version='1.0.0',
    description="Serious tool for serious people. I'm serious.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='voilalex',
    author_email='ilya.vouk@gmail.com',
    url='https://github.com/VoIlAlex',
    download_url='https://github.com/VoIlAlex/archive/v1.0.0.tar.gz',
    keywords=[
        'serious',
        'people',
        'importance',
        'love'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Environment :: Console'
    ],
    entry_points="""
    [console_scripts]
    seriousity = seriousity.cli:cli
    """,
    zip_safe=False
)
