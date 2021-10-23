s = "PPALLP"


def absent(a):
    consecutive_late_count = 0
    absent_count = 0
    for i in range(len(s)):
        if s[i] == "L":
            consecutive_late_count += 1
            if consecutive_late_count == 3:
                return False
        elif s[i] == "A":
            consecutive_late_count = 0
            absent_count += 1
            if absent_count == 2:
                return False
        elif s[i] == "P":
            consecutive_late_count = 0
            continue

    return True
