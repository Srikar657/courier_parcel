
from courier import *

def setup_function():
    parcels.clear()

def test_add():
    assert add_parcel(101, "Ram", "Sam") == "Parcel Added"

def test_track():
    add_parcel(102, "Ram", "Sam")
    assert track_parcel(102)[0] == "Ram"

def test_invalid_track():
    assert track_parcel(999) == "Parcel Not Found"

def test_update():
    add_parcel(103, "Ram", "Sam")
    assert update_status(103, "Delivered") == True
    assert track_parcel(103)[2] == "Delivered"

def test_delete():
    add_parcel(104, "Ram", "Sam")
    assert delete_parcel(104) == True

def test_invalid_delete():
    assert delete_parcel(999) == False
