# ðŸŽ¨ Finla â€” YAML Small Caps Formatter  
*Aesthetic Minecraft Language File Formatter*

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square)  
![Status](https://img.shields.io/badge/Project%20Status-Active-brightgreen?style=flat-square)  
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

---

## âœ¨ Overview

**Finla** is a Python-powered tool that beautifully transforms selected text in `.yml` files into **small caps Unicode**, perfect for **Minecraft plugin language files** and other visual YAML content.

Made for **developers who love aesthetic vibes and clean configs.**

---

## ðŸš€ Features

- ðŸ”  **Small Caps Conversion**  
  Transform regular letters into stylish **small caps Unicode** for visual appeal.

- ðŸŽ¨ **Color Code Compatibility**  
  Fully supports Minecraft-style color codes like `&a`, `&b`, `&f` â€” colors remain intact.

- ðŸ§  **Smart Text Detection**  
  Finla intelligently detects and converts:
  - âœ… **Bracketed Words**  
    `&a[Example]` â†’ `&a[á´‡xá´€á´á´˜ÊŸá´‡]`
  - âœ… **Prefixes & Labels**  
    `&eName:` â†’ `&eÉ´á´€á´á´‡:`
  - âœ… **Regular Colored Words**  
    `&cServer` â†’ `&csá´‡Ê€á´ á´‡Ê€`
  - âœ… **Domains & IPs**  
    `play.example.com` â†’ `á´˜ÊŸá´€Ê.á´‡xá´€á´á´˜ÊŸá´‡.á´„á´á´`

- ðŸŒŸ **Aesthetic-First Approach**  
  Built for developers who care about the look of their Minecraft configurations.

- ðŸŽ‰ **Upcoming Features**  
  Emoji support and more customization options coming soon!

---

## ðŸ“‚ Getting Started

### Prerequisites
- Python 3.8 or higher

### Installation
Clone the repository:
```bash
git clone https://github.com/ItzArefin/finla.git
cd finla
```

### Usage
1. Place your YAML file in the project directory and name it `input.yml`.
2. Run the script:
   ```bash
   python Finla.py
   ```
3. The formatted YAML will be saved as `output.yml`.

---

## ðŸ“¸ Example

**Before:**
```yaml
- '&a[Server]'
- '&cServer Name:'
- '&eplay.example.com'
```

**After:**
```yaml
- '&a[êœ±á´‡Ê€á´ á´‡Ê€]'
- '&cêœ±á´‡Ê€á´ á´‡Ê€ É´á´€á´á´‡:'
- '&eá´˜ÊŸá´€Ê.á´‡xá´€á´á´˜ÊŸá´‡.á´„á´á´'
```

---

## ðŸ“Œ Roadmap
- [x] Small caps formatting
- [ ] Emoji support
- [ ] Customizable style options
- [ ] GUI version (planned)

---

## ðŸ¤ Contributing

Contributions, suggestions, and issues are welcome!  
Please feel free to open a pull request or start a discussion.

---

## ðŸ“„ License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## ðŸ’¬ Contact

Made with â¤ï¸ for Minecraft developers.  
GitHub: [ItzArefin](https://github.com/ItzArefin)
