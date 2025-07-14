# Customized from donnemartin/data-science-ipython-notebooks
# Original: https://github.com/donnemartin/data-science-ipython-notebooks
# Cloned on: 2025-07-14

from nose.tools import assert_equal
from ..type_util import TypeUtil


class TestUtil():

    def test_is_iterable(self):
        assert_equal(TypeUtil.is_iterable('foo'), True)
        assert_equal(TypeUtil.is_iterable(7), False)

    def test_convert_to_list(self):
        assert_equal(isinstance(TypeUtil.convert_to_list('foo'), list), True)
        assert_equal(isinstance(TypeUtil.convert_to_list(7), list), False)