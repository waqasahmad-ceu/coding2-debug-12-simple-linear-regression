"""Display your Homework 1 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "233c52a35e29cfed9853893336108174"
GRADE_HASH = "0dbdf5f1684dd24ff538bc2587fcc9c2436505d083371c232109e3250329feea"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 1: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
