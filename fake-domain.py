import random
import sys

def generate_fake_domains(legitimate_domain):
    """Generate 4 different fake domain variants"""
    
    homograph_map = {
        'a': 'а', 'e': 'е', 'o': 'о', 'c': 'с', 'p': 'р',
        'x': 'х', 'y': 'у', 'i': 'і', 'k': 'к', 'm': 'м'
    }
    
    invisible_chars = ['\u200B', '\u200C', '\u200D', '\u200E', '\u200F']
    
    variants = []
    
    # Variant 1: Just homographs
    variant1 = []
    for char in legitimate_domain:
        if char.lower() in homograph_map and random.random() > 0.7:
            variant1.append(homograph_map[char.lower()])
        else:
            variant1.append(char)
    variants.append(''.join(variant1))
    
    # Variant 2: Homographs + invisible characters
    variant2 = []
    for char in legitimate_domain:
        if char.lower() in homograph_map and random.random() > 0.6:
            variant2.append(homograph_map[char.lower()])
        else:
            variant2.append(char)
        if random.random() > 0.8 and char not in ['.', '-', '_']:
            variant2.append(random.choice(invisible_chars))
    variants.append(''.join(variant2))
    
    # Variant 3: Focus on TLD homographs
    variant3 = list(legitimate_domain)
    if '.' in legitimate_domain:
        dot_index = legitimate_domain.rfind('.')
        for i in range(dot_index + 1, len(legitimate_domain)):
            if legitimate_domain[i] in homograph_map:
                variant3[i] = homograph_map[legitimate_domain[i]]
    variants.append(''.join(variant3))
    
    # Variant 4: Mixed approach
    variant4 = []
    for i, char in enumerate(legitimate_domain):
        if i < len(legitimate_domain) // 2 and char.lower() in homograph_map and random.random() > 0.5:
            variant4.append(homograph_map[char.lower()])
        else:
            variant4.append(char)
        if i % 2 == 0 and random.random() > 0.7:
            variant4.append(random.choice(invisible_chars))
    variants.append(''.join(variant4))
    
    return variants

def main():
    if len(sys.argv) != 2:
        print("Usage: python fake_domain.py <domain>")
        print("Example: python fake_domain.py paypal.com")
        sys.exit(1)
    
    legitimate_domain = sys.argv[1]
    
    # Validate domain format
    if '.' not in legitimate_domain:
        print("Error: Please provide a valid domain (e.g., example.com)")
        sys.exit(1)
    
    fake_domains = generate_fake_domains(legitimate_domain)
    
    print(f"Original: {legitimate_domain}")
    print("Fake domains:")
    for i, fake in enumerate(fake_domains, 1):
        print(f"{i}. {fake}")

if __name__ == "__main__":
    main()
