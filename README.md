# A list of burner email addresses

**Forked from [/wesbos/burner-email-providers](https://github.com/wesbos/burner-email-providers)**, a fork of [a gist](https://gist.github.com/adamloving/4401361).

This is the PyPI package of the same list, and then some.

## Installation

```
pip install burner-email-providers  # Stable
pip install git+https://github.com/WCF/burner-email-providers.git@master  # Latest, not recommended
```

## Example

```
from burner_email_providers import EMAILS

for domain in EMAILS:
    if 'foo@sharklasers.com'.endswith(domain):
        raise ValueError("You can't use this email!")

```

## Licence

Since there was no licence on [the gist](https://gist.github.com/adamloving/4401361), and there was also no licence on the [repository](https://github.com/wesbos/burner-email-providers), this repository is assumed to be open domain.
If you must require a licence, this repository has an MIT licence included. *THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, ...* applies to this repository regardless.
