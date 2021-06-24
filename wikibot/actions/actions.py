# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
# This is a simple example for a custom action which utters "Hello World!"

import pathlib as p
import os
from typing import Any, Text, Dict, List
import rasa_sdk.events as rasaEvents
from rasa_sdk import Action, Tracker
# from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


class ActionFindName(Action):
       
    def name(self) -> Text:
        return  "action_find_name"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="search.start")
        players = p.Path(f"data/statistics/player_list_full.txt").read_text('utf-8').split("\n")
        for blob in tracker.latest_message['entities']:
            if blob['entity'] == 'name':
                for idx in range(len(players)):
                    name = blob['value'].lower()
                    cur_name = players[idx].lower()
                    print(cur_name, " <==> ", name)
                    if cur_name == name:
                        dispatcher.utter_message(text=f"'{name}' exists in our system")
        
        dispatcher.utter_message(text="search.end")
        return []


class ActionFactSearch(Action):
    
    knowledge = ""
    
    def name(self) -> Text:
        return  "action_fact_search"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="search.start")
        players = p.Path(f"data/statistics/player_list_full.txt").read_text('utf-8').split("\n")
        for blob in tracker.latest_message['entities']:
            if blob['entity'] == 'name':
                for idx in range(len(players)):
                    name = blob['value'].lower()
                    cur_name = players[idx].lower()
                    print(cur_name, " <==> ", name)
                    if cur_name == name:
                        dispatcher.utter_message(text=f"'{name}' exists in our system")
        for blob in tracker.latest_message['entities']:
            if blob['entity'] == 'name':
                POI = blob['value'].lower()
                filename = ((POI).replace(' ', '_'))
                if os.path.isfile(f"data/wikipedia/{filename}.txt"):
                    self.knowledge = p.Path(f"data/wikipedia/{filename}.txt").read_text('utf-8').split("\n")
                else:
                    dispatcher.utter_message(text=f"{POI} was not found in our database")
                    return []
        
        if len(self.knowledge) == 0:
            dispatcher.utter_message(text=f"the request failed")
            return []
        

        message = ""
        for blob in tracker.latest_message['entities']:            
            if blob['entity'] == 'person' \
            or blob['entity'] == 'name' \
            or blob['entity'] == 'pronoun' \
            or blob['entity'] == 'keyword' \
            or blob['entity'] == 'interrogative':
                name = blob['value']
                for idx in range(len(self.knowledge)):
                    if name.lower() in self.knowledge[idx].lower():
                        message += f"{self.knowledge[idx]}\n"
                        dispatcher.utter_message(text=f"Idx: {idx}, Found '{name}': Y")
                    else:
                        pass
                        # dispatcher.utter_message(text=f"Idx: {idx}, Found '{name}': N")
        
        dispatcher.utter_message(text="search.end")
        if len(message):
            dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text="failed to locate information")
        
        return []











