import string
import nose
from nose.tools import ok_
from unittest import TestCase
from context import hokonui
from hokonui.exchanges.bitx import BitX as btx

class TestBitX(TestCase):

  def setUp(self):
      print(__name__, ': TestClass.setup_class() ----------')

  def tearDown(self):
      print(__name__, ': TestClass.teardown_class() -------')

  def test_name(self):
      ok_(btx.NAME==string.replace(type(self).__name__,'Test',''))

  def test_price(self):
      ok_(btx.get_current_price('ZAR')>0.00)

  def test_bid(self):
      ok_(btx.get_current_bid('ZAR')>0.00)

  def test_ask(self):
      ok_(btx.get_current_ask('ZAR')>0.00)

  def test_orders(self):
      orders = btx.get_current_orders('ZAR',5)
      ok_(len(orders["Asks"])>0, "Asks array should not be empty")
      ok_(len(orders["Bids"])>0, "Bids array should not be empty")
      ok_(orders["Source"]=="BitX", "Source should be 'BitX'")
      ok_(float(orders["Timestamp"])>0,"Timestamp should be greater than zero")
      #raise ValueError(str(orders))