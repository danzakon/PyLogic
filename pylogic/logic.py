# -*- coding: utf-8 -*-

"""Basic fundamental constants."""

# connectives: strings to symbols
CONN = {"not":"!", "and":"&", "or":"|", "impl":"=>", "implr":"<=", "nand":"!&",
        "nor":"!|", "nimpl":"!=>", "nimplr":"!<=", "eq":"<=>", "neq":"!="}
# connectives: symbols to strings
CONN_ST = {'!': 'not', '&': 'and', '!<=': 'nimplr', '!=>': 'nimpl', '!=': 'neq',
           '<=': 'implr', '|': 'or', '!&': 'nand', '=>': 'impl', '<=>': 'eq',
           '!|': 'nor',
           # prover9 version
           # '&': 'and', '|': 'or',
           '<-': 'implr', '->': 'impl', '<->': 'eq'}

CONJ = ["and", "nor", "nimpl", "nimplr"]
DISJ = ["or", "impl", "implr", "nand"]

TOP = "T"
BOTTOM = "F"

DUAL = {"and":"or", "or":"and", "impl":"nimplr", "implr":"nimpl", "nand":"nor",
        "nor":"nand", "nimpl":"implr", "nimplr":"impl", "eq":"neq", "neq":"eq"}

QUANT = {'all':'∀', 'exists':'∃'}


re_LETTER = r'[A-Z]+'
re_VARIABLE = r'[abd-z][0-9]*'
re_CONSTANT = r'c[0-9]*'



# logics that use this constants
# import pylogic.propositional.propositional_logic
# import pylogic.first_order.first_order_logic
