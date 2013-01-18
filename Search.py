from __future__ import absolute_import, division, print_function, unicode_literals

import sys

from echomesh.util import Log
from gittwit.twitter import MultiSearch

LOGGER = Log.logger(__name__)

def print_twitter(twitter):
  print('name:', twitter['user_name'])
  print('text:', twitter['text'])
  print()

MULTISEARCH = MultiSearch.MultiSearch(print_twitter)

for arg in sys.argv[1:]:
  MULTISEARCH.add(arg)

while MULTISEARCH.is_open:
  tag = raw_input('Enter a tag or quit to exit\n').strip().split()
  if tag:
    command = tag[0]
    if command == 'quit':
      MULTISEARCH.close()
    elif command == 'add':
      for tag in tag[1:]:
        MULTISEARCH.add(tag)
    elif command == 'remove':
      for tag in tag[1:]:
        MULTISEARCH.remove(tag)
    else:
      LOGGER.error("Don't understand command '%s'", command)


