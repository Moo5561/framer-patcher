import os

# Define the patch code with a unique signature comment
PATCH_SIGNATURE = "/* FRAMER_WATERMARK_KILLER_PATCH */"
css_patch = f"""
    <style>
      {PATCH_SIGNATURE}
      #__framer-badge-container, .__framer-badge, .framer-badge, #__framer-editorbar-button {{ 
        display: none !important; 
        visibility: hidden !important;
        opacity: 0 !important;
        pointer-events: none !important;
      }}
    </style>
    </head>
"""

def patch_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if we already applied this specific patch
    if PATCH_SIGNATURE in content:
        print(f"Already patched: {file_path}")
        return

    if "</head>" in content:
        content = content.replace("</head>", css_patch)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully patched: {file_path}")
    else:
        print(f"No </head> tag found in: {file_path}")

def run_patcher():
    # Targets index.html and any other html files in the directory
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                patch_file(os.path.join(root, file))

if __name__ == "__main__":
    run_patcher()
