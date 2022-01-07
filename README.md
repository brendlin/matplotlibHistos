
How to install the package via pip
--------

This package is not yet registered on pypi, and therefore to install the package, one must
check it out from github and install it locally.

The package defined using the following files:
 - `pyproject.toml`
 - `setup.py` (dynamic definitions)
 - `setup.cfg` (static definitions; not used as extensively as `setup.py`)

To install, navigate to the base directory:
```
cd matplotlibHistos
pip install -e .
```

To re-install after making local changes:
```
# pip install --upgrade -e . # apparently this does not work
pip uninstall matplotlibHistos
pip insall -e .
```
To verify that it was installed correctly, you can run `pip show matplotlibHistos`.



How to load the package contents
--------

From a python prompt:

```python
from matplotlibHistos import Histo
my_histo = Histo.Histo([0,1,2,3])
```
or
```python
from matplotlibHistos.Histo import Histo
my_histo = Histo([0,1,2,3])
```
or finally (enabled inside `matplotlibHistos/__init__.py`):
```
import matplotlibHistos as mplh
my_histo = mplh.Histo([0,1,2,3])
```

or
```
from matplotlibHistos import Histo
my_hist = Histo([0,1,2,3])
```
