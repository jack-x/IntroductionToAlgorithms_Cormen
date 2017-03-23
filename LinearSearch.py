#LinearSearch Python


def main():
	arr = input().split()
	v = input()
	flag=0
	for x in arr:
		if x==v:
			print("Value Found")
			print("Index:{}".format(arr.index(x)))
			print("arr[{}] = {}".format(arr.index(x),x))
			flag=1
			break
	if flag==0:
		print("Value does not exist.Exiting...")
			

if __name__ == "__main__": main()
