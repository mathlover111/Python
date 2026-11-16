# Open a file using open()
# file name "note.txt"
# "w" stands for write mode.
file = open("note.txt", "w", encoding="utf-8")

# Writing text to a file
file.write("114514")


# Close the file and release system resources
file.close()

print("success write")
