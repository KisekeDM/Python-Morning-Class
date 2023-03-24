class computer:
    x = "Mouse"

    def mycomputer(self):
        print("8GB", "500GB")

device=computer()
v = type(device)
print(v)

y = device.x
print(y)

device.mycomputer()