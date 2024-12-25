

class Solution:

    def generateParenthesis(self, n: int) -> List[str]:

        def generate_right_side(n, left_cnt, right_cnt):
            res_list = []
            if left_cnt<right_cnt:
                return res_list


            if n-left_cnt>0:
                tmp_list1 = generate_right_side(n, left_cnt+1, right_cnt)
                tmp_list1 = ["("+x for x in tmp_list1]
                res_list+=tmp_list1

                if n-right_cnt>0:
                    tmp_list2 = generate_right_side(n, left_cnt, right_cnt+1)
                    tmp_list2 = [")"+x for x in tmp_list2]
                    res_list+=tmp_list2

            elif n-right_cnt>0:
                tmp_list3 = generate_right_side(n, left_cnt, right_cnt+1)
                tmp_list3 = [")"+x for x in tmp_list3]
                res_list+=tmp_list3

            else:
                tmp_list4 = [""]
                res_list+=tmp_list4

            return res_list

        res_list = generate_right_side(n, 0, 0)
        return res_list
