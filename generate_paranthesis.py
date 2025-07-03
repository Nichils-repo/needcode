class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        result = []
        def fun(openpara, closedpara):
            if openpara == closedpara == n:
                result.append("".join(stack))
                return result

            if openpara < n:
                stack.append("(")
                fun(openpara + 1, closedpara)
                stack.pop()
            
            if closedpara < openpara :
                stack.append(')')
                fun(openpara, closedpara + 1)
                stack.pop()

        fun(0,0)
        return result
