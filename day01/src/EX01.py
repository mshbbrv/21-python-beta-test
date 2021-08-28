from EX00 import add_ingot


def split_booty(*purses):
    gold_sum = 0
    for purse in purses:
        gold_sum += purse.get("gold_ingots", 0)
    purse_1 = {}
    purse_1.setdefault("gold_ingots", 0)
    while purse_1.get("gold_ingots") < round(gold_sum / 3):
        purse_1 = add_ingot(purse_1)
    purse_2 = {}
    purse_2.setdefault("gold_ingots", 0)
    while purse_2.get("gold_ingots") < round(gold_sum / 3):
        purse_2 = add_ingot(purse_2)
    purse_3 = {}
    purse_3.setdefault("gold_ingots", 0)
    while purse_3.get("gold_ingots") < gold_sum - round(gold_sum / 3) * 2:
        purse_3 = add_ingot(purse_3)
    return purse_1, purse_2, purse_3

