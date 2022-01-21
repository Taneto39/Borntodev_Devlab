"""รูปแบบการเข้ารหัสเป็นดังนี้

text -> binary(ASCII) -> pupe code



ตัวอย่างการเข้ารหัส

A = pupepupupupupupe //(A = 01000001 = pupepupupupupupe)

Ab = pupepupupupupupepupepepupupupepu //(Ab =0100000101100010 = pupepupupupupupepupepepupupupepu)

"""

x = input()
binary_txt = x.replace("p", "").replace("u", "0").replace("e", "1")
binary_txt = [binary_txt[i:i+8] for i in range(0, len(binary_txt), 8)]
encrypt_txt = []
for i in binary_txt:
    decrypt = 0
    y = 0
    for j in reversed(i):
        if j == "1":
            decrypt += 2 ** y
        y += 1
    encrypt_txt.append(decrypt)
for i in encrypt_txt:
    print(chr(i), end="")
