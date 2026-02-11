# AI Code Review Assignment (Python)

## Candidate
- Name: Mehmet Baran Korkusuz
- Approximate time spent: ~60 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- The function skips cancelled orders when summing but still divides by the total number of orders. So the average comes out wrong — it's potentially lower than it should be.
- If you pass an empty list, you get a ZeroDivisionError because `count` is 0 and there's no check for that.

### Edge cases & risks
- All orders being cancelled case is not considered in `task1.py`. This case would output 0 as average but needs clarification actually.
- If an order dict misses the "status" or "amount" key, we would get a KeyError.

### Code quality / design issues
- Using `len(orders)` for count is misleading here because we're filtering some orders out. The count should only reflect what we actually summed up.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Changed `count` from `len(orders)` to a manual counter that only increments for non-cancelled orders.
- Added a check: if count is 0, return 0 instead of dividing by zero.
- Added checks for the existence of `status` and `amount` keys in an order dictionary to prevent `KeyError`.

### Corrected code
See `correct_task1.py`

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

- Normal case with a mix of cancelled and non-cancelled orders — make sure the math is right.
- Empty list — should return 0, not crash.
- All cancelled orders — should also return 0.
- Single order — basic sanity check.
- Orders with zero amount — make sure it doesn't break anything.


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- It says "correctly excludes cancelled orders" but that's not true. It only excludes them from the sum, not from the count. The division still uses the total number of orders, so the average is wrong.
- The explanation makes it sound like everything works fine, which is misleading.

### Rewritten explanation
- This function tries to calculate the average order value by skipping cancelled orders during summation. However, it divides by the total order count instead of only the non-cancelled count, so the result is incorrect. It also crashes on empty input.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The core logic has a clear bug — the count doesn't match what's being summed. It will give wrong results for any list that has cancelled orders in it.
- Confidence & unknowns: Pretty confident about this one. The bug is straightforward.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- The only validation is checking if "@" exists in the string. That means stuff like `"@"`, `"@@@@"`, `"hello@"`, `"@domain"` all pass as "valid" emails, which they obviously aren't.

### Edge cases & risks
- If the list contains non-string values (like None, integers, etc.), calling `"@" in email` would either return wrong results or raise a TypeError.
- Also if email element type is list and contains `"@"` it would assume the email element as a valid email address, but of course this is not the case.
- Empty string passes because `"@" in ""` is False, so that's actually fine. But `"@"` alone would pass, which is bad.

### Code quality / design issues
- The validation is way too simple. At minimum you'd want to check that there's something before and after the @, and that the domain part has a dot.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Added a type check — skip anything that's not a string.
- Split by "@" and make sure there are exactly 2 parts (so no multiple @ signs).
- Check that both the local part and domain part are non-empty, and that the domain has a dot in it.

### Corrected code
See `correct_task2.py`


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

- Obviously valid emails like `"user@example.com"` — should count.
- Clearly invalid stuff like `"@"`, `""`, `"domain@"`, `"@domain"` — should not count.
- Multiple @ signs like `"a@b@c.com"` — should not count.
- Non-string inputs mixed in — should be skipped without crashing.
- Empty list — should return 0.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- It says "valid email addresses" but the validation is basically nonexistent — just checking for "@" is not real validation.
- "Safely ignores invalid entries" is wrong too — it doesn't handle non-string types at all, so it could crash.

### Rewritten explanation
- This function attempts to count valid emails but only checks for the presence of "@", which is not enough. Many invalid strings would be counted as valid. It also doesn't handle non-string inputs, which could cause errors.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The email validation is too weak to be useful. Anything with an @ in it gets counted. Needs proper checks.
- Confidence & unknowns: High confidence. The fix is simple — just need better string checks. I didn't go too complex validations like here: https://emailregex.com/ because that's overkill for this context, but basic structural checks are a must.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- Same issue as Task 1: it filters out None values from the sum but uses `len(values)` for the count. So the average is divided by the wrong number.
- Empty list causes ZeroDivisionError.
- If a value can't be converted to float (like a random string), `float(v)` will throw a ValueError.

### Edge cases & risks
- If all values are None, count is still `len(values)` (non-zero) but total is 0, so you'd get 0.0 instead of an error or a meaningful "no data" response.


### Code quality / design issues
- The count logic is wrong for the same reason as task1. If you're filtering data, your denominator should reflect the filtered count, not the original.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Changed count to a manual counter, only incrementing when we actually add a value to the total.
- Added try/except around the float conversion to handle values that can't be converted.
- Added a zero-count check to avoid division by zero.

### Corrected code
See `correct_task3.py`

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

- Normal list of numbers — basic check.
- List with some None values — make sure average is calculated from non-None values only.
- All None values — should return 0.
- Empty list — should return 0.
- Mixed types including strings that can't convert to float — should skip them gracefully.
- Strings that CAN convert to float like `"2.5"` — should work fine.


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- "Averaging the remaining values" is not accurate — it divides by the total count, not the count of valid values. So the average is wrong when there are None values.
- "Safely handles mixed input types" is false — passing a non-numeric string would crash the function with a ValueError.

### Rewritten explanation
- This function tries to average non-None measurements but has a bug: it divides by the total number of elements instead of only the valid ones. It also doesn't handle values that can't be converted to float, so it can crash on non-valid input.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The count bug gives wrong averages whenever there are None values in the list. Plus the lack of error handling for non-numeric values is a problem.
- Confidence & unknowns: Very confident. It's essentially the same bug pattern as Task 1.
