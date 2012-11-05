"""

>>> String.truncate('hello', 6)
u'hello'

>>> String.truncate('hello', 5)
u'hello'

>>> String.truncate('hello', 4)
u'h...'

>>> String.truncate('hello', 3)
u'...'

>>> String.truncate('hello', 2)
u'..'

>>> String.truncate('hello', 1)
u'.'

>>> String.truncate('hello', 0)
u''

>>> String.truncate_suffix('hello', ' suf', 9)
u'hello suf'

>>> String.truncate_suffix('hello', ' suf', 8)
u'h... suf'

>>> String.truncate_suffix('hello', ' suf', 7)
u'... suf'

>>> String.truncate_suffix('hello', ' suf', 6)
u'.. suf'

>>> String.truncate_suffix('hello', ' suf', 5)
u'. suf'

>>> String.truncate_suffix('hello', ' suf', 4)
u' suf'
"""

from __future__ import absolute_import, division, print_function, unicode_literals

from util import String

if __name__ == "__main__":
  import doctest
  doctest.testmod()
