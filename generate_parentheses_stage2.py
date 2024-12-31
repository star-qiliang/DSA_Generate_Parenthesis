
class Solution:

    def generateParenthesis(self, n: int) -> List[str]:

        def get_right_by_left(n, n_left, n_right):
            res_list = []
            if n_right>n_left:
                return res_list
            if n_right>n:
                return res_list
            if n_left>n:
                return res_list
            
            if n_left==n and n_right==n:
                res_list.append('')
                return res_list

            res = get_right_by_left(n, n_left, n_right+1)
            res = [")"+x for x in res]
            res_list += res

            res = get_right_by_left(n, n_left+1, n_right)
            res = ["("+x for x in res]
            res_list += res

            return res_list


        res_list = get_right_by_left(n,0,0)
        return res_list
