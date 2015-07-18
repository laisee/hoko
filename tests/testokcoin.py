import string
import nose
from nose.tools import ok_
from unittest import TestCase

if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from exchanges.okcoin import OKCoin as okc
else:
    from ..exchanges.okcoin import OKCoin as okc

class TestOkCoin(TestCase):

  def test_price(self):
      self.assertNotEqual(okc.get_current_price(),0.00)

  def test_bid(self):
      self.assertNotEqual(okc.get_current_bid(),0.00)

  def test_ask(self):
      self.assertNotEqual(okc.get_current_ask(),0.00)

  def test_orders(self):
      orders = okc.get_current_orders()
      ok_(len(orders["Asks"])>0, "Asks array should not be empty")
      ok_(len(orders["Bids"])>0, "Bids array should not be empty")
      ok_(orders["Source"]=="OKCoin", "Source should be 'OKCoin'")
      ok_(float(orders["Timestamp"])>0,"Timestamp should be greater than zero")

if __name__ == '__main__':
    nosetests.runmodule()
