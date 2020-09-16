from redeal import *
from redeal import dds
from redeal.global_defs import Seat, Suit, Card, Rank, Strain

print(Seat())

Deal.set_str_style("short")
Hand.set_str_style("short")
vuln = False
predeal = {Seat["E"]: H("752 Q JT9 A65432")}
dealer = Deal.prepare(predeal)


def accept(deal):
    if deal.north.hcp < 12 and deal.south.hcp < 12:
        if deal.west.hcp > 11 and deal.west.hcp < 23:
            if len(deal.west.diamonds) > 3:
                return True


imps = Payoff(("pass", "3NT", "3D", "5D", "6D", "5C", "1NT"), imps)
found = 0
n = 1000
for _ in range(1000 * n):
    if found > n:
        break
    deal = dealer()
    if not accept(deal):
        continue
    found += 1
    score_1d = deal.dd_score("1DW", vuln)
    score_3d = deal.dd_score("3DW", vuln)
    score_3n = deal.dd_score("3NW", vuln)
    score_5d = deal.dd_score("5DW", vuln)
    score_6d = deal.dd_score("6DW", vuln)
    score_5c = deal.dd_score("5CE", vuln)
    score_1n = deal.dd_score("1NE", vuln)

    data = {
        "pass": score_1d,
        "3NT": score_3n,
        "3D": score_3d,
        "5C": score_5c,
        "5D": score_5d,
        "6D": score_6d,
        "1NT": score_1n,
    }
    imps.add_data(data)

imps.report()
