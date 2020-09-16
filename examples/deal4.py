"""
Deal's example 4:

By agreement, you open a weak 2 with exactly 6 cards in your major, fewer than
4 cards in the other major, 5-10 HCP and either 2 of the top 3 or three of the
top 5 in your suit.
"""

from redeal import *

w2q = Evaluator(2, 2, 1, 1, 1)


def accept(deal):
    s = deal.south
    return (
        5 <= s.hcp <= 10
        and len(s.clubs) <= 3
        and len(s.diamonds) <= 3
        and (
            len(s.spades) == 6
            and len(s.hearts) <= 3
            and w2q(s.spades) > 3
            or len(s.hearts) == 6
            and len(s.spades) <= 3
            and w2q(s.hearts) > 3
        )
    )
