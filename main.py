from src.validator import validate_sequence

print(validate_sequence("ATGCGA"))      # Expected: True
print(validate_sequence("atgcga"))      # Expected: True
print(validate_sequence("AT GC GA"))    # Expected: True
print(validate_sequence("ATGBCA"))      # Expected: False
print(validate_sequence(""))            # Expected: False