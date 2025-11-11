from myUtils.Utils import printResult

class Solution:
    def simplifyPath(self, path: str) -> str:
      parts = path.split("/")
      parts = list(filter(None, parts))

      s = []
      for p in parts:
        #  print(p)
         if p == ".":
            continue
         if p == "..":
            if len(s) > 0:
              s.pop()
            continue
         s.append(p)
      return "/" + "/".join(s)
    

obj = Solution()

path = "/home/"
expected = "/home"
result = obj.simplifyPath(path)
printResult(result, expected)

path = "/home//foo/"
expected = "/home/foo"
result = obj.simplifyPath(path)
printResult(result, expected)

path = "/home/user/Documents/../Pictures"
expected = "/home/user/Pictures"
result = obj.simplifyPath(path)
printResult(result, expected)

path = "/../"
expected = "/"
result = obj.simplifyPath(path)
printResult(result, expected)

path = "/.../a/../b/c/../d/./"
expected = "/.../b/d"
result = obj.simplifyPath(path)
printResult(result, expected)

