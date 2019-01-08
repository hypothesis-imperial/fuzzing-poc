from hypothesis.strategies import floats, integers
from hypothesis import given
from sender_receiver import Receiver

waits = floats(min_value=0, max_value=10.00000000000001)


@given(waits, integers())
def test_object(wait, id):
    receiver = Receiver(wait, id)
    assert receiver.get_id() < 100
    assert receiver.get_wait() < 5
