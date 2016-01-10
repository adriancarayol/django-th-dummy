from setuptools import setup, find_packages
from th_dummy import __version__ as version
import os


def strip_comments(l):
    return l.split('#', 1)[0].strip()


def reqs(*f):
    return list(filter(None, [strip_comments(l) for l in open(
        os.path.join(os.getcwd(), *f)).readlines()]))

install_requires = reqs('requirements.txt')

setup(
    name='django_th_dummy',
    version=version,
    description='Django Trigger Happy : This handles the Dummy service',
    author='FoxMaSk',
    author_email='foxmask@trigger-happy.eu',
    url='https://github.com/foxmask/django-th-dummy',
    download_url="https://github.com/foxmask/django-th-dummy/archive/trigger-happy-dummy-"
    + version + ".zip",
    packages=find_packages(exclude=['th_dummy/local_settings']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django',
    ],
    install_requires=install_requires,
    include_package_data=True,
)
