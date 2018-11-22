#!/usr/bin/env python2
from hermes_python.hermes import Hermes

def intent_received(hermes, intent_message):
    print('Intent {}'.format(intent_message.intent.intent_name))
    for (slot_value, slot) in intent_message.slots.items():
        print('Slot {} -> \n\tRaw: {} \tValue: {}'.format(slot_value, slot[0].raw_value, slot[0].slot_value.value.value))

    if intent_message.intent.intent_name == 'normanchan888:book_flight' :
        if intent_message.slots.departcity:
            depart_city = intent_message.slots.departcity.first().value
        if intent_message.slots.arrivecity:
            arrive_city = intent_message.slots.arrivecity.first().value
        hermes.publish_continue_session(intent_message.session_id, "which airport", "normanchan888:airport_selection")
        
    elif intent_message.intent.intent_name == 'normanchan888:airport_selection' :
        if intent_message.slots.airport:
            airport = intent_message.slots.airport.first().value
        hermes.publish_end_session(intent_message.session_id, "Bye")

with Hermes("10.81.0.223:1883") as h:
    h.subscribe_intents(intent_received).start()
