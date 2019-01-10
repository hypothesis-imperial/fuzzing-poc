from hypothesis.strategies import integers
from hypothesis import given
from sender_receiver import Receiver

# waits = floats(min_value=0, max_value=10.00000000000001)


@given(integers())
def test_object(id):
    receiver = Receiver(10, id)
    assert receiver.get_id() < 5
