import setuptools
import subprocess
from setuptools.command.develop import develop
from pragma_utils.version import __VERSION__

# shim to install dev depenedencies on 'setup.py develop'
class ExtDevelop(develop):
    def install_for_development(self):
        from distutils import log
        develop.install_for_development(self)
        if 'develop' in self.distribution.extras_require:
            log.info('\nInstalling development dependencies')
            requirements = ' '.join(self.distribution.extras_require['develop'])
            proc = subprocess.Popen('pip install ' + requirements, shell=True)
            proc.wait()


setuptools.setup(
    name='pragma_utils',
    version=__VERSION__,
    description='Misc utilities to small for their own projects',
    long_description=open('README.md').read().strip(),
    author='Eric Anderton',
    author_email='eric.t.anderton@gmail.com',
    url='http://github.com/eanderton/pragma-utils',
    packages=['pragma_utils'],
    test_suite='tests',
    install_requires=[
        'ansicolors',
    ],
    extras_require={
        'develop': ['coverage'],
    },
    cmdclass= {
        'develop': ExtDevelop,
    },
    license='MIT License',
    zip_safe=False,
    keywords='parser parsers dfa lexer lexers',
    classifiers=[
        'Packages'
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ])
