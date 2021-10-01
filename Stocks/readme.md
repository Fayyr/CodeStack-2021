Stocks to the moon:<br><br>

You are given an integer array of prices where prices[i] is the price of a given stock on the ith day.<br>

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.<br>

Find and return the maximum profit you can achieve.<br>

Input Format: The first line contains number of days , second line contains an array of prices .<br>
Output Format : Output 0 if there is no way to make profit, otherwise maximum profit that you can achieve by buying or selling.<br>


Example 1:<br><br>

Input: <br>
6<br>
7 1 5 3 6 4<br><br>
Output: 7<br>
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.<br><br>
Example 2:

Input: 
5<br>
1 2 3 4 5<br><br>
Output: 4<br>
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices =  <br>
5<br>
7 6 4 3 1<br>
Output: 0<br>
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 <br><br>

Constraints:
<br>
1 <= prices.length <= 3 * 104<br>
0 <= prices[i] <= 104

