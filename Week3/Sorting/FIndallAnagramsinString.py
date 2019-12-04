class Solution(object):
    def findAnagrams(self, s, p):
        ans = []
        p = list(sorted(p))
        length = len(p)
        st = list(s[0:length - 1])
        i = length -1
        while i < len(s):
            st.append(s[i])
            if sorted(st) == p:
                ans.append(i - (length-1))
            del st[0]
            i += 1
        return ans