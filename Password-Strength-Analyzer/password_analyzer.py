# password_analyzer.py

from zxcvbn import zxcvbn
import argparse
import itertools

def analyze_password(password):
    result = zxcvbn(password)
    score = result['score']
    feedback = result['feedback']
    print("\nPassword Strength Report:")
    print(f"Score (0-4): {score}")
    
    strength = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
    print(f"Strength: {strength[score]}")
    
    if feedback['warning']:
        print("Warning:", feedback['warning'])
    if feedback['suggestions']:
        print("Suggestions:", ', '.join(feedback['suggestions']))
    print("\n")

def generate_wordlist(name, dob, pet):
    # Creating simple patterns for custom wordlist
    base_words = [name, dob, pet]
    patterns = []

    # Simple combos like Name+DOB, Name+Pet, etc.
    for i in range(1, len(base_words)+1):
        for combo in itertools.permutations(base_words, i):
            patterns.append(''.join(combo))

    # Adding variations with common suffixes/prefixes
    suffixes = ['@123', '123', '!', '2025']
    extended_patterns = []

    for word in patterns:
        for suf in suffixes:
            extended_patterns.append(word + suf)

    total_words = patterns + extended_patterns

    with open("wordlist.txt", "w") as f:
        for word in total_words:
            f.write(word + "\n")

    print(f"\n[+] Wordlist generated successfully! {len(total_words)} entries saved to 'wordlist.txt'\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Password Strength Analyzer & Custom Wordlist Generator")
    
    parser.add_argument("-p", "--password", help="Password to analyze")
    parser.add_argument("-w", "--wordlist", nargs=3, metavar=('NAME', 'DOB', 'PET'),
                        help="Generate custom wordlist using personal info: NAME DOB PET")

    args = parser.parse_args()

    if args.password:
        analyze_password(args.password)
    if args.wordlist:
        name, dob, pet = args.wordlist
        generate_wordlist(name, dob, pet)
    
    if not args.password and not args.wordlist:
        parser.print_help()
