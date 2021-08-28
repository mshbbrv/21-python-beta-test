def add_ingot(purse):
    new_purse = {"gold_ingots": purse.get("gold_ingots", 0)}
    new_purse["gold_ingots"] += 1
    return new_purse


def get_ingot(purse):
    new_purse = {"gold_ingots": purse.get("gold_ingots", 0)}
    if new_purse["gold_ingots"] > 0:
        new_purse["gold_ingots"] -= 1
    return new_purse


def empty(purse):
    purse.clear()
    copy_purse = purse.copy()
    return copy_purse

