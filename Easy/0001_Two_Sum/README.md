# 1. Two Sum

## Problem

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

## Example

Input:

```text
nums = [2,7,11,15]
target = 9
```

Output:

```text
[0,1]
```

## Approach

- Create an empty HashMap (dictionary).
- Traverse the array once.
- Calculate the required value:
  `need = target - current`
- If `need` exists in the HashMap, return both indices.
- Otherwise, store the current number and its index.

## Time Complexity

```
O(n)
```

## Space Complexity

```
O(n)
```

## Language

Python