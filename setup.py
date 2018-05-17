"""
Sample project to be edited.
"""

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand
import sys
import os


class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)



dependencies = ['click','pytz',
                'requests', 'docker-py', 'py-cpuinfo', 'ruamel.yaml']

setup(
    name='smartcontainers',
    version='0.0.2',
    url='https://github.com/charlesvardeman/smartcontainers',
    license='Apache Software License',
    author='Charles Vardeman',
    author_email='charles.vardeman@gmail.com',
    description='Tool to track provenance of docker containers',
    long_description=__doc__,
    packages=find_packages(exclude=['tests', 'docs', 'scripts', 'resources']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    python_requires='>=3.5',
    install_requires=dependencies,
    tests_require=['tox'],
    cmdclass = {'test': Tox},
    entry_points={
        'console_scripts': [
            'sc= sc.cli:cli',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
