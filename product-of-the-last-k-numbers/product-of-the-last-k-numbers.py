
'''

■■■■■■■■■ PROBLEM ■■■■■■■■■
PRODUCT OF LAST K NUMBERS


■■■■■■■■■ EDGE ■■■■■■■■■
■ at least k nums k <= stream
■ no overflow
■ k > 0

■■■■■■■■■ EXAMPLE ■■■■■■■■■
Input
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

Output
[null,null,null,null,null,null,20,40,0,null,32]

notes: order is relevant, ideally accessing 

■■■■■■■■■ BRUTE ■■■■■■■■■
dunder init 
initial empty list 
track size

add 
append whatever num
update size of list



getProduct 


we'll get the slice of the last k numbers and multiple

24, 24, 12, 4

1,2,3,4

5 

5
■■■■■■■■■ PSEUDO ■■■■■■■■■

■■■■■■■■■ CODE ■■■■■■■■■
'''
class ProductOfNumbers:
    def __init__(self):
        self.data = []
        self.product = 1

    def add(self, num: int) -> None:
        if num != 0:
            self.product *= num
            self.data.append(self.product)
        else:
            self.data = []
            self.product = 1

    def getProduct(self, k: int) -> int:
        if len(self.data) < k:
            return 0
        if len(self.data) == k:
            return self.data[-1]
        else:
            return int(self.data[-1] / self.data[-1-k])

'''
■■■■■■■■■ TEST ■■■■■■■■■
1,2,3,4,5

prefix_mul = 120
integer_stream = [1,2,3,4,5]
                  



'''
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)