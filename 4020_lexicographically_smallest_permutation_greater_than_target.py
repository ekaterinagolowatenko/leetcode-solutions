class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt={}
        for char in s:
            cnt[char]=cnt.get(char, 0)+1
        for char in target:
            cnt[char]=cnt.get(char, 0)-1
        
        n=len(target)
        for i in range(n-1,-1,-1):
            cnt[target[i]]+=1
            if min(cnt.values())>=0:
                suffix = ""
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if cnt.get(c, 0) > 0 and c > target[i]:
                        cnt[c] -= 1
                        suffix = ""
                        for char in "abcdefghijklmnopqrstuvwxyz":
                            suffix+=char*cnt.get(char, 0)
                        ans = target[:i] + c + suffix
                        return ans
        return ''