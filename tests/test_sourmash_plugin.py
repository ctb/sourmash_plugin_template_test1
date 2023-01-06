"""
Tests for sourmash_plugin_xyz.
"""
import os
import pytest

import sourmash
import sourmash_tst_utils as utils
from sourmash_tst_utils import SourmashCommandFailed


def test_run_sourmash(runtmp):
    with pytest.raises(SourmashCommandFailed):
        runtmp.sourmash('', fail_ok=True)

    print(runtmp.last_result.out)
    print(runtmp.last_result.err)
    assert runtmp.last_result.status != 0                    # no args provided, ok ;)


def test_sourmash_save(runtmp):
    # can we save a signature w/sourmash?

    # load '47.fa.sig' from test-data directory. This is just a small
    # genome signature that we use for testing a lot ;).
    sig47 = utils.get_test_data('47.fa.sig')

    # place output file in tmp directory
    outfile = runtmp.output('47.test1.sig')

    runtmp.sourmash('sig', 'cat', sig47, '-o', outfile)
    assert os.path.exists(outfile)

    # add whatever tests you need here to verify that your plugin worked!


def test_sourmash_load(runtmp):
    # can we load a signature w/sourmash?

    # replace '47.fa.sig' with one that your plugin generated.
    sig47 = utils.get_test_data('47.fa.sig')

    runtmp.sourmash('sig', 'describe', sig47)

    out = runtmp.last_result.out
    err = runtmp.last_result.out

    print(out, err)

    expected = """signature: NC_009665.1 Shewanella baltica OS185, complete genome
source file: 47.fa
md5: 09a08691ce52952152f0e866a59f6261
k=31 molecule=DNA num=0 scaled=1000 seed=42 track_abundance=0
size: 5177
sum hashes: 5177
signature license: CC0""".splitlines()

    for line in expected:
        assert line in out
