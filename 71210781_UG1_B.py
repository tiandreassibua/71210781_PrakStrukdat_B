inputan = input("Input here : ")
if inputan == "Q":
    print("Program berhenti!")
else:
    inputan = inputan.split(" ")
    bil1 = int(inputan[0])
    bil2 = int(inputan[2])
    operasi = inputan[1]
    if operasi == "+":
        print(bil1 + bil2)
    elif operasi == "-":
        print(bil1 - bil2)
    elif operasi == "*":
        print(bil1 * bil2)
    if operasi == "/":
        print(bil1 / bil2)
