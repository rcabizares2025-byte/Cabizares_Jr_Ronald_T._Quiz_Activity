class MagicCard:
    DEFAULT_SET= "Core Set"
    def __init__(self, card_name, mana_cost, power=1):
        self.card_name = card_name
        self.mana_cost = mana_cost
        self.power = power
                
Thornscape_Battlemage = MagicCard ("Thornscape Battlemage", 1)
Winter_Misanthropic_Guide = MagicCard ("Winter, Misanthropic Guide", 2)

Thornscape_Battlemage.power = 0

print("Card Name:", Thornscape_Battlemage.card_name)
print("Mana Cost:", Thornscape_Battlemage.mana_cost)
print("Set:", MagicCard.DEFAULT_SET)
print("Power:", Thornscape_Battlemage.power)

print()
print()

print("Card Name:", Winter_Misanthropic_Guide.card_name)
print("Mana Cost:", Winter_Misanthropic_Guide.mana_cost)
print("Set:", MagicCard.DEFAULT_SET)
print("Power:", Winter_Misanthropic_Guide.power)