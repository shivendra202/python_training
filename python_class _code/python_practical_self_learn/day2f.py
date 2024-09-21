def get_unique_references(reference_list):
    # Convert the list to a set to remove duplicates, then convert back to a list
    unique_references = list(set(reference_list))
    return unique_references

# Example usage
references = ["ref1", "ref2", "ref3", "ref1", "ref2", "ref4"]
unique_references = get_unique_references(references)
print("Unique references:", unique_references)
