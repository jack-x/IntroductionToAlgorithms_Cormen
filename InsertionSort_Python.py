#Insertion Sort Algorithm Python

#Logic implemented for Cormen book
def InsertionSort_WhileLoop(arr = [0]):
	j=0
	while j< len(arr):
		key = arr[j]
		i = j - 1
		while (i>=0 and arr[i] > key):
			arr[i+1] = arr[i]
			i-=1
		arr[i+1]= key
		j+=1
	
	return arr

def InsertionSort_ForLoop(arr =[0]):
	for x in range(0,len(arr)):
		key = arr[x]
		y = x -1
		A=y
		for z in range(y,-1,-1):
			if(arr[z]<key):
				break
			arr[z+1] = arr[z]
			A=z
		arr[A+1] = key
		
	return arr

def main():
	numbers = input()
	arr = []
	for x in numbers.split():
		arr.append(int(x))
	arr2 = arr
	print("Original Array")
	print(arr)
	arr = InsertionSort_WhileLoop(arr)
	print("\nSorted Array")
	print(arr)
	print("\nSorted Array using for loop")
	print(InsertionSort_ForLoop(arr2))

if __name__ == "__main__" : main()
