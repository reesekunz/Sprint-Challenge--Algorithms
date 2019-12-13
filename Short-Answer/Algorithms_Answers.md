#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - Linear because for each increase in input size (n), the number of operations will increase at the same rate.


b) O(n^c) - Polynomial because the outer loop runs at O(n) while the inner loop runs at O(n-1). O(n) * O(n-1) = O(n^2-1) which we can simplify when determining runtimes to O(n^2).


c) O(1) - Constant because increasing the input size (n) wouldn't affect the runtime of this function.

## Exercise II


<!-- Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution. -->

building floors
|            egg breaks
|
|---------- floor (f) cut off point
|
|           egg doesnt break
|

n = number of stories
f = story floor

Starting at floor 1, drop an egg
If egg breaks, stop.
Else go up one more floor.
Once egg breaks, the range of acceptable floors to drop your egg from will be the min floor story to the broken egg floor story -1.

Rumtime complexity = O(n) 

    
