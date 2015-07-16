import nose
from nose.tools import ok_
import os, sys

if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from exchanges.mexbtc import MexBtc as mex
else:
    from ..exchanges.mexbtc import MexBtc as mex

class TestMex():
  
  def setup_func():
    "set up test fixtures"

  def teardown_func():
    "tear down test fixtures"

  def test_price(self):
      #print 'Ask   ', mex.get_current_ask()
      ok_(mex.get_current_price() > 0.00)

  def test_bid(self):
      #print 'Bid   ', mex.get_current_bid()
      ok_(mex.get_current_bid() > 0.00)

  def test_ask(self):
      #print 'Ask   ', mex.get_current_ask()
      ok_(mex.get_current_ask() > 0.00)

  def test_orders(self):
      orders = mex.get_current_orders('USD')
      ok_(len(orders["Asks"])>0, "Asks array should not be empty")
      ok_(len(orders["Bids"])>0, "Bids array should not be empty")
      ok_(orders["Source"]=="ITBIT", "Source should be 'ITBIT'")
      ok_(float(orders["Timestamp"])>0,"Timestamp should be greater than zero")
      #raise ValueError(str(orders))

if __name__ == '__main__':
    nose.runmodule()
