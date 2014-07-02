from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
	packages=['rqt_overview'],
	package_dir={'': 'src'},
	scripts=['scripts/rqt_overview']
)

setup(**setup_args)