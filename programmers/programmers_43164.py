# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：programmers_43164.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-24 오후 7:58 
'''

"""
    use dfs
"""
from collections import deque


# def bfs(v, graph):
#     result = []
#     visited = []
#     q = deque()
#
#     visited.append(v)
#     q.append(v)
#
#     while q:
#         now = q.popleft()
#         result.append(now)
#         if now in graph.keys():
#             for i in graph[now]:
#                 if i not in visited:
#                     q.append(i)
#                     visited.append(i)
#
#     return result


def solution(tickets):
    answer = []
    graph = {}
    for i in tickets:
        if i[0] in graph.keys():
            graph[i[0]].append(i[1])
        else:
            graph[i[0]] = [i[1]]

    # answer = bfs("ICN", graph)

    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"],
                ["ATL", "ICN"], ["ATL","SFO"]]))