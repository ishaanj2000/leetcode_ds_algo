
   
    def getPermutation(self, n: int, k: int) -> str:
      # https://www.youtube.com/watch?v=wT7gcXLYoao
      fact = 1
      arr = []
      res = ''
      for i in range(1, n):
        arr.append(i)
        fact *= i
      arr.append(n)
      while True:
        #find the left most element each time
        res += str(arr[math.floor((k-1)/fact)])
        #remove that number from arr 
        arr.pop(math.floor((k-1)/fact))
        if len(arr) == 0:
          break
        #to find which position of number to choose next
        k = k%fact
        #fact value will be divided by size of arr each time
        fact /= len(arr)
      return res
