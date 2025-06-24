class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        
        beam_list = []
        result = 0
        for row in bank:
            count_beams = row.count("1")
            if count_beams > 0:
                beam_list.append(count_beams)
        
        
        for i in range(1, len(beam_list)):
            k = i - 1
            result+=(beam_list[k] * beam_list[i])
            
        return result
            
                
                
        
    
    

beam = Solution()
bank = ["011001","000000","010100","001000"]
bank = ["000","111","000"]
result = beam.numberOfBeams(bank)
print(result)