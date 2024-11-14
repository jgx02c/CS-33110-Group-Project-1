from typing import List, Set, Dict, Tuple
import json
from pathlib import Path

class NFA:
    def __init__(self):
        # States definitions 
        self.states: Set[str] = {
            # Integer states
            'start', 'zero', 'oct_x', 'oct_o', 'hex_x', 'bin_b',
            'dec_digit', 'oct_digit', 'hex_digit', 'bin_digit',
            'dec_underscore', 'oct_underscore', 'hex_underscore', 'bin_underscore',
            'accept_dec', 'accept_oct', 'accept_hex', 'accept_bin',
            # Float states
            'decimal_point', 'after_decimal', 'after_decimal_underscore',
            'e_symbol', 'after_e', 'after_e_sign', 'after_e_digit',
            'after_e_underscore', 'accept_float'
        }
        
        # Alphabet definitions
        self.digits = set('0123456789')
        self.oct_digits = set('01234567')
        self.hex_digits = set('0123456789abcdefABCDEF')
        self.bin_digits = set('01')
        
        # Transition function
        self.transitions: Dict[str, Dict[str, Set[str]]] = {
            'start': {
                '0': {'zero'},
                '.': {'decimal_point'},
                **{d: {'dec_digit', 'accept_dec'} for d in '123456789'}
            },
            'zero': {
                'x': {'hex_x'},
                'o': {'oct_o'},
                'b': {'bin_b'},
                'X': {'hex_x'},
                'O': {'oct_o'},
                'B': {'bin_b'},
                '.': {'decimal_point'},
                'e': {'e_symbol'},
                'E': {'e_symbol'},
                **{d: {'oct_digit', 'accept_oct'} for d in self.oct_digits},
            },
            # Binary number states
            'bin_b': {
                **{d: {'bin_digit', 'accept_bin'} for d in self.bin_digits}
            },
            'bin_digit': {
                '_': {'bin_underscore'},
                **{d: {'bin_digit', 'accept_bin'} for d in self.bin_digits}
            },
            'bin_underscore': {
                **{d: {'bin_digit', 'accept_bin'} for d in self.bin_digits}
            },
            # Hex states
            'hex_x': {
                **{d: {'hex_digit', 'accept_hex'} for d in self.hex_digits}
            },
            'hex_digit': {
                '_': {'hex_underscore'},
                **{d: {'hex_digit', 'accept_hex'} for d in self.hex_digits}
            },
            'hex_underscore': {
                **{d: {'hex_digit', 'accept_hex'} for d in self.hex_digits}
            },
            # Octal states
            'oct_o': {
                **{d: {'oct_digit', 'accept_oct'} for d in self.oct_digits}
            },
            'oct_digit': {
                '_': {'oct_underscore'},
                **{d: {'oct_digit', 'accept_oct'} for d in self.oct_digits}
            },
            'oct_underscore': {
                **{d: {'oct_digit', 'accept_oct'} for d in self.oct_digits}
            },
            # Decimal states
            'dec_digit': {
                '_': {'dec_underscore'},
                '.': {'decimal_point'},
                'e': {'e_symbol'},
                'E': {'e_symbol'},
                **{d: {'dec_digit', 'accept_dec'} for d in self.digits}
            },
            'dec_underscore': {
                **{d: {'dec_digit', 'accept_dec'} for d in self.digits}
            },
            # Float states
            'decimal_point': {
                **{d: {'after_decimal', 'accept_float'} for d in self.digits}
            },
            'after_decimal': {
                '_': {'after_decimal_underscore'},
                'e': {'e_symbol'},
                'E': {'e_symbol'},
                **{d: {'after_decimal', 'accept_float'} for d in self.digits}
            },
            'after_decimal_underscore': {
                **{d: {'after_decimal', 'accept_float'} for d in self.digits}
            },
            'e_symbol': {
                '+': {'after_e_sign'},
                '-': {'after_e_sign'},
                **{d: {'after_e_digit', 'accept_float'} for d in self.digits}
            },
            'after_e_sign': {
                **{d: {'after_e_digit', 'accept_float'} for d in self.digits}
            },
            'after_e_digit': {
                '_': {'after_e_underscore'},
                **{d: {'after_e_digit', 'accept_float'} for d in self.digits}
            },
            'after_e_underscore': {
                **{d: {'after_e_digit', 'accept_float'} for d in self.digits}
            },
            # Accept states transitions
            'accept_dec': {
                '_': {'dec_underscore'},
                '.': {'decimal_point'},
                'e': {'e_symbol'},
                'E': {'e_symbol'},
                **{d: {'dec_digit', 'accept_dec'} for d in self.digits}
            },
            'accept_oct': {
                '_': {'oct_underscore'},
                **{d: {'oct_digit', 'accept_oct'} for d in self.oct_digits}
            },
            'accept_hex': {
                '_': {'hex_underscore'},
                **{d: {'hex_digit', 'accept_hex'} for d in self.hex_digits}
            },
            'accept_bin': {
                '_': {'bin_underscore'},
                **{d: {'bin_digit', 'accept_bin'} for d in self.bin_digits}
            },
            'accept_float': {
                '_': {'after_decimal_underscore'},
                'e': {'e_symbol'},
                'E': {'e_symbol'},
                **{d: {'after_decimal', 'accept_float'} for d in self.digits}
            }
        }
        
        # Accept states
        self.accept_states = {'accept_dec', 'accept_oct', 'accept_hex', 'accept_bin', 'accept_float'}

    def accepts(self, input_string: str) -> Tuple[bool, str]:
        """
        Check if the input string is accepted by the NFA.
        Returns (is_accepted, number_type)
        """
        # Remove any whitespace
        input_string = input_string.strip()
        
        # Special cases for invalid inputs
        if input_string.endswith('_'):
            return False, "invalid"
        if '__' in input_string:
            return False, "invalid"
        if input_string.endswith('e') or input_string.endswith('E'):
            return False, "invalid"
        if input_string.endswith('+') or input_string.endswith('-'):
            return False, "invalid"
            
        current_states = {'start'}
        
        for char in input_string:
            next_states = set()
            for state in current_states:
                if state in self.transitions:
                    for input_char, next_state_set in self.transitions[state].items():
                        if char == input_char:
                            next_states.update(next_state_set)
            
            if not next_states:
                return False, "invalid"
            
            current_states = next_states
        
        # Determine the type of number
        if not any(state in self.accept_states for state in current_states):
            return False, "invalid"
            
        if 'accept_float' in current_states:
            return True, "float"
        elif 'accept_hex' in current_states:
            return True, "hexadecimal"
        elif 'accept_oct' in current_states:
            return True, "octal"
        elif 'accept_bin' in current_states:
            return True, "binary"
        elif 'accept_dec' in current_states:
            return True, "decimal"
        
        return False, "invalid"

