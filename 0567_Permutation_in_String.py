class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lenS1 = len(s1)
        dictS1 = defaultdict(int)
        dictS2 = defaultdict(int)
        
        for ch in s1: # s1에 대한 dict 생성
            dictS1[ch] += 1
        
        for i in range(len(s2)) : # s2의 lenth 만큼 돌면서 dict 생성 
            dictS2[s2[i]] += 1
            if i >= lenS1 :  # 만약 길이가 s1보다 커졌다면, 앞에 문자를 dict에서 삭제 
                dictS2[s2[i-lenS1]] -= 1 # dict에서 cnt 하나 감소
                if(dictS2[s2[i-lenS1]] == 0): # 혹은 삭제
                    del dictS2[s2[i-lenS1]]
            if dictS1 == dictS2 :  # 같은 dict가 있다면 true
                return True
        return False