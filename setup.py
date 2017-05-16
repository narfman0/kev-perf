from setuptools import setup, find_packages
from kev_perf import __version__ as version


setup(
    name='kev-perf',
    version=version,
    description=('Performance test some kev features'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    keywords='irc bot quip joke jokes',
    author='Jon Robison',
    author_email='narfman0@gmail.com',
    url='https://github.com/narfman0/kev-perf',
    license='LICENSE',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=['kev', ],
    test_suite='tests',
)
