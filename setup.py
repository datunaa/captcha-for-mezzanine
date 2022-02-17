# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from setuptools import setup, find_packages

NAME = 'mezzanine-captcha'
VERSION = '0.0.5'

DESCR = """\
Captcha field for Mezzanine. A hack which can break your fields if you're not careful.

Use with extreme care. Can screw up your field types if you have other apps like this.
Do not use unless you know what you're doing.
"""

AUTHOR = 'John Doe'
AUTHOR_EMAIL = 'test@domain.com'

URL = 'https://github.com/dshubitidze/captcha-for-mezzanine'

setup(
    name=NAME,
    version=VERSION,
    description=DESCR,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools', 'django-simple-captcha>=0.3.4', 'mezzanine']
)

# EOF
