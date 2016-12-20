from setuptools import setup, find_packages
from helga_meet import __version__ as version


setup(
    name="helga-meet",
    version=version,
    description=('System for asynchronous meetings e.g. standup'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
    ],
    keywords='irc bot meet',
    author='Jon Robison',
    author_email='narfman0@gmail.com',
    license='LICENSE',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=['helga', 'apscheduler', 'requests'],
    test_suite='tests',
    entry_points=dict(
        helga_plugins=[
            'meet = helga_meet.helga_meet:meet',
        ],
    ),
)
