#!/bin/python3
#----------------------------------------------------------------
#
#   Created by: Amir Azmi
#   Created on: 4 July 2021
#   Updated on:
#
#----------------------------------------------------------------
targs = [ 64, 56, 48, 40, 32, 24 ]

class Solution2:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        res=[]
        self.DFS(candidates,target,0,res,[])
        return res

    def DFS(self,candidates,target,start,res,intermedia):
        if target==0:
            res.append(intermedia)
            return
        for i in range(start,len(candidates)):
            if target<candidates[i]:
                return
            self.DFS(candidates,target-candidates[i],i,res,intermedia+[candidates[i]])


test2=Solution2()
a = [ x for x in range(1,10)]
# print(test2.combinationSum(a,64))

for val in targs:
	ls_comp = sorted( test2.combinationSum(a, val), key=len)
	with open( f"{val} - precomputed_values.txt", "w+") as f:
		for comb in ls_comp:
			f.write( f"{','.join([ str(k) for k in comb])}\n")
		f.close()




