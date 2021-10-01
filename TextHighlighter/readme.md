In a notepad, when a continuous part of text is selected, the selection is highlighted with a colored block (light blue). Each word is colored separately. For example:<br>

There is a list of 26 character heights aligned backwards by index to their letters. For example, 'a' is at index 25 and 'z' is at index 0. There will also be a string. Using the letter heights given, determine the area of the rectangle highlighted in mm2 assuming all letters are 1mm wide.<br><br>
Example<br>
 h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 1, 1, 5, 5, 1, 5, 2, 5, 5, 5, 5, 5, 5]<br>
Word = ‘torn’<br>
The heights are t = 1, o = 5, r = 2 and n=5. The tallest letter(s) is 5 high and there are 4 letters. The highlighted area will be 5*4 = 20mm2 so the answer is 20.<br>
 
Input Format<br><br>
The first line contains 26 space-separated integers describing the respective heights of each consecutive lowercase English letter, ascii[a-z].<br>
The second line contains a single word consisting of lowercase English alphabetic letters.<br><br>
 
Constraints<br>
·        Consider only English lowercase letters.<br>
·         contains no more than 10 letters.
