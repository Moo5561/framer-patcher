import os
import re

# Default fallback settings if config.txt is missing or broken
config = {
    "name": "Default Framer Site",
    "favicon": "favicon.ico"
}

def load_config():
    config_file = "config.txt"
    if not os.path.exists(config_file):
        print("Warning: config.txt not found! Using default settings.")
        return

    print("Reading configuration from config.txt...")
    with open(config_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # Skip empty lines and comments
            if not line or line.startswith("#"):
                continue
            
            if "=" in line:
                key, val = line.split("=", 1)
                key = key.strip().lower()
                # Clean up quotes around the value
                val = val.strip().strip('"').strip("'")
                config[key] = val

def patch_html_file(file_path):
    print(f"Patching: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Inject the Watermark Killer CSS right before </head>
    css_patch = """
    <style>
      #__framer-badge-container, .framer-badge { display: none !important; }
    </style>
    </head>
    """
    if "</head>" in content and "framer-badge" not in content:
        content = content.replace("</head>", css_patch)

    # 2. Patch the Title
    content = re.sub(r"<title>.*?</title>", f"<title>{config['name']}</title>", content)

    # 3. Patch the Favicon
    fav_val = config['favicon']
    favicon_code = f'<link rel="icon" href="{fav_val}">'
    
    # Replace existing favicon tags or inject a new one
    if 'rel="icon"' in content or 'rel="shortcut icon"' in content:
        content = re.sub(r'<link rel="(shortcut )?icon".*?>', favicon_code, content)
    else:
        content = content.replace("</head>", f"{favicon_code}\n</head>")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    load_config()
    print(f"Target Title: {config['name']}")
    print(f"Target Favicon: {config['favicon']}")
    print("-" * 40)

    # Scan the current directory and all subdirectories for HTML files
    html_found = False
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".html"):
                html_found = True
                patch_html_file(os.path.join(root, file))
                
    if html_found:
        print("-" * 40)
        print("All files successfully patched! Watermark is gone.")
    else:
        print("Error: No HTML files found in this directory to patch.")

if __name__ == "__main__":
    main()