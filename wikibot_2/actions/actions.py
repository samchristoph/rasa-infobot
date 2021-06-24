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
                    if name in cur_name:
                        if name == cur_name:
                            dispatcher.utter_message(text=f"'{name}' exists in our system")
                        else:
                            dispatcher.utter_message(text=f"{name} ==> {cur_name}")
        dispatcher.utter_message(text="search.end")
        return []


class ActionFactSearch(Action):
        
    def name(self) -> Text:
        return  "action_fact_search"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        players = p.Path(f"data/statistics/player_list_full.txt").read_text('utf-8').split("\n")
        POI = ""
        for blob in tracker.latest_message['entities']:
            if blob['entity'] == 'name':
                for idx in range(len(players)):
                    name = blob['value'].lower()
                    cur_name = players[idx].lower()
                    if name in cur_name:
                        if name == cur_name:
                            POI = name
                            dispatcher.utter_message(text=f"'{name}' exists in our system")
                        else:
                            dispatcher.utter_message(text=f"{name} ==> {cur_name}")
        if len(POI) == 0:
            dispatcher.utter_message(text="query failed")
            return []
        
        knowledge_men = p.Path(f"data/statistics/all_time_wins_men.txt").read_text('utf-8').split("\n")
        knowledge_women = p.Path(f"data/statistics/all_time_wins_women.txt").read_text('utf-8').split("\n")
        stats_collective = p.Path(f"data/statistics/stats_collective.txt").read_text('utf-8').split("\n")
        status = False
        
        for idx in range(len(knowledge_men)):
            player_stats = knowledge_men[idx].split("\t")
            player_stats_compact = ""
            for item in player_stats:
                player_stats_compact += item.lower()
            POI_compact = POI.replace(" ", "")
            player_stats_compact = player_stats_compact.replace(" ", "")
            print(POI_compact, " ==> ", player_stats_compact)
            if POI_compact in player_stats_compact and len(player_stats) >= 10:
                status = True
                dispatcher.utter_message(text=f"Player: '{POI}'")
                dispatcher.utter_message(text=f"Total Titles: {player_stats[3]}")
                dispatcher.utter_message(text=f"Total Finales: {player_stats[4]}")
                dispatcher.utter_message(text=f"Single Titles: {player_stats[5]}")
                dispatcher.utter_message(text=f"Single Finales: {player_stats[6]}")
                dispatcher.utter_message(text=f"Double Titles: {player_stats[7]}")
                dispatcher.utter_message(text=f"Double Finales: {player_stats[8]}")

        for idx in range(len(knowledge_women)):
            player_stats = knowledge_women[idx].split("\t")
            player_stats_compact = ""
            for item in player_stats:
                player_stats_compact += item.lower()
            POI_compact = POI.replace(" ", "")
            player_stats_compact = player_stats_compact.replace(" ", "")
            print(POI_compact, " ==> ", player_stats_compact)
            if POI_compact in player_stats_compact and len(player_stats) >= 10:
                status = True
                dispatcher.utter_message(text=f"Player: '{POI}'")
                dispatcher.utter_message(text=f"Total Titles: {player_stats[3]}")
                dispatcher.utter_message(text=f"Total Finales: {player_stats[4]}")
                dispatcher.utter_message(text=f"Single Titles: {player_stats[5]}")
                dispatcher.utter_message(text=f"Single Finales: {player_stats[6]}")
                dispatcher.utter_message(text=f"Double Titles: {player_stats[7]}")
                dispatcher.utter_message(text=f"Double Finales: {player_stats[8]}")

        for idx in range(len(stats_collective)):
            player_stats = stats_collective[idx].split("\t")
            player_stats_compact = ""
            for item in player_stats:
                player_stats_compact += item.lower()
            POI_compact = POI.replace(" ", "")
            player_stats_compact = player_stats_compact.replace(" ", "")
            print(POI_compact, " ==> ", player_stats_compact)
            if POI_compact in player_stats_compact:
                status = True
                dispatcher.utter_message(text=f"Player: '{POI}'")
                dispatcher.utter_message(text=f"{stats_collective[idx]}")

        if status == False:
            dispatcher.utter_message(text=f"no rankings found for {POI}")
        return []



'''
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
'''








