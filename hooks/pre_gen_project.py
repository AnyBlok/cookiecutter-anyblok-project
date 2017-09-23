import re
import sys


REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

python_package = '{{ cookiecutter.python_package }}'
blok_name = '{{ cookiecutter.blok_name }}'

if not re.match(REGEX, python_package):
    print("ERROR: '%s' is not a valid Python module name!" % python_package)
    # exits with status 1 to indicate failure
    sys.exit(1)

if not re.match(REGEX, blok_name):
    print("ERROR: '%s' is not a valid Blok name!" % blok_name)
    sys.exit(1)
