class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        og = numbers.copy()
        numbers.sort()

        l=0
        r=len(numbers)-1

        while l<r:
            #find the  numbers needed for the target and do .indexof to find their indicies
            #
            if numbers[l]+numbers[r] > target:
                r-=1
            elif numbers[l]+numbers[r] < target:
                l+=1
    
            elif numbers[l]+numbers[r]==target:
                return [og.index(numbers[l])+1, og.index(numbers[r])+1]
                #write the return statement fir the indicies witu the .idnexof thing

            

