# File Handling + Error Handling Challenge

# Ask user for a filename
filename = input("Enter the filename you want to read: ")

try:
    # Try opening and reading the file
    with open(filename, "r") as infile:
        content = infile.read()
        print("\n✅ Original File Content:\n")
        print(content)

    # Modify the content (convert to uppercase as an example)
    modified_content = content.upper()

    # Write the modified content into a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as outfile:
        outfile.write(modified_content)

    print(f"\n🎉 Success! Modified content written to {new_filename}")

# Handle possible errors
except FileNotFoundError:
    print("❌ Error: File not found. Please check the filename and try again.")

except PermissionError:
    print("❌ Error: You don’t have permission to read this file.")

except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")

finally:
    print("\nOperation complete. Thank you for using the program.")
