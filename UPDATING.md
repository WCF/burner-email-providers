# First run

```
python setup.py register -r pypitest
# If you are sure
python setup.py register -r pypi
```

# Uploading

Bump the `version` in `setup.py`.

```
python setup.py sdist upload -r pypitest
```

Check under https://testpypi.python.org/pypi/burner-email-providers to see if it was uploaded successfully.
Check under https://testpypi.python.org/simple/burner-email-providers/ to see if it was uploaded successfully.

```
pip install -i https://testpypi.python.org/pypi burner-email-providers==new_version
python setup.py sdist upload -r pypi
```
