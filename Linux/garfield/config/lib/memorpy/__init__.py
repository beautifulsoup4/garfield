import logging
logger=logging.getLogger("memorpy")
logger.setLevel(logging.WARNING)
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)
logger.addHandler(ch)

import sys
from .MemWorker import *
from .Locator import *
from .Address import *
from .Process import *
from .utils import *