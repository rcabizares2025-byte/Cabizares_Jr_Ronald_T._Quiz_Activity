class MagicCard:
    DEFAULT_SET = "Core Set"
    def __init__(self, rarity, card_name, mana_cost, card_type, rules_text, artist, power=1):
        self.rarity = rarity
        self.card_name = card_name
        self.mana_cost = mana_cost
        self.card_type = card_type
        self.rules_text = rules_text
        self.artist = artist
        self.power = power

Thornscape_Battlemage = MagicCard("Uncommon", "Thornscape Battlemage", 3, "Creature — Elf Wizard", "Sacrifice Thornscape Battlemage: It deals 2 damage to target creature.\n , Sacrifice Thornscape Battlemage: Destroy target artifact.", "rk post", "2/2")
Winter_Misanthropic_Guide = MagicCard("Rare", "Winter Misanthropic Guide", 4, "Legendary Creature — Human Warlock", "During your turn, creatures you control have menace.\nWhenever one or more creatures you control deal combat damage to a player, draw a card.", "David Palumbo", "3/4")

Thornscape_Battlemage.power = 0

print("Set:", MagicCard.DEFAULT_SET)
print("Rarity:", Thornscape_Battlemage.rarity)
print("Card Name:", Thornscape_Battlemage.card_name)
print("Mana Cost:", Thornscape_Battlemage.mana_cost)
print("Power:", Thornscape_Battlemage.power)
print("Rules Text:", Thornscape_Battlemage.rules_text)
print("Artist:", Thornscape_Battlemage.artist)

print()
print()

print("Set:", MagicCard.DEFAULT_SET)
print("Rarity:", Winter_Misanthropic_Guide.rarity)
print("Card Name:", Winter_Misanthropic_Guide.card_name)
print("Mana Cost:", Winter_Misanthropic_Guide.mana_cost)
print("Power:", Winter_Misanthropic_Guide.power)
print("Rules Text:", Winter_Misanthropic_Guide.rules_text)
print("Artist:", Winter_Misanthropic_Guide.artist) 