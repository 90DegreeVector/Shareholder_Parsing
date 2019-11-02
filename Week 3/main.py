
#print(fo.read())
#fo.close()
#print(fo.readlines())

def filter(phrase: str, line: str) -> None:
    if phrase in line:
        print(line)

with open("my_writeable.txt", 'rw') as w:
    w.write('Hello World!!\n')
    w.write('Hello Amazon!!\r\n')

#fo = open("tiny.txt")

# for line in fo.readlines():
#     filter("billion", line)
#     filter("Amazon", line)




# def recursive(ctr: int):
#     print(f"I am a counter {ctr}")
#
#     if ctr > 3:
#         return
#     recursive(ctr + 1)

#recursive(0)



