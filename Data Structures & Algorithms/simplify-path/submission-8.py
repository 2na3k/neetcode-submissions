class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        split = path.split("/")
        wl = [c for c in split if c != ""]
        print(wl)

        stack = []
        for c in wl:
            if c == "..":
                if len(stack) > 0:
                    stack.pop()
            
            elif c == ".":
                continue
            else:
                stack.append(c)
                

        return "/" + "/".join(stack)