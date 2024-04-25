from setuptools import setup

VERSION = '0.0.21'
DESCRIPTION = 'Dominion API python wrapper'

setup(
    name='dvpOAuth2',
    version=VERSION,    
    description=DESCRIPTION,
    url='https://github.com/nexant-uts/dvpOAuth2.git',
    author='Resource Innovations',
    author_email='',
    license='BSD 2-clause',
    packages=['dvpOAuth2'],
    install_requires=['requests',
                      'urllib3',
                      'pytest'
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
