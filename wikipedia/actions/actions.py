# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
# This is a simple example for a custom action which utters "Hello World!"

import pathlib as p
import os
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionFindPOI(Action):

    def name(self) -> Text:
        return  "action_find_POI"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="search.start")
        for blob in tracker.latest_message['entities']:
            # dispatcher.utter_message(text=f"{tracker.latest_message}")
            if blob['entity'] == 'POI':
                name = blob['value']
                filename = ((name).replace(' ', '_')).lower()
                # knowledge = p.Path(f"data/wikipedia/{name}.txt").read_text().split("\n")
                if os.path.isfile(f"data/wikipedia/{filename}.txt"):
                    dispatcher.utter_message(text=f"{name} was found. What would you like to know about {name}?")
                else:
                    dispatcher.utter_message(text=f"{name} was not found in our database.")
                    
        dispatcher.utter_message(text="search.end")
        return []

class ActionFactSearch(Action):

    knowledge = p.Path(r'data/wikipedia/serena_williams.txt').read_text().split("\n")
    def name(self) -> Text:
        return  "action_fact_search"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="search.start")
        slot_value = tracker.get_slot("POI")
        for blob in tracker.latest_message['entities']:
            dispatcher.utter_message(text=f"{tracker.latest_message}")
            if blob['entity'] == 'POI':
                name = blob['value']
                if name in self.knowledge:
                    dispatcher.utter_message(text=f"{name} was found")
                else:
                    dispatcher.utter_message(text=f"{name} was not found")
                    
        dispatcher.utter_message(text="search.end")
        return []











