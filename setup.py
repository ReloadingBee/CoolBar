from setuptools import setup, find_packages
from pathlib import Path


VERSION = "0.5.7"


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name='CoolBar',
    packages=find_packages(),
    version=VERSION,
    license='Apache-2.0',
    description='Dynamic Python Progress Bar',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='ReloadingBee',
    author_email='reloadingbee@gmail.com',
    url='https://github.com/ReloadingBee/CoolBar',
    download_url=f'https://github.com/ReloadingBee/CoolBar/archive/v_{VERSION}.tar.gz',
    keywords=['progress', 'loading', 'bar', 'dynamic', 'python'],
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Terminals',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
    ],
)
