class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        keyArray = self.timeMap[key]
        # start the binary search
        l, r = 0, len(keyArray) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            curTime = keyArray[mid][0]
            if curTime > timestamp:
                r = mid - 1
            elif curTime <= timestamp:
                l = mid + 1
                res = keyArray[mid][1]
        return res