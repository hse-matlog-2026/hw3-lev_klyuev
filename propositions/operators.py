# This file is part of the materials accompanying the book
# "Mathematical Logic through Python" by Gonczarowski and Nisan,
# Cambridge University Press. Book site: www.LogicThruPython.org
# (c) Yannai A. Gonczarowski and Noam Nisan, 2017-2022
# File name: propositions/operators.py

"""Syntactic conversion of propositional formulas to use only specific sets of
operators."""

from propositions.syntax import *
from propositions.semantics import *

def to_not_and_or(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'~'``, ``'&'``, and ``'|'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'~'``, ``'&'``, and
        ``'|'``.
    """
    # Task 3.5
    return formula.substitute_operators({
        "T": Formula.parse('(p|~p)'),
        'F': Formula.parse('(p&~p)'),
        '->': Formula.parse('(~p|q)'),
        '+': Formula.parse('((p&~q)|(~p&q))'),
        '<->': Formula.parse('((p&q)|(~p&~q))'),
        '-|': Formula.parse('~(p|q)'),
        '-&': Formula.parse('~(p&q)')
    })


def to_not_and(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'~'`` and ``'&'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'~'`` and ``'&'``.
    """
    # Task 3.6a
    f = to_not_and_or(formula)
    return f.substitute_operators({"|": Formula.parse("~(~p&~q)")})


def to_nand(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'-&'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'-&'``.
    """
    # Task 3.6b
    f = to_not_and(formula)
    p = Formula.parse('p')
    q = Formula.parse('q')
    p_nand_q = Formula('-&', p, q)
    return f.substitute_operators({
        '~': Formula('-&', p, p),
        '&': Formula('-&', p_nand_q, p_nand_q)
    })


def to_implies_not(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'->'`` and ``'~'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'->'`` and ``'~'``.
    """
    # Task 3.6c
    f = to_not_and_or(formula)
    p = Formula.parse('p')
    q = Formula.parse('q')
    return f.substitute_operators({
        'T': Formula('->', p, p),
        'F': Formula('~', Formula('->', p, p)),
        '~': Formula('~', p),
        '&': Formula('~', Formula('->', p, Formula('~', q))),
        '|': Formula('->', Formula('~', p), q)
    })


def to_implies_false(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'->'`` and ``'F'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'->'`` and ``'F'``.
    """
    # Task 3.6d
    f = to_not_and_or(formula)
    p = Formula.parse('p')
    q = Formula.parse('q')
    return f.substitute_operators({
        '~': Formula('->', p,  Formula.parse('F')),
        '&': Formula('->', Formula('->', p, Formula('->', q, Formula.parse('F'))), Formula.parse('F')),
        '|': Formula('->', Formula('->', p,  Formula.parse('F')), q),
        'T': Formula('->', Formula.parse('F'), Formula.parse('F')),
        'F':  Formula.parse('F')
    })
