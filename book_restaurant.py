#!/usr/bin/env python2
from hermes_python.hermes import Hermes

def intent_received(hermes, intent_message):
    print('Intent {}'.format(intent_message.intent.intent_name))
    for (slot_value, slot) in intent_message.slots.items():
        print('Slot {} -> \n\tRaw: {} \tValue: {}'.format(slot_value, slot[0].raw_value, slot[0].slot_value.value.value))

    if intent_message.intent.intent_name == 'normanchan888:BookRestaurant' :
        if intent_message.slots.booked_restaurant:
            booked_restaurant = intent_message.slots.booked_restaurant.first().value
        hermes.publish_continue_session(intent_message.session_id, "For how many persons", ["normanchan888:SetNumOfPersons"])
        
    elif intent_message.intent.intent_name == 'normanchan888:SetNumOfPersons' :
        if intent_message.slots.NumOfPersons:
            NumOfPersons = intent_message.slots.NumOfPersons.first().value
        hermes.publish_continue_session(intent_message.session_id, "For what time", ["normanchan888:SetBookingTime"])
        
    elif intent_message.intent.intent_name == 'normanchan888:SetBookingTime' :
        if intent_message.slots.BookingTime:
            BookingTime = intent_message.slots.BookingTime.first().value
        hermes.publish_end_session(intent_message.session_id, "I have booked the table")

with Hermes("10.81.0.34:1883") as h:
    h.subscribe_intents(intent_received).start()
