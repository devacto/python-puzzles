from nose.tools import *
from parking.room import Room

def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. 
                There is a door to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})