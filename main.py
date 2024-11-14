from typing import List, Set, Dict, Tuple
import json

class NFA:
  

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