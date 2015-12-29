class Solution(object):
    def countAndSay(self, n):

        default = {1 :"1",
        			2 :"11",
        			3 :"21",
        			4 :"1211",
        			5 :"111221",
        			6 :"312211",
        			7 :"13112221",
        			8 :"1113213211",
        			9 :"31131211131221",
        			10 :"13211311123113112211",
        			11 :"11131221133112132113212221",
        			12 :"3113112221232112111312211312113211",
        			13 :"1321132132111213122112311311222113111221131221",
        			14 :"11131221131211131231121113112221121321132132211331222113112211",
        			15 :"311311222113111231131112132112311321322112111312211312111322212311322113212221",
        			16 :"132113213221133112132113311211131221121321131211132221123113112221131112311332111213211322211312113211",
        			17 :"11131221131211132221232112111312212321123113112221121113122113111231133221121321132132211331121321231231121113122113322113111221131221",
        			18 :"31131122211311123113321112131221123113112211121312211213211321322112311311222113311213212322211211131221131211132221232112111312111213111213211231131122212322211331222113112211",
        			19 :"1321132132211331121321231231121113112221121321132122311211131122211211131221131211132221121321132132212321121113121112133221123113112221131112311332111213122112311311123112111331121113122112132113213211121332212311322113212221"}



        if n in default.keys():
        	return default[n]


        n_1 = self.countAndSay(n-1)

        result = ''
        count = 0
        key = n_1[0]
        for i in n_1:

        	if i == key:
        		count += 1
        	else:
        		result+=str(count)+str(key)
        		key = i
        		count = 1
        result+=str(count)+str(key)
        return result
sol = Solution()

import time
start = time.time()

print sol.countAndSay(26)
end = time.time()
        

#print end - start