def process_input_file(nfa: NFA, input_filename: str, output_filename: str):
    """Process input file and write results to output file."""
    # Make sure the file exists in the same directory as the script
    script_dir = Path(__file__).parent  # Get the script's directory
    file_path = script_dir / input_filename  # Create the full file path
    output_file_path = script_dir / output_filename # Create the full path for the output file

    # Check if the file exists and then open it
    if file_path.exists():
        with file_path.open('r') as f:
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
        actual, number_type = nfa.accepts(test_string)
        
        # Compare results
        passed = actual == expected
        
        results.append({
            'test_string': test_string,
            'expected': expected,
            'actual': actual,
            'number_type': number_type,
            'passed': passed
        })
    
   # Write results to the output file
    with open(output_file_path, 'w') as f:
        f.write("Test Results:\n")
        f.write("-" * 50 + "\n")
        for result in results:
            f.write(f"Input: {result['test_string']}\n")
            f.write(f"Expected: {result['expected']}\n")
            f.write(f"Actual: {result['actual']}\n")
            f.write(f"Number Type: {result['number_type']}\n")
            f.write(f"Test {'PASSED' if result['passed'] else 'FAILED'}\n")
            f.write("-" * 50 + "\n")

def main():
    nfa = NFA()
    
    while True:
        print("\nPython Number Literal Recognizer")
        print("1. Test single input")
        print("2. Process test file")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            test_string = input("Enter a string to test: ")
            result, number_type = nfa.accepts(test_string)
            print(f"Result: {result} ({number_type} Python number literal)")
            
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