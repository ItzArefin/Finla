# 🎨 Finla - YAML Small Caps Formatter
*Make your Minecraft configs look stunning! ✨*

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## 🌟 What is Finla?

**Finla** transforms your YAML text into **ᴄᴏᴏʟ sᴍᴀʟʟ ᴄᴀᴘs** for Minecraft server configs and plugin language files.

---

## ✨ Features

🔤 **Smart Small Caps Conversion** - Converts text to Unicode small caps  
🎨 **Minecraft Color Code Support** - Works with `&a`, `&c`, `&e` and all color codes  
🧠 **Intelligent Detection** - Handles brackets, labels, domains, and regular text  
⚡ **Fast Processing** - Transform entire YAML files in seconds

---

## 🚀 Quick Start

### Requirements
- Python 3.8+

### Installation & Usage
```bash
# Clone and navigate
git clone https://github.com/ItzArefin/finla.git
cd finla

# Add your YAML file as 'input.yml'
# Run the formatter
python Finla.py

# Get your formatted file as 'output.yml'
```

---

## 📖 Examples

### Before:
```yaml
messages:
  welcome: '&a[Welcome] &fHello player!'
  server_name: '&cAwesome Server'
  website: '&eplay.server.com'
```

### After:
```yaml
messages:
  welcome: '&a[ᴡᴇʟᴄᴏᴍᴇ] &fʜᴇʟʟᴏ ᴘʟᴀʏᴇʀ!'
  server_name: '&cᴀᴡᴇsᴏᴍᴇ sᴇʀᴠᴇʀ'
  website: '&eᴘʟᴀʏ.sᴇʀᴠᴇʀ.ᴄᴏᴍ'
```

---

## 🗺️ Roadmap

- [x] Small caps conversion
- [x] Color code support
- [ ] Custom emoji integration
- [ ] GUI application
- [ ] Multiple formatting styles

---

## 📜 License

MIT License - free to use in your projects!

---

## 💬 Connect

Made with ❤️ for Minecraft developers  
**GitHub**: [ItzArefin](https://github.com/ItzArefin)

⭐ **Star us** if Finla helped your server look amazing!
