## porting the main module from python2 to python3.

The very first module is designed by <a href="https://github.com/danrasband/krtpy">Dan Rasband, in 2010.</a>
Few lines in the code with deprecated keywords of python3 are modified.

|   |   |
|---|---|
|python2 | python3 |
|unichr() | chr() |

krtpy
=====

Korean Romanization/Hangulization utility written in python

Installation
============

    $ python setup.py install

Usage
=====

```python
from krt import *

# To hangulize text in the utf8 format:
hangulize('chen')

# To romanize text in the utf8 format:
romanize('천')

# To hangulize text into a different output format:
hangulize('chen', 'euc-kr')

# To romanize text in different input/output formats:
romanize(raw='천',fromEncoding='euc-kr',toEncoding='utf8')
```

