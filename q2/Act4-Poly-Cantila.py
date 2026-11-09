class HealthPotion:
    def use(self):
        print("You regain 50 HP!")

class ManaPotion:
    def use(self):
        print("You restore 30 MP!")

class SpeedBoost:
    def use(self):
        print("Your speed increases for 10 seconds!")

def apply_item(item):
    item.use()

hp_potion = HealthPotion()
mp_potion = ManaPotion()
speed_item = SpeedBoost()

potions = [hp_potion, mp_potion, speed_item]

for item in potions:
    apply_item(item)