from equipment_slots import EquipmentSlots


class Equipment:
    def __init__(self, main_hand=None, body=None):
        self.main_hand = main_hand
        self.body = body

    @property
    def max_hp_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.max_hp_bonus

        if self.body and self.body.equippable:
            bonus += self.body.equippable.max_hp_bonus

        return bonus

    @property
    def power_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.power_bonus

        if self.body and self.body.equippable:
            bonus += self.body.equippable.power_bonus

        return bonus

    @property
    def defense_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.defense_bonus

        if self.body and self.body.equippable:
            bonus += self.body.equippable.defense_bonus

        return bonus

    def toggle_equip(self, equippable_entity):
        results = []

        slot = equippable_entity.equippable.slot

        if slot == EquipmentSlots.MAIN_HAND:
            if self.main_hand == equippable_entity:
                self.main_hand = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.main_hand:
                    results.append({'dequipped': self.main_hand})

                self.main_hand = equippable_entity
                results.append({'equipped': equippable_entity})
        elif slot == EquipmentSlots.BODY:
            if self.body == equippable_entity:
                self.body = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.body:
                    results.append({'dequipped': self.body})

                self.body = equippable_entity
                results.append({'equipped': equippable_entity})

        return results