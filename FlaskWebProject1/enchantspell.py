import enchant
from enchant.checker import SpellChecker
def spellenchant(user):
    d = enchant.Dict("en_US")
    chkr = SpellChecker("en_US")
    chkr.set_text(user)
    for err in chkr:
	    abc = []
	    abc.append(err.word)
	    print(abc)
	    z=d.suggest(abc[0])
	    print(z)
    return z