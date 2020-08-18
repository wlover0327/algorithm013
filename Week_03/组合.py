class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def process(level, start, pre):
            if level == k:
                result.append(pre)
                return
            for i in range(start, n - k + len(pre) + 2):
                process(level + 1, i + 1, pre + [i])

        process(0, 1, [])
        return result
