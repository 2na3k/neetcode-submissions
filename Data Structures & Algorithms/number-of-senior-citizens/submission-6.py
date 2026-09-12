class Solution:
    def countSeniors(self, details: List[str]) -> int:
        def func(detail: str) -> bool:
            age_str = detail[11:13]
            return int(age_str) > 60

        res = map(func, details)
        return sum(list(res))   # the most map-reduce shit i've ever seen in