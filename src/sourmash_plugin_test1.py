"Read/write sketches via plugin."
import sourmash

from sourmash.index import LinearIndex
from sourmash.logging import debug_literal, notify

from sourmash.save_load import (Base_SaveSignaturesToLocation,
                                _get_signatures_from_rust)


###

#
# load_from plugin
#

def load_sketches(location, *args, **kwargs):
    if location and location.endswith('.test1.sig'):
        # ... add your code here ...
        notify(f'*** test1 plugin is at work! Reading from {location}')
        with open(location, 'rb') as fp:
            siglist = list(sourmash.load_signatures(location))
        return LinearIndex(siglist, location)

load_sketches.priority = 5


#
# save_to plugin - supports output to .xyz
#

class SaveSignatures_Test1(Base_SaveSignaturesToLocation):
    "Save signatures to a location."
    def __init__(self, location):
        super().__init__(location)
        self.keep = []

    @classmethod
    def matches(self, location):
        # match anything that is not None or ""
        if location:
            notify(f"*** test1 plugin matches {location}! using!")
            return location.endswith('.test1.sig')

    def __repr__(self):
        return f"SaveSignatures_Test1('{self.location}')"

    def open(self):
        pass

    def close(self):
        # actually do the writing...
        with open(self.location, 'wb') as fp:
            notify("*** test1 plugin is writing!")
            sourmash.save_signatures(self.keep, fp)

    def add(self, ss):
        super().add(ss)
        self.keep.append(ss)

#
# CLI command - 'sourmash scripts xyz'
#


class ScriptsCommand_Test1:
    command = "test1"
    description = "do something test1"

    def __init__(self, subparser):
        "Initialize command. Use argparse 'add_argument' to add arguments."
        # edit, add, remove these as you need!
        subparser.add_argument("filename_test", help="input file")
        subparser.add_argument("-x", "--xyz", action="store_true",
                               help="boolean flag to turn on behavior.")

    def main(self, args):
        "The actual code to do something."
        notify("RUNNING command {self.command}")
        notify("received argument: '{args.filename_test}'")
        notify("flag xyz value: {args.xyz}")
