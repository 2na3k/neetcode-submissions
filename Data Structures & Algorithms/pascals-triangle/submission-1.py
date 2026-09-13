class Solution:
    @staticmethod
    def convolute_1d_stride_2(input_list: list):
        new_list = []
        for i in range(len(input_list)-1):
            new_list.append(input_list[i] + input_list[i+1])
        assert len(new_list) == len(input_list) - 1
        return new_list

    def generate(self, numRows: int) -> List[List[int]]:
        # i will do that myself, no need to fucking deal with that
        out = [[1], [1, 1]]
        
        if numRows == 1:
            return [[1]]

        elif numRows == 2:
            return [[1], [1, 1]]

        
        for i in range(2, numRows):
            # modify directly on the thing
            new_layer = [1] + self.convolute_1d_stride_2(out[-1]) + [1]
            out.append(new_layer)


        
        return out

    
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1] * (i + 1) for i in range(numRows)]

        for i in range(2, numRows):
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res