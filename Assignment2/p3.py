from dataclasses import dataclass


# Automatically cretes dunder functions such as init and eq
# for the class
@dataclass
class Card:
    name: str
    cost: int
    type : str
    color: str
    rarity: int

    def show_rarity(self):
        if self.rarity <10:
            print(self.name, "is a common card")
        if self.rarity < 25:
            print(self.name, "is an uncommon card")
        else:
            print(self.name, "is a rare card")


def main():
    mycard1 = Card("Thundering tempest", 5, "creature", "black", 28)
    mycard1.show_rarity()

    mycard2 = Card("Thundering tempest1", 5, "creature", "black", 28)

    print(mycard2)

    if mycard1 == mycard2:
        print('These are the same card')
    else:
        print('These cards are different')




main()