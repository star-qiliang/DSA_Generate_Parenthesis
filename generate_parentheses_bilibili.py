class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def get_right_part(n, left, right):
            res_list = []

            if left<right:
                return res_list

            if left>n:
                return res_list

            if right>n:
                return res_list
            
            if left==n and right==n:
                return ['']
            
            elif left==n:
                tmp_list = get_right_part(n, left, right+1)
                tmp_list = [")"+x for x in tmp_list]
                res_list += tmp_list

            else: # left<n:
                tmp_list = get_right_part(n, left+1, right)
                tmp_list = ["("+x for x in tmp_list]
                res_list += tmp_list
                # print("tmp_list:", tmp_list)

                tmp_list = get_right_part(n, left, right+1)
                tmp_list = [")"+x for x in tmp_list]
                res_list += tmp_list
                # print("tmp_list:", tmp_list)

            return res_list

        res_list = get_right_part(n, 0, 0)
        return res_list