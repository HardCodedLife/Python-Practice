
#!/bin/bash

# Loop through all files in the current directory
for file in *; do
    # Check if the filename contains exactly one digit (not followed or preceded by another digit)
    # This matches 'filename1.txt' but ignores 'filename10.txt'
    if [[ "$file" =~ ^([^0-9]*)([0-9])([^0-9]*)$ ]]; then
        prefix="${BASH_REMATCH[1]}"
        digit="${BASH_REMATCH[2]}"
        suffix="${BASH_REMATCH[3]}"
        
        # Construct the new filename with a leading zero
        new_name="${prefix}0${digit}${suffix}"
        
        echo "Renaming '$file' to '$new_name'"
        mv "$file" "$new_name"
    fi
done
