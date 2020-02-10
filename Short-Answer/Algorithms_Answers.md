#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)
O(n) - the number of operations increases linearly with the input size (n) due to the While loop.

b)
O(n log(n)) - the outer loop is (n) and the nested loop is (log n) since j \*= 2 is processing chunks of elements at a time, making the entire algorithm O(n log(n))

c)
O(n) - Each time you make a recursive call has the runtime complexity of n. The base case is O(1) and the recursive case is O(n) since it makes one recursive call, which can all be simplified to O(n)

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

Binary Search Approach - runtime of O(log n)

1. Start at the floor that is in the middle of the building (n // 2)
2. Drop and egg
3. If egg doesnt break, move to the floor that is the halfway point between where you currently are and the max floor
4. If egg breaks, move to the floor that is the halfway point between the min floor and where you currently are
5. Repeat the process of cutting floors in half until you are at the highest floor where an egg can be dropped and not break. That floor is the value of 'f'.
