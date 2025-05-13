import csv
from collections import defaultdict, deque
import math 

def build_graph_from_csv(file_path):
    deck_to_cards = defaultdict(set)
    
    # Step 1: Read CSV and collect cards per deck, deduplicated by card name
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            card = row['name'].strip()
            deck = row['deck'].strip()
            deck_to_cards[deck].add(card)

    # Step 2: Build graph edges between all unique card pairs in each deck
    graph = defaultdict(set)
    for cards in deck_to_cards.values():
        card_list = list(cards)
        for i in range(len(card_list)):
            for j in range(i + 1, len(card_list)):
                a, b = card_list[i], card_list[j]
                graph[a].add(b)
                graph[b].add(a)

    return graph

def shortest_path(graph, start, end):
    start, end = start.strip(), end.strip()
    
    if start not in graph or end not in graph:
        return math.inf  # One or both cards not found

    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        current, cost = queue.popleft()
        if current == end:
            return cost
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, cost + 1))

    return math.inf  # No path found
