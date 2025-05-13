from graph import build_graph_from_csv, shortest_path
from visualize import visualize_graph
from utils import find_median

drafted = [
    "Illidari Studies",
    "Felrattler",
    "Snake Eyes",
    "Venomous Scorpid",
    "School Teacher",
    "Immolation Aura","Immolation Aura",
    "Nightmare Dragonkin","Nightmare Dragonkin",
    "Spectral Sight",
    "Sunwell Initiate",
    "Mad Bomber",
    "Chaos Strike",
    "Herald of Chaos",
    "Amalgam of the Deep",
    "Royal Librarian",
    "Ferocious Felbat",
    "Dire Wolf Alpha",
    "Gan'arg Glaivesmith",
    "Midnight Wolf",
    "Vilefiend Trainer",
    "Miracle Salesman",
    "Coilskar Commander",
    "Bone Glaive",
    "Ravenous Felhunter",
    "Soulshard Lapidary",
    "Horseshoe Slinger",
    "School Teacher",
    "Parched Desperado",
    "Fan the Hammer"

]

candidate = [
    ""
]

graph = build_graph_from_csv("demon_hunter.csv")

for card in candidate:
    cost_list = []
    for draft in drafted:
        cost = shortest_path(graph, card, draft)
        cost_list.append(cost)
    median = find_median(cost_list)
    min_value = min(cost_list)
    print("Candidate:", card, ' Median cost:', median,' Min cost:', min_value)

visualize_graph(graph, drafted)
