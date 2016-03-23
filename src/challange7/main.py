#!/usr/bin/env python

from girl import *
from src.aux.graphs import bfs


def girls_dict_to_graph(girls):
    graph = dict()
    for key in girls:
        friends = girls[key].friends
        adjacents = set()
        for friend in friends:
            adjacents.add(friend.name)
        graph[key] = adjacents
    return graph


def handle_friendship(girls, a, b):
    girls[a].add_friend(girls[b])
    girls[b].add_friend(girls[a])


def store_friendships(girls, num_of_friendships):
    for i in range(num_of_friendships):
        names = raw_input().split(' ')
        while len(names) > 1:
            girl_a = names.pop(0)
            for it in range(len(names)):
                handle_friendship(girls, girl_a, names[it])


def count_graph_points(girls, girl):
    points = 0
    girls_graph = girls_dict_to_graph(girls)
    visited = bfs(girls_graph, girl)
    not_visited = set(girls_graph.keys()) - visited
    for name in not_visited:
        if girls[name].like_shopping():
            points += 5
    return points


def count_max_points(girls):
    max_points = 0
    for girl in girls:
        poll_points = girls[girl].count_points()
        graph_points = count_graph_points(girls, girls[girl].name)
        if (poll_points + graph_points) > max_points:
            max_points = (poll_points + graph_points)
    return max_points


def generate_girls(num_of_girls):
    girls = dict()
    for i in range(num_of_girls):
        girl_info = raw_input().split(' ')
        answers = {'A': girl_info[1], 'B': girl_info[2], 'C': girl_info[3], 'D': girl_info[4], 'E': girl_info[5]}
        name = girl_info[0]
        girls[name] = Girl(name, answers)
    return girls


def main():
    inputs = raw_input().split(' ')
    num_of_girls = int(inputs[0])
    num_of_friendships = int(inputs[1])

    # Storing girls poll info
    girls = generate_girls(num_of_girls)

    # Storing friendships
    store_friendships(girls, num_of_friendships)

    # Counting the maximum
    max_points = count_max_points(girls)
    print max_points


if __name__ == '__main__':
    main()
