# My solution for leetcode question 8, straight forward solution
# remove beginning/ending spaces with strip, then check for any +/- signs
# lastly convert the number and check if the number is within range

class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip(" ")
        result = 0

        if str == "" or str == "-" or str == "+": return 0
        if str[0] != "-" and str[0] != "+" and not str[0].isdigit ():
            return 0
        if len(str) >= 2:
            if (str[0] == "-" or str[0] == "+") and not str[1].isdigit:
                return 0

        negative = False if str[0] != "-" else True
        positive_sign = True if str[0] == "+" else False

        i = 1 if (negative or positive_sign) else 0

        while(i < len(str)):
            if(str[i].isdigit()):
                result = result * 10 + int(str[i])  # can also use ascii conversion here
            else:
                break
            i += 1
        
        result = -result if negative else result

        if result < pow(-2, 31): result = pow(-2, 31)
        if result > pow(2, 31) - 1: result = pow(2, 31) - 1

        return result


        