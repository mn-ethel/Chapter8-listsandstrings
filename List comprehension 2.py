L=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
gaps=[L[i+1]-L[i] for i in range (len(L)-1)]# gaps between consecutive numbers
max_gaps=max(gaps)# to find the maximum gap numbers
gap_size_2=sum(1 for gap in gaps if gaps==2)
percentage=(gap_size_2/len(gaps)) * 100
print("Gaps:", gaps)
print("Maximum gap size:", max_gaps)
print("Percentage of gaps with size 2:", percentage)

