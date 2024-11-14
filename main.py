from typing import List, Set, Dict, Tuple
import json

class NFA:
    def __init__(self):
        # States definitions
        self.states: Set[str] = {
            'start', 'zero', 'oct_x', 'oct_o', 'hex_x', 
            'dec_digit', 'oct_digit', 'hex_digit',
            'accept_dec', 'accept_oct', 'accept_hex'
        }
        
        # Alphabet definitions
        self.digits = set('0123456789')
        self.oct_digits = set('01234567')
        self.hex_digits = set('0123456789abcdefABCDEF')
        
        # Transition function
        self.transitions: Dict[str, Dict[str, Set[str]]] = {
            'start': {
                '0': {'zero'},
                **{d: {'dec_digit', 'accept_dec'} for d in '123456789'}
            },
            'zero': {
                'x': {'hex_x'},
                'o': {'oct_o'},
                'X': {'hex_x'},
                'O': {'oct_o'},
                **{d: {'oct_digit', 'accept_oct'} for d in self.oct_digits},
            },
            'hex_x': {
                **{d: {'hex_digit', 'accept_hex'} for d in self.hex_digits}
            },
            'oct_o': {
                **{d: {'oct_digit', 'accept_oct'} for d in self.oct_digits}
            },
            'dec_digit': {
                **{d: {'dec_digit', 'accept_dec'} for d in self.digits}
            },
            'oct_digit': {
                **{d: {'oct_digit', 'accept_oct'} for d in self.oct_digits}
            },
            'hex_digit': {
                **{d: {'hex_digit', 'accept_hex'} for d in self.hex_digits}
            },
            'accept_dec': {
                **{d: {'dec_digit', 'accept_dec'} for d in self.digits}
            },
            'accept_oct': {
                **{d: {'oct_digit', 'accept_oct'} for d in self.oct_digits}
            },
            'accept_hex': {
                **{d: {'hex_digit', 'accept_hex'} for d in self.hex_digits}
            }
        }
        
        # Accept states
        self.accept_states = {'accept_dec', 'accept_oct', 'accept_hex'}
        
    def accepts(self, input_string: str) -> bool:
        """Check if the input string is accepted by the NFA."""
        current_states = {'start'}
        
        for char in input_string:
            next_states = set()
            for state in current_states:
                if state in self.transitions:
                    for input_char, next_state_set in self.transitions[state].items():
                        if char == input_char:
                            next_states.update(next_state_set)
            
            if not next_states:
                return False
            
            current_states = next_states
        
        return any(state in self.accept_states for state in current_states)

def process_input_file(nfa: NFA, input_filename: str, output_filename: str):
    """Process input file and write results to output file."""
    with open(input_filename, 'r') as f:
        lines = f.readlines()
    
    results = []
    for line in lines:
        # Split line into test string and expected result
        parts = line.strip().split()
        if len(parts) != 2:
            continue
            
        test_string, expected = parts
        expected = expected.lower() == 'true'
        
        # Get actual result
        actual = nfa.accepts(test_string)
        
        # Compare results
        passed = actual == expected
        
        results.append({
            'test_string': test_string,
            'expected': expected,
            'actual': actual,
            'passed': passed
        })
    
    # Write results to output file
    with open(output_filename, 'w') as f:
        f.write("Test Results:\n")
        f.write("-" * 50 + "\n")
        for result in results:
            f.write(f"Input: {result['test_string']}\n")
            f.write(f"Expected: {result['expected']}\n")
            f.write(f"Actual: {result['actual']}\n")
            f.write(f"Test {'PASSED' if result['passed'] else 'FAILED'}\n")
            f.write("-" * 50 + "\n")

def main():
    nfa = NFA()
    
    while True:
        print("\nPython Integer Literal Recognizer")
        print("1. Test single input")
        print("2. Process test file")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            test_string = input("Enter a string to test: ")
            result = nfa.accepts(test_string)
            print(f"Result: {result} ({'valid' if result else 'invalid'} Python integer literal)")
            
        elif choice == '2':
            input_file = input("Enter input filename (default: in_ans.txt): ").strip() or "in_ans.txt"
            output_file = input("Enter output filename (default: out.txt): ").strip() or "out.txt"
            try:
                process_input_file(nfa, input_file, output_file)
                print(f"Results written to {output_file}")
            except FileNotFoundError:
                print(f"Error: Could not find input file '{input_file}'")
                
        elif choice == '3':
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()