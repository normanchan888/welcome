#!/usr/bin/env python2
# -*-: coding utf-8 -*-

from hermes_python.hermes import Hermes
import json


MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


INTENT_BOOK_FLIGHT = "book_flight"
INTENT_AIRPORT_SELECTION = "airport_selection"


def user_book_flight(hermes, intent_message):
    print("User is booking a flight")

    if intent_message.slots.departcity:
        depart_city = intent_message.slots.departcity.first().value
    if intent_message.slots.arrivecity:
        arrive_city = intent_message.slots.arrivecity.first().value

    hermes.publish_continue_session(intent_message.session_id, "which airport", INTENT_AIRPORT_SELECTION)


def user_airport_selection(hermes, intent_message):
    print("User is selecting an airport")

    session_id = intent_message.session_id

    if intent_message.slots.airport:
        airport = intent_message.slots.airport.first().value

    hermes.publish_end_session(session_id, "Bye"))


def session_started(hermes, session_started_message):
    print("Session Started")

    print("sessionID: {}".format(session_started_message.session_id))
    print("session site ID: {}".format(session_started_message.site_id))

    session_id = session_started_message.session_id


def session_ended(hermes, session_ended_message):
    print("Session Ended")
    session_id = session_ended_message.session_id
    session_site_id = session_ended_message.site_id


with Hermes(MQTT_ADDR) as h:

    h.subscribe_intent(INTENT_BOOK_FLIGHT, user_book_flight) \
        .subscribe_intent(INTENT_AIRPORT_SELECTION, user_airport_selection) \
        .subscribe_session_ended(session_ended) \
        .subscribe_session_started(session_started) \
        .start()
