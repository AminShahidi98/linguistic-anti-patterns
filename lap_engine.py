"""
Runs the detectors and the fixers of this project on one piece of Java code.

Core.py does the same job from the command line: it asks a question on the
keyboard and edits Demo.java in place. This module asks nothing, works on a
temporary copy, and returns what it found and the fixed code. The web page
(app.py) calls run().
"""
import copy
import os
import tempfile

import javalang

from Utils import findMethodDeclarations, returnGetMethodSmell, returnIsMethodSmell, returnSetMethodSmell
from Detectors import returnGetLAPType, returnIsLAPType, returnSetLAPType
from Actuators import (createMethodComplement, createMethodComplementName, insertMethodToTheEnd,
                       createAndReplaceEditedFunction, renameMethodInPlace, removeMethodInPlace,
                       resolveSetMethodeNameAndReturns)
from Models import Lap, GetMethodLAP, IsMethodLAP, SetMethodLAP, NotImplementedLAP

LAP_NAMES = {
    1: '"Get" more than an accessor',
    7: 'Get method does not return',
    2: 'Is returns more than a boolean',
    3: 'Set method returns',
    5: 'Not implemented method',
}

# The same order Core.py fixes them in.
FIX_ORDER = [1, 7, 5, 2, 3]


def read_file(path):
    with open(path) as file:
        return file.read()


def detect(path):
    """Return {LAP type number: [LAP objects]} for the code in path."""
    found = {t: [] for t in FIX_ORDER}
    for m in findMethodDeclarations(path):
        if returnGetMethodSmell(m) == 'getMethod':
            t = returnGetLAPType(m).value
            if t in (1, 5, 7):
                found[t].append(GetMethodLAP(m, Lap(t), LAP_NAMES[t], 1))
        elif returnIsMethodSmell(m) == 'isMethod':
            t = returnIsLAPType(m).value
            # Type 8 (an "is" method with no return) is detected but has no fix yet.
            if t in (2, 5):
                found[t].append(IsMethodLAP(m, Lap(t), LAP_NAMES[t], 1))
        elif returnSetMethodSmell(m) == 'setMethod':
            t = returnSetLAPType(m).value
            if t in (3, 5):
                found[t].append(SetMethodLAP(m, Lap(t), LAP_NAMES[t], 1))

        # Any other method with an empty body. Core.py stores these as plain
        # tuples, which removeMethodInPlace cannot use; here they are LAP objects.
        if m.body == [] and not any(lap.node is m for lap in found[5]):
            found[5].append(NotImplementedLAP(m, Lap(5), LAP_NAMES[5]))
    return found


def fix(path, lap, t):
    """Fix one LAP in the file, the same way Core.py does."""
    if t in (1, 2):
        methods = findMethodDeclarations(path)
        lines = createMethodComplement(path, lap.node)
        old_lines = copy.copy(lines)
        first_line, call = createMethodComplementName(lines[0], lap, methods, False)
        lines[0] = first_line
        insertMethodToTheEnd(path, lines)
        createAndReplaceEditedFunction(path, old_lines[0], call, lap.node, old_lines, t == 2)
    elif t == 7:
        renameMethodInPlace(path, lap, False)
    elif t == 5:
        removeMethodInPlace(path, lap)
    elif t == 3:
        lines = createMethodComplement(path, lap.node)
        resolveSetMethodeNameAndReturns(path, lap.node, lines)


def describe_fix(lap, t):
    name = lap.node.name
    line = lap.node.position.line
    if t == 1:
        return f'{name} (line {line}): its work moved to complement_{name}; {name} now only returns that result.'
    if t == 2:
        return f'{name} (line {line}): now returns a boolean; its old body moved to complement_{name}.'
    if t == 7:
        return f'{name} (line {line}): renamed to calculateFor{name}, because it returns nothing.'
    if t == 5:
        return f'{name} (line {line}): removed, because its body is empty.'
    return f'{name} (line {line}): renamed to {name}_WithLog; it now stores its message in logFor_{name} instead of returning it.'


def run(source_code, remove_empty=False, max_steps=100):
    """
    Find and fix the linguistic anti-patterns in source_code.

    Returns a dict with:
      found       list of (type, method name, line) seen in the original code
      steps       one sentence per fix, in the order they were made
      fixed_code  the code after all fixes (or as far as it got)
      error       None, or a sentence saying why it stopped early
    """
    source_code = source_code.replace('\r\n', '\n')
    types = [t for t in FIX_ORDER if remove_empty or t != 5]
    result = {'found': [], 'steps': [], 'fixed_code': source_code, 'error': None}

    with tempfile.TemporaryDirectory() as folder:
        path = os.path.join(folder, 'Source.java')
        with open(path, 'w') as file:
            file.write(source_code)
        try:
            first = detect(path)
            result['found'] = [(t, lap.node.name, lap.node.position.line) for t in types for lap in first[t]]

            # Fix one LAP, then look again, until none is left (like Core.py).
            for _ in range(max_steps):
                laps = detect(path)
                todo = [(t, laps[t][0]) for t in types if laps[t]]
                if not todo:
                    break
                t, lap = todo[0]
                before = read_file(path)
                fix(path, lap, t)
                if read_file(path) == before:
                    result['error'] = f'Could not fix {lap.node.name} (line {lap.node.position.line}), so it stopped there.'
                    break
                result['steps'].append(describe_fix(lap, t))
            else:
                result['error'] = f'Stopped after {max_steps} fixes, because the problems kept coming back.'
        except (javalang.parser.JavaSyntaxError, javalang.tokenizer.LexerError):
            if not result['steps']:
                result['error'] = ('This is not valid Java, or it uses syntax newer than Java 8 '
                                   '(for example var, records or switch expressions), which the parser does not read.')
            else:
                result['error'] = 'A fix produced code the parser could not read, so it stopped there.'
        except Exception as e:
            result['error'] = f'The tool hit an error and stopped: {type(e).__name__}: {e}'
        result['fixed_code'] = read_file(path)

    return result
