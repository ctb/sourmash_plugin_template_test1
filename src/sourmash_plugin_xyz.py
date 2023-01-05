"Read/write sketches via plugin."

# TODO:
# * add support for other moltypes

import sourmash

from sourmash.index import LinearIndex
from sourmash.logging import debug_literal

from sourmash.save_load import (Base_SaveSignaturesToLocation,
                                _get_signatures_from_rust)


###

#
# load_from plugin
#

def load_sketches(location, *args, **kwargs):
    if location and location.endswith('.xyz'):
        # ... add your code here ...
        # return LinearIndex(siglist)
        pass

load_sketches.priority = 5


#
# save_to plugin - supports output to .xyz
#

class SaveSignatures_XYZ(Base_SaveSignaturesToLocation):
    "Save signatures to a location."
    def __init__(self, location):
        super().__init__(location)
        self.keep = []

    @classmethod
    def matches(self, location):
        # match anything that is not None or ""
        if location:
            return location.endswith('.xyz')

    def __repr__(self):
        return f"SaveSignatures_AvroFile('{self.location}')"

    def open(self):
        pass

    def close(self):
        # actually do the writing...
        pass

    def add(self, ss):
        super().add(ss)
        self.keep.append(ss)
