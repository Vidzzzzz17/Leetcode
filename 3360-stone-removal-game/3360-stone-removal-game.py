class Solution:
    def canAliceWin(self, n: int) -> bool:
        need = 10
        alice_turn = True
        while need > 0 and n >= need:
            n -= need
            need -= 1
            alice_turn = not alice_turn
        # The player whose turn it is cannot move and loses
        return not alice_turn