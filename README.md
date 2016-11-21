Install
=======

pip install cbktree


Changelog
=========

* 0.2.0: updated from https://github.com/fake-name/IntraArchiveDeduplicator/commit/7ef8329cc9714116cf70c5fca09d7fa334506d4d
    * fixed https://github.com/fake-name/IntraArchiveDeduplicator/issues/2
    * added `cbktree.__version__`
* 0.1.0: initial version


Original source
===============

https://github.com/fake-name/IntraArchiveDeduplicator/tree/master/deduplicator


Example
=======

```python
from cbktree import BkHammingTree, explicitSignCast

DATA = {
    # Format: id -> bitstring
    1: '1011010010010110110111111000001000001000100011110001010110111011',
    2: '1011010010010110110111111000001000000001100011110001010110111011',
    3: '1101011110100100001011001101001110010011100010011101001000110101',
}

SEARCH_DIST = 2  # 2 out of 64 bits

int_bits = lambda b: explicitSignCast(int(b, 2))


tree = BkHammingTree()
descriptor = {}
for node_id, bits in DATA.items():
    ib = int_bits(bits)
    descriptor[node_id] = ib
    tree.insert(ib, node_id)

# Find near matches for each node that was inserted.
for node_id, ib in descriptor.items():
    res = tree.getWithinDistance(ib, SEARCH_DIST)
    print("{}: {}".format(node_id, res))

# Find near matches for items that were not inserted.

new = '1101011110100100001011001101001110010011100010011101001000110101'
print("new: {}".format(tree.getWithinDistance(int_bits(new), SEARCH_DIST)))

ones = '1' * 64
print("111..: {}".format(tree.getWithinDistance(int_bits(ones), SEARCH_DIST)))

# XXX Should return empty, returns [0] instead.
zeroes = '0' * 64
print("000..: {}".format(tree.getWithinDistance(int_bits(zeroes), SEARCH_DIST)))
```
