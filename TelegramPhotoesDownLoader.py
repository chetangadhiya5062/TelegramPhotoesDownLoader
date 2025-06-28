from telethon.sync import TelegramClient
from telethon.tl.types import InputMessagesFilterPhotos
import os

# Telegram API credentials
api_id = Enter Your API ID          # Replace with your API ID
api_hash = 'API Hash'    # Replace with your API Hash

# Output folder for downloaded photos
output_folder = "telegram_photos"
os.makedirs(output_folder, exist_ok=True)

# Start Telegram Client
with TelegramClient('photo_downloader_session', api_id, api_hash) as client:
    
    # Step 1: List all chats
    dialogs = client.get_dialogs()
    print("\nAvailable Chats:\n")
    for i, dialog in enumerate(dialogs):
        print(f"{i}. {dialog.name}")

    # Step 2: User selects a chat
    chat_index = int(input("\nEnter the number of the chat you want to download photos from: "))
    target_entity = dialogs[chat_index].entity
    target_name = dialogs[chat_index].name

    print(f"\nDownloading photos from: {target_name}...\n")

    # Step 3: Download all photos from selected chat
    count = 0
    for message in client.iter_messages(target_entity, filter=InputMessagesFilterPhotos):
        if message.photo:
            file_path = client.download_media(message, file=output_folder)
            if file_path:
                count += 1
                print(f"Downloaded: {file_path}")

    print(f"\n✅ Total photos downloaded from '{target_name}': {count}")
