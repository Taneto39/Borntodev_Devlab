type_1 = [
    ["underwear - 20", 20],
    ["pants - 30", 30],
    ["skirt - 30", 30],
    ["shirt - 40", 40],
    ["blouse - 40", 40]
]
size = [
    ["size S - 5", 5],
    ["size M - 10", 10],
    ["size L - 15", 15],
    ["size Xl - 20", 20],
    ["size XXL - 25", 25]
]
color = {
    "R":["color red - 15", 15],
    "B":["color blue - 15", 15],
    "W":["color white - 10", 10],
    "G":["color green - 15", 15],
    "BK":["color black - 15", 15],
}
type_2 = [
    ["cotton - 20", 20],
    ["nylon - 15", 15],
    ["spandex - 25", 25],
    ["wool - 30", 30],
    ["linen - 25", 25],
]
result = 0

a = int(input())
print(type_1[a-1][0])
result += type_1[a-1][1]

a = int(input())
print(size[a-1][0])
result += size[a-1][1]

a = input()
print(color[a][0])
result += color[a][1]

b = int(input())
print(type_2[b-1][0])
result += type_2[b-1][1]

b = int(input())
print("amount -", b)

print("cost - {}*{} =".format(result, b), result * b)
