from nose.tools import assert_equal
from reverser import reverse

def test_return():
    assert_equal(reverse.reverse("go"), "og")
