class TimeMap:

    def __init__(self):
        self.kv = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kv:
            self.kv[key] = {}
        if timestamp not in self.kv[key]:
            self.kv[key][timestamp] = []
        self.kv[key][timestamp].append(value)
        print(self.kv)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv:
            return ""
        
        seen = 0

        for t in self.kv[key]:
            if t <= timestamp:
                seen = max(seen, t)
        
        return "" if seen == 0 else self.kv[key][seen][-1]
