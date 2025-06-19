import re

def to_small_caps(text):
    small_caps_map = str.maketrans(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ" * 2
    )
    return text.translate(small_caps_map)

def convert_line(line):

    line = re.sub(r"(&[a-f0-9l-or])\[(\w+?)\]", lambda m: f"{m.group(1)}[{to_small_caps(m.group(2))}]", line)

    line = re.sub(r"(&[a-f0-9l-or])([A-Za-z ]+?):", lambda m: f"{m.group(1)}{to_small_caps(m.group(2))}:", line)

    line = re.sub(r"((?:&[a-f0-9l-or])+)([A-Za-z]{3,})\b", lambda m: f"{m.group(1)}{to_small_caps(m.group(2))}", line)

    def domain_replacer(match):
        parts = match.group().split('.')
        return '.'.join(to_small_caps(p) for p in parts)

    line = re.sub(r"\b[\w\-]+\.[\w\-.]+\b", domain_replacer, line)

    return line

def convert_file(content):
    return "\n".join(convert_line(line) for line in content.splitlines())

with open("input.yml", "r", encoding="utf-8") as f:
    original = f.read()

converted = convert_file(original)

with open("output.yml", "w", encoding="utf-8") as f:
    f.write(converted)

print("✅ All done! Check output.yml for results with small caps everywhere.")
