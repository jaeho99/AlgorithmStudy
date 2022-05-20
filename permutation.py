from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    results = []
    prev_elements = []
    
    def dfs(elements):
        if len(elements) == 0:
            results.append(prev_elements[:])

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)
            print(f'results : {results} dfs 종료')
            print()
            prev_elements.append(e)
            print(f'elements : {elements}, prev_elements : {prev_elements}, next_elements : {next_elements}, dfs 호출')
            dfs(next_elements)
            print("간디")
            prev_elements.pop()
    print(f"assasa{nums}")
    dfs(nums)
    return results


a = [1, 2, 3]
print(permute(a))

