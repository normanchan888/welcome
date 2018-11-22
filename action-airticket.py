#!/usr/bin/env python2
from hermes_python.hermes import Hermes

def intent_received(hermes, intent_message):
    print('Intent {}'.format(intent_message.intent.intent_name))

    for (slot_value, slot) in intent_message.slots.items():
        print('Slot {} -> \n\tRaw: {} \tValue: {}'.format(slot_value, slot[0].raw_value, slot[0].slot_value.value.value))

    hermes.publish_end_session(intent_message.session_id, None)

with Hermes('10.81.0.223:1883') as h:
    h.subscribe_intents(intent_received).start()
