import sys
import warnings
warnings.filterwarnings('ignore')
try:
    from PIL import Image
    img = Image.open(r'c:\Users\ADMIN\Documents\AI_QUEST_LTP\blog-html\design-md-b2b-system-mockup\images\icon_claude.webp').convert('L')
    w,h = img.size
    img = img.resize((30, int(h/w * 30 * 0.55)))
    chars = ['█','▓','▒','░',' ']
    data = img.getdata()
    out = ""
    for idx, p in enumerate(data):
        out += chars[int(p/52)]
        if (idx+1) % 30 == 0:
            out += "\n"
    print(out)
except Exception as e:
    print(f"Error: {e}")
