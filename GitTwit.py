from __future__ import absolute_import, division, print_function, unicode_literals

from gittwit.git import TwitterCommit

from gittwit.config import Auth
from gittwit.config import Config
from echomesh.util import Log

LOGGER = Log.logger(__name__)

if __name__ == '__main__':
  result = TwitterCommit.twitter_commit(Config.CONFIG, Auth.AUTH)
  if result:
    LOGGER.info('Twittered %s', result)

