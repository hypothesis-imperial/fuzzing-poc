from hypothesis.strategies import text
from hypothesis import given, note
from sender_receiver import Sender, Receiver

msgs = text(min_size=1)


@given(msgs)
def test_message_format(msg):
    x = Sender()
    y = Receiver(5, 1)
    x.send(y, msg)
    note(msg)
    assert y.get_message()[0].isdigit()
