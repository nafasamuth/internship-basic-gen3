class BigRandom:
    def __init__(self):
        self.data = open("data.txt", "r")
        # add attributes if you need more

    @property
    def answer(self):
        noh = 0 # variable to store number of hashtag
                # ommiting line number's hashtag
        suc = 0 # variable to store sum of character's code in ascii,
                # ommiting line number and its hashtag

        # your algorithm
        for each in b.data:
            c = each
            for x in c:
                c = c[1:]
                if (x == "#"):
                    break
            for x in c:
                if (x == "#"):
                    noh += 1
                suc += ord(x)
        return (noh,suc)


b = BigRandom()
print (b.answer)

    # add methods if you need more