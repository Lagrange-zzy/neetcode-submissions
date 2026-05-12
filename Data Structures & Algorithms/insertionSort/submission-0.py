# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
from typing import List

class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
    def __repr__(self):
        return f"({self.key}, \"{self.value}\")"

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        states=[]
        for i in range(len(pairs)):
            current_pair=pairs[i]
            j=i-1

            while j>=0 and current_pair.key < pairs[j].key:
                pairs[j+1]=pairs[j]
                j-=1
            pairs[j+1]=current_pair
            states.append(list(pairs))
        return states