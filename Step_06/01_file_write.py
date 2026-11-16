# Open a file using open()
# file name "note.txt"
# "w" 代表 寫入模式
file = open("note.txt", "w", encoding="utf-8")

# Writing text to a file
file.write("114514")


# Close the file and release system resources
file.close()

print("寫入成功")
