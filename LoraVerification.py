try:
    import lora  # Replace 'lora' with the actual module name if different
    print("LoRa library imported successfully!")
except ImportError as e:
    print("Failed to import LoRa library:", e)
    

print(dir(lora))