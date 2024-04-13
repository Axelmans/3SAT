from itertools import combinations


class SUBSETSUM:

    def __init__(self, items: list):
        self.items = items

    def subsets(self) -> list:
        # Generates all possible subsets: 2^n -> not very efficient for big n.
        subsets = []
        n = len(self.items)
        for r in range(n + 1):
            subsets.extend(combinations(self.items, r))
        return subsets

    def subsetsum(self, wanted_sum: int):
        # Generate all subsets and check if one of them has the desired sum.
        subsets = self.subsets()
        for subset in subsets:
            if sum(subset) == wanted_sum:
                print("Subsetsum found!")
                print(subset)
                return subset
        print("No subsetsum found!")
        return None
