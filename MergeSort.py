#Merge Sort

def main():
	a = input().split()
	arr=[]
	for x in a:
		arr.append(int(x))
	
	print("Original:{}".format(arr))
	#MergeSortDebug(arr,0,len(arr))
	MergeSort(arr,0,len(arr))
	print("Sorted:{}".format(arr))

def MergeSort(arr,p,r):
		if p < (r-1):		#Comparing with (r-1) and not r, because r is the length, while (r-1) is the actual last index. We need to compare the indexes, not with the length, or the recursion stack never stops and keeps on going
			q = int((p+r)/2)
			
			MergeSort(arr,p,q)
			MergeSort(arr,q,r)
			
			#MergeDebug(arr,p,r)
			Merge(arr,p,r)
			
			
def Merge(arr,p,r):
		q = int((p+r)/2)
		
		L = arr[p:q]
		R = arr[q:r]
		
		#Both Li and Ri, representing the current index of Left array and Right array are 0, because these are two new arrays that will, quite obviously have starting index at 0. This is a minor mistake that got overlooked at the beginning
		Li=0
		Ri=0
		
		for x in range(p,r):
			if(Li==len(L)):
				for y in R[Ri:r]:
					arr[x] = y
					x+=1
				break
			
			if(Ri == len(R)):
				for y in L[Li:q]:
					arr[x] = y
					x+=1
				break
				
			if(L[Li] < R[Ri]):
				arr[x] = L[Li]
				Li+=1
			else:
				arr[x] = R[Ri]
				Ri+=1

#Merge function with input() breaks and print statements to elaborate on the function steps and Left and Right array contents while sorting
def MergeDebug(arr,p,r):
		q = int((p+r)/2)
		
		L = arr[p:q]
		
		R = arr[q:r]
		print("Left Array: {}".format(L))
		print("RightArray: {}".format(R))
		input()
		print()
		
		Li=0
		Ri=0
		
		for x in range(p,r):
			if(Li==len(L)):
				for y in R[Ri:r]:
					arr[x] = y
					x+=1
				break
			
			if(Ri == len(R)):
				for y in L[Li:q]:
					arr[x] = y
					x+=1
				break
				
			if(L[Li] < R[Ri]):
				arr[x] = L[Li]
				Li+=1
			else:
				arr[x] = R[Ri]
				Ri+=1


#MergeSort logic with input() pauses and print statements in the workflow to elaborate on the function calls for debugging
def MergeSortDebug(arr,p,r):
		if p < (r-1):
			q = int((p+r)/2)
			print("Function call 1")
			print("MergeSort({},{},{})".format("arr",p,q))
			input()
			MergeSortDebug(arr,p,q)
			
			print("Function call 2")
			print("MergeSort({},{},{})".format("arr",q,r))
			input()
			MergeSortDebug(arr,q,r)
			
			print("Function call 3")
			print("Merge({},{},{})".format("arr",p,r))
			input()
			MergeDebug(arr,p,r)
			#Merge(arr,p,r)
			print("arr after one full MergeSort run: {}".format(arr))
				
			
if __name__ == "__main__": main()
