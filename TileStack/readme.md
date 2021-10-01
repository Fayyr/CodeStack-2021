There are N tile stacks, with xi tiles in the ith stack. The following is a game Kaustubh and Anuj play:<br>
1. Kaustubh takes the first turn, and they exchange turns.
2. In a turn, a player can choose any one of the Stacks of tiles and divide the tiles in it into any number of unequal Stacks such that no two of the newly created Stacks have the same number of tiles. For example, if there 10 tiles in a stack, it can be divided into one of these set of Stacks: (1,9), (2,8), (3,7), (4,6), (1,2,7), (1,3,6), (1,4,5), or (2,3,5).
3. The game is lost by the player who is unable to make a move (due to the indivisible nature of the remaining Stacks).
<br>
Given the starting set of Stacks, who wins the game assuming both players play optimally (that means they will not make a move that causes them to lose the game if some better, winning move exists)?<br><br>
Input Format<br><br>
The first line contains the number of test cases T. T test cases follow. The first line for each test case contains N, the number of Stacks initially. The next line contains N space delimited numbers, the number of tiles in each of the Stacks.<br><br>
Constraints<br><br>
·         1<= T <= 50<br>
·         1<= N <= 50<br>
·         1<= xi <= 50<br><br>
Output Format<br><br>
Output T lines, one corresponding to each test case containing KAUSTUBH if Kaustubh wins the game and ANUJ otherwise.
