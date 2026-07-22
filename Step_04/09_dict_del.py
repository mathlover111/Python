user_info = {
    "name": "Homo",
    "phone": "0919191919",
    "status": "暫時離線"
}
print(f"刪除前: {user_info}")

removed_value = user_info.pop("status")

print(f"被刪除的內容是: {removed_value}")
print(f"刪除後: {user_info}")