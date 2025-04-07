# Jump Problem

## Description

The Jump Problem involves determining whether it is possible to reach the last index of a list, starting from the first index. Each element in the list represents the maximum jump length that can be made from that position.

### Input

- A list of non-negative integers, `nums`, where each element represents the maximum jump length from that position.

### Output

- A boolean value: `True` if it is possible to reach the last index, and `False` otherwise.

## Input/Output Examples

### Example 1:
```python
Input:  [2, 3, 1, 1, 4]
Output: True
```
### Example 2:
```python
Input:  [3, 2, 1, 0, 4]
Output: False
```
### Other examples:
```python
[0, 1, 2, 3]       -> False
[0]                -> True
[1, 0, 0]          -> False
[2, 0, 0]          -> True
[1, 2, 3, 4, 5]    -> True
```

## How to run the script

Clone the project from GitHub to your local machine:
```bash
git clone https://github.com/lolochek/test_task
```

And then move to the project directory:
```bash
cd test_task
```

Then execute:
```bash
python solution.py
```

You will be prompted to enter a list of numbers:
```bash
You will be prompted to enter a list of numbers (e. g. 2 3 1 1 4):
```

### After entering a list of numbers, you will get the result. Happy jumping!
