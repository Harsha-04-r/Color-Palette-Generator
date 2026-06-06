# Color Palette Generator
A Python + Tkinter desktop app that extracts dominant and palette colors from any image.

## Features
- 🖼️ Upload any image (PNG, JPG, JPEG, GIF, BMP, TIFF)
- 🎨 Extracts 1 dominant color + 9 palette colors
- 🖱️ Click any color button to see its hex and rgb values
- 📋 Click hex or rgb value to copy it to clipboard
- 🔄 Change image anytime with the Change Image button
- ⚠️ Invalid file format warning

## Preview
<img width="1920" height="1080" alt="Screenshot (171)" src="https://github.com/user-attachments/assets/62be1dec-fdfc-4307-9fb7-aa42b38a640a" />
<img width="1920" height="1080" alt="Screenshot (172)" src="https://github.com/user-attachments/assets/6ce0ba27-d096-47df-a30d-020fa9363ac4" />
<img width="1920" height="1080" alt="Screenshot (173)" src="https://github.com/user-attachments/assets/2cdbb1df-fa59-4cc2-99cc-7c1ea20880c5" />
<img width="1920" height="1080" alt="Screenshot (175)" src="https://github.com/user-attachments/assets/a46830ac-dbe2-4926-8311-ee7d453101a5" />




## How It Works
1. Click **Upload Image** and select an image file.
2. The app extracts the dominant color and 9 palette colors.
3. Click any color button to display its hex and rgb codes.
4. Click the hex or rgb value to copy it to your clipboard.

## Technologies Used
- Python
- Tkinter
- Pillow (image handling)
- ColorThief (color extraction)
- webcolors (rgb to hex conversion)
- pyperclip (clipboard copy)

## Installation
Clone the repository:
```bash
git clone https://github.com/yourusername/color-palette-generator.git
cd color-palette-generator
```
Install dependencies:
```bash
pip install pillow colorthief webcolors pyperclip
```
Run the application:
```bash
python main.py
```

## Future Improvements
- Name colors using nearest CSS color name
- Drag and drop image support
- Increase palette size option
