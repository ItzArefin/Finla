# 🔠 YAML Small Caps Formatter

This Python script converts select text elements in a `.yml` file into **small caps Unicode**—perfect for stylizing Minecraft plugin configs or any other visual YAML-based content.

---

## ✨ Features

- 🔤 **Small Caps Conversion**:
  - Transforms normal letters into stylish small caps for visual flair.
  
- 🎨 **Color Code Compatibility**:
  - Maintains Minecraft-style color codes (e.g. `&b`, `&f`, etc).

- 🧠 **Smart Text Detection**:
  - Converts:
    - Words inside brackets: `&a[Example]` → `&a[ᴇxᴀᴍᴘʟᴇ]`
    - Labels and prefixes: `&eName:` → `&eɴᴀᴍᴇ:`
    - Regular words with color codes: `&cServer` → `&csᴇʀᴠᴇʀ`
    - Domains/IPs: `play.example.com` → `ᴘʟᴀʏ.ᴇxᴀᴍᴘʟᴇ.ᴄᴏᴍ`

---

## 🛠️ Usage

1. Place your YAML file as `input.yml` in the script directory.
2. Run the script:
   ```bash
   python script.py```
