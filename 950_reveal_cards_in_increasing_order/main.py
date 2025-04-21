class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        reveal_cards = []
     
        sorted_nums = sorted(deck)
        
        for i in reversed(sorted_nums):
            if reveal_cards:
                poped_card = reveal_cards.pop()
                reveal_cards.insert(0, poped_card)
            reveal_cards.insert(0, i)
                
        return reveal_cards

deck = [17,13,11,2,3,5,7]
s1 = Solution()
print(s1.deckRevealedIncreasing(deck))