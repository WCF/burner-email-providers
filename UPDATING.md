# First run

```
python setup.py register -r pypitest
# If you are sure
python setup.py register -r pypi
```

(You'll likely get "Project pre-registration is no longer required or supported, upload your files instead", but try it out anyway.)

# Uploading

Make your changes.

Bump the `version` in `setup.py`.

Run this:

```
python setup.py sdist upload -r pypitest
```

Check under https://testpypi.python.org/pypi/burner-email-providers to see if it was uploaded successfully.
Check under https://testpypi.python.org/simple/burner-email-providers/ to see if it was uploaded successfully.

Test your package by installing it.

```
pip install -i https://testpypi.python.org/pypi burner-email-providers==new_version
```

Finally, upload it to the real PyPI.

```
python setup.py sdist upload -r pypi
```
