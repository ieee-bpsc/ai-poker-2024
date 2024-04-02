from pypokerengine.api.game import setup_config, start_poker
import csv
import importlib
from examples.players.fish_player import FishPlayer
from examples.players.fold_man import FoldMan
from examples.players.honest_player import HonestPlayer
import numpy as np

participants = {}

with open("participants.csv", "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    participants = {"Name": [], "Module": []}
    for row in csv_reader:
        participants["Name"].append(row[0])
        participants["Module"].append(row[1])

scores = {}
agents = {}
for i in range(len(participants["Name"])):
    try:
        scores[participants["Name"][i]] = 0
        agents[participants["Name"][i]] = importlib.import_module(
            "submissions." + participants["Module"][i],
        )
    except Exception as e:
        print(e)
        participants["Name"][i] = None

participants["Name"] = [i for i in participants["Name"] if i is not None]


def game(agent):
    config = setup_config(max_round=10, initial_stack=100, small_blind_amount=5)
    config.register_player(name="p1", algorithm=FishPlayer())
    config.register_player(name="p2", algorithm=FoldMan())
    config.register_player(name="p3", algorithm=HonestPlayer())
    config.register_player(name="p4", algorithm=agent.CustomPokerPlayer())

    game_result = start_poker(config, verbose=0)
    return game_result


print(participants)

total_scores = {}


def round_robin():
    for i in range(len(participants["Name"])):
        agent = agents[participants["Name"][i]]
        res = game(agent)
        if participants["Name"][i] not in total_scores:
            total_scores[participants["Name"][i]] = 0
        total_scores[participants["Name"][i]] += res["players"][3]["stack"]
        print(participants["Name"][i], res["players"][3]["stack"])


for i in range(50):
    round_robin()
    print(total_scores)

print(total_scores)
