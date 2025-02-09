L=['January','February','March','April','May','On','July','August','September','Days']
without_first_letter=[s[1:] for s in L]
print(without_first_letter)
lengths=[len(item)for item in L]
print(lengths)
long_items=[s for s in L if len(s)>=3]
print(long_items)

