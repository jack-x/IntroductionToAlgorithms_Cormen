#Selection Sort

def main():
	a = input().split()
	arr =[]
	for x in a:
		arr.append(int(x))
	
	print("Original Array:{}".format( arr))
	SelectionSort(arr)
	print("Sorted Array:{}".format(arr))


def SelectionSort(arr2):
	for i in range(0,len(arr2)):
		smallestIndex = i
		
		#Searching for the ith Smallest element in the array
		for j in range(i,len(arr2)):
			if arr2[smallestIndex]> arr2[j] :
				smallestIndex=j
		
		#Replacing the ith smallest element with the element at the ith position
		temp=arr2[i]
		arr2[i]=arr2[smallestIndex]
		arr2[smallestIndex]=temp
	return arr2

	
if __name__ == "__main__": main()
