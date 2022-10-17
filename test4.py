x = int(input())
# cur_total = [i for i in range(x)]
cur_sentence = []
lis_sentences = []
for i in range(x):
    lis_sentences.append(input().split(' '))
for pri_sentence in lis_sentences:  # find initial sentence
    sec_sentences = [st for st in lis_sentences if st != pri_sentence]
    for idx, sec in enumerate(sec_sentences):
        for word in range(1, len(pri_sentence)+1):
            if pri_sentence[:word] == sec[-word:]:
                break
        else:
            continue
        break
    else:
        print(pri_sentence)
        break

"""for pri_index in range(x):
    pri_sentence = globals()[f'txt{pri_index}']
    nd_list = cur_total.copy()
    nd_list.remove(pri_index)
    for nd_index in nd_list:
        for word in range(1, len(pri_sentence) + 1):
            if pri_sentence[-word:] == globals()[f'txt{nd_index}'][:word]:
                print(pri_sentence, end='')
                print(globals()[f'txt{nd_index}'][word:])
                break
        else:
            continue
        break"""

