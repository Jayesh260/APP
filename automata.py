def accept(fa, bstr):
  print(f"{bstr}: {'Accepted' if fa.accepts_input(bstr) else 'Rejected'}") 
  
  
  # dfa: L(M)={w|wε{0,1}*} and w is a string that does not contain consecutive 0's
from automata.fa.dfa import DFA
dfa = DFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q1', '1': 'q0'},
        'q1': {'0': 'q2', '1': 'q0'},
        'q2': {'0': 'q2', '1': 'q2'}
    },
    initial_state='q0',
    final_states={'q0', 'q1'}
)
accept(dfa, '10101010')
accept(dfa, '100110')
accept(dfa, '10111101')
accept(dfa, '11111')



# dfa: ∑={w|wε{0,1}*} and w is a string with three consecutive 1's
from automata.fa.dfa import DFA
dfa = DFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q0', '1': 'q2'},
        'q2': {'0': 'q0', '1': 'q3'},
        'q3': {'0': 'q3', '1': 'q3'}
    },
    initial_state='q0',
    final_states={'q3'}
)
accept(dfa, '00111010')
accept(dfa, '10101011')
accept(dfa, '0101101')



# dfa: ∑={0,1} accepts even number of 0's and even number of 1's
from automata.fa.dfa import DFA
dfa = DFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q1', '1': 'q2'},
        'q1': {'0': 'q0', '1': 'q3'},
        'q2': {'0': 'q3', '1': 'q0'},
        'q3': {'0': 'q2', '1': 'q1'},
    },
    initial_state='q0',
    final_states={'q0'}
)
accept(dfa, '1010')
accept(dfa, '10101')
accept(dfa, '11001001')



# dfa: ∑={0,1} accepts only the input 101
from automata.fa.dfa import DFA
dfa = DFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q4', '1': 'q1'},
        'q1': {'0': 'q2', '1': 'q4'},
        'q2': {'0': 'q4', '1': 'q3'},
        'q3': {'0': 'q4', '1': 'q4'},
        'q4': {'0': 'q4', '1': 'q4'}
    },
    initial_state='q0',
    final_states={'q3'}
)
accept(dfa, '101')
accept(dfa, '0101')
accept(dfa, '1010')



# dfa: ∑={0,1} accepts accepts those string which starts with 1 and ends with 0
from automata.fa.dfa import DFA
dfa = DFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q3', '1': 'q1'},
        'q1': {'0': 'q2', '1': 'q1'},
        'q2': {'0': 'q2', '1': 'q1'},
        'q3': {'0': 'q3', '1': 'q3'},
    },
    initial_state='q0',
    final_states={'q2'}
)
accept(dfa, '10101011')
accept(dfa, '1000')
accept(dfa, '0101101')
accept(dfa, '100010')



# nfa: (a|b)*aab
from automata.fa.nfa import NFA
nfa = NFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': {'q0', 'q1'}, 'b': {'q0'}},
        'q1': {'a': {'q2'}},
        'q2': {'b': {'q3'}},
    },
    initial_state='q0',
    final_states={'q3'}
)
accept(nfa, 'aab')
accept(nfa, 'aaabab')
accept(nfa, 'baab')
accept(nfa, 'bbbbb')



# nfa: at least two consecutive 0's or 1's
from automata.fa.nfa import NFA
nfa = NFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': {'q0', 'q1'}, '1': {'q0', 'q3'}},
        'q1': {'0': {'q2'}},
        'q3': {'1': {'q4'}},
    },
    initial_state='q0',
    final_states={'q2', 'q4'}
)
accept(nfa, '010101')
accept(nfa, '1010100')
accept(nfa, '101011')



# nfa: either odd number of 0's, or number of 1's not a multiple of 3, or both
from automata.fa.nfa import NFA
nfa = NFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'': {'q1', 'q5'}},
        'q1': {'0': {'q1'}, '1': {'q2'}},
        'q2': {'0': {'q2'}, '1': {'q3'}},
        'q3': {'0': {'q3'}, '1': {'q4'}},
        'q4': {'0': {'q4'}, '1': {'q2'}},
        'q5': {'0': {'q6'}, '1': {'q5'}},
        'q6': {'0': {'q5'}, '1': {'q6'}}
    },
    initial_state='q0',
    final_states={'q1', 'q2', 'q3', 'q6'}
)
accept(nfa, '000')
accept(nfa, '111')
accept(nfa, '110110')



# nfa: L=(ab)*(ba)* U aa*
from automata.fa.nfa import NFA
nfa = NFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': {'q1', 'q3'}},
        'q1': {'b': {'q2'}},
        'q2': {'a': {'q1'}, 'b': {'q4'}},
        'q3': {'a': {'q3'}},
        'q4': {'a': {'q2'}}
    },
    initial_state='q0',
    final_states={'q2', 'q3'}
)
accept(nfa, 'abba')
accept(nfa, 'abbaaa')
accept(nfa, 'ababbaba')



# nfa: L=(01 U 010)*
from automata.fa.nfa import NFA
nfa = NFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': {'q1'}, '1': {'q3'}},
        'q1': {'1': {'q0', 'q2'}},
        'q2': {'0': {'q0'}, '1': {'q3'}},
    },
    initial_state='q0',
    final_states={'q1', 'q2'}
)
accept(nfa, '010101')
accept(nfa, '0101')
accept(nfa, '01010')
accept(nfa, '1001')



