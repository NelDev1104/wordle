This is a project to solve the game Wordle
===

This project is free to use.
<br> 
<br> 
### Requirements: 
Chrome Selenium Webdriver

### How it works
Our wordle solver select a random word from the 12.000 words list for wordle.
After selecting a random word, we then filter out the alphabet and words which is not included in that word.
We filter the correct alphabets, false alphabets and the included alphabets i.e

#### Given is a List of [salet, focus, diner] and the selected alphabet was T.

if the selected alphabet T is not included in that word, we would filter out salet else we filter out those 2 words since
they do not have a T in it.
<br>
We also filter out all the words if the alphabet T was in a correct spot. Which means every word in the word list
would be filtered out if the T was not in that correct spot.

#### Example
[salet, store, slate] -> if T was in the last spot, we would filter the 2 words store and slate.

#### Selecting the right word by filtering out
The process is repeated until there is only one word left. And most of the time it is the right word.