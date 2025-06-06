import itertools
import string
import csv

def generate_combinations(length, character_set):
    """
    A generator function that yields all possible combinations for a given
    length from a given character set.

    Args:
        length (int): The desired length of the combinations.
        character_set (str): The characters to use for combinations.

    Yields:
        str: A single combination as a string.
    """
    # itertools.product generates the cartesian product.
    # 'repeat' specifies the length of each combination.
    for combo_tuple in itertools.product(character_set, repeat=length):
        yield "".join(combo_tuple)

def build_the_infinite_library():
    """
    Generates every possible combination of text and saves it to a CSV file.
    This function is designed to run forever, assuming infinite resources.
    """
    # Define the character set. We'll include lowercase, uppercase, digits,
    # punctuation, and a space for a more complete "library".
    character_set = string.ascii_letters + string.digits + string.punctuation + ' '
    output_filename = 'infinite_library.csv'
    
    print(f"Beginning the infinite generation process.")
    print(f"Character set contains {len(character_set)} unique characters.")
    print(f"Output will be continuously written to '{output_filename}'...")

    try:
        # Open the CSV file in write mode with newline='' to prevent blank rows.
        with open(output_filename, 'w', newline='', encoding='utf-8') as f:
            # Create a CSV writer object.
            writer = csv.writer(f)
            
            # Write the header row to the CSV file.
            writer.writerow(['combination'])
            
            # This is the infinite loop. itertools.count(1) counts up from 1 forever.
            for length in itertools.count(1):
                print(f"\n--- Now generating all combinations of length {length} ---")
                
                # Get the generator for the current length.
                combination_generator = generate_combinations(length, character_set)
                
                # Write all combinations for the current length to the CSV.
                for combo in combination_generator:
                    writer.writerow([combo])
                
                print(f"--- Finished all combinations of length {length}. Moving to length {length + 1}. ---")

    except KeyboardInterrupt:
        print("\nProcess stopped by user. The library is incomplete.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    build_the_infinite_library()
