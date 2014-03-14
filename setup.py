import os
import sys

from setuptools import setup, find_packages
from distutils.sysconfig import get_python_lib

if "install" in sys.argv:
    lib_paths = [get_python_lib()]
    if lib_paths[0].startswith("/usr/lib/"):
        # We have to try also with an explicit prefix of /usr/local in order to
        # catch Debian's custom user site-packages directory.
        lib_paths.append(get_python_lib(prefix="/usr/local"))
    for lib_path in lib_paths:
        existing_path = os.path.abspath(os.path.join(lib_path, "loloadx"))

EXCLUDE_FROM_PACKAGES = []

version = __import__('mitx_cas_mapper').VERSION

setup(
    name='mitx_cas_mapper',
    version=version,
    url='http://odl.mit.edu',
    author='MITx',
    author_email='mitx-help@mit.edu',
    description=('CAS attribute mapper'),
    license='Proprietary',
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: edX Platform',
        'Intended Audience :: Developers',
        'License :: Proprietary :: Proprietary',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
