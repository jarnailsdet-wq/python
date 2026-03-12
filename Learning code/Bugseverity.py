#Bug severity level
bugseverity=int(input("Enter the bug severity level from 1 to 5 : "))
if bugseverity<=1:
    print("Critical Bug: Fix immediately")
else:
    print("Normal Bug: Add to Backlog")
