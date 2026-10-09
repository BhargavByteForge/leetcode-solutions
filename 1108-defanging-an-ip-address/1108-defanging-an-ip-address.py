class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans=""
        for i in range(len(address)):
            ch=address[i]
            if ch==".":
                ans+="[.]"
            else:
                ans=ans+ch
        return ans
