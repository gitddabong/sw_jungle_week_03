# -*- coding: UTF-8 -*-
'''
@Project ：sw_jungle_week_03 
@File ：programmers_43163.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2021-11-24 오후 4:45 
'''
import copy


def dfs(begin, target, words, level):
    candidate = []
    if target == begin:
        return level

    for i in words:
        # print(begin, i)
        only_one = 0
        for j in range(len(begin)):
            if i[j] == begin[j]:
                only_one+=1
        if only_one >= len(begin)-1:
            temp = copy.deepcopy(words)
            temp.remove(i)
            # print(begin, i, only_one, len(begin))
            candidate.append([i, temp])
    # print(1)
    # print(candidate)

    # if not candidate:
    #     return 0

    ans = float('inf')
    for i in candidate:
        tmp = dfs(i[0], target, i[1], level+1)
        ans = min(ans, tmp)

    return ans



def solution(begin, target, words):
    if target not in words:
        return 0

    answer = dfs(begin,target,words,0)

    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))