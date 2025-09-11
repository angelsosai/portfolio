# At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

# Note that you do not have any change in hand at first.

# Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        contador5=0
        contador10=0
        for i in bills:
            if i==5:
                contador5+=1
            elif i==10:
                if 1>contador5:
                    return False
                else:
                    contador5-=1
                    contador10+=1
            else:
                if contador10>0 and contador5>0:
                    contador10-=1
                    contador5-=1
                else:
                    if 3<=contador5:
                        contador5-=3
                    else:
                        return False

            # print(contador5,contador10,i)
            
        return True
                    
