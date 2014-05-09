"""luppy
======

.. _docs: https://4ch.readthedocs.org
.. _repo: https://github.com/plausibility/4ch

luppy is a wrapper to the lupchan/tinyboard 4chan-style JSON API, provided by nanasi. It allows you to interact with lupchan (in a READONLY way) easily through your scripts.
Currently this will not work at all because nanasi still needs to update tinyboard and enable API.
In the future I plan to include a posting method since lupchan has no captchas.
luppy is a fork of `plausibility/4ch <https://github.com/plausibility/4ch>`_. Almost all of the code is not mine, so refer to 4ch for usage and things.

Requirements
------------

- Python 2.7 (what I test with, 2.x might work)
- requests

Notes
-----

- This isn't guaranteed to work all the time; after all, the API may change, and 4ch will have to be updated accordingly.
- If a feature is missing, open an issue on the `4ch repo`_, and it may well be implemented.
- If the feature is lupchan/tinyboard specific, open it on the luppy repo instead.

Running / Usage
---------------

- Currently no installation method
- See the `4ch docs`_

Contributing
------------
If you're interested in contributing to the usability of luppy, or just want to give away stars, you can visit the 4ch github `repo`_.
"""
from setuptools import setup

if __name__ != "__main__":
    import sys
    sys.exit(1)

kw = {
    "name": "luppy",
    "version": "0.3.0",
    "description": "Python wrapper for the lupchan/tinyboard 4chan-style JSON API.",
    "long_description": __doc__,
    "url": "https://github.com/feblehober123/luppy",
    "author": "plausibility",
    "author_email": "chris@gibsonsec.org",
    "license": "MIT",
    "packages": ['luppy'],
    "install_requires": ["requests"],
    "zip_safe": False,
    "keywords": "wrapper lupchan chan json",
    "classifiers": [
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2"
    ]
}

if __name__ == "__main__":
    setup(**kw)
