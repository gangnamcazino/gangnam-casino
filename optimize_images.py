import os
import shutil
from PIL import Image

image_names = [
    "1. 딜러_정면_토끼홀복",
    "2. 실제카지노칩과 트레이",
    "3. 카지노로비 컨시어지 상담",
    "4. 바카라 진행테이블",
    "5. 카지노 VIP 컨시어지 서비스",
    "6. 데일리이벤트",
    "7. 위클리 이벤트",
    "8. 365일_24시간운영"
]

backup_dir = "backup_originals"
os.makedirs(backup_dir, exist_ok=True)

print("Starting image optimization...")

total_orig_size = 0
total_webp_size = 0
total_png_size = 0

for name in image_names:
    png_file = f"{name}.png"
    webp_file = f"{name}.webp"
    backup_file = os.path.join(backup_dir, png_file)
    
    if not os.path.exists(png_file):
        print(f"File not found: {png_file}")
        continue
        
    orig_size = os.path.getsize(png_file)
    total_orig_size += orig_size
    
    # Backup original if not already backed up
    if not os.path.exists(backup_file):
        shutil.copy2(png_file, backup_file)
        
    with Image.open(png_file) as img:
        # Maintain aspect ratio, max width 1200
        w, h = img.size
        max_w = 1200
        if w > max_w:
            new_w = max_w
            new_h = int(h * (max_w / w))
            resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        else:
            resized = img.copy()
            
        # 1. Save WebP (ultra fast, high quality)
        resized.save(webp_file, "WEBP", quality=82, method=6)
        webp_size = os.path.getsize(webp_file)
        total_webp_size += webp_size
        
        # 2. Overwrite PNG with optimized version (smaller fallback)
        resized.save(png_file, "PNG", optimize=True)
        png_size = os.path.getsize(png_file)
        total_png_size += png_size
        
        print(f"{name}:")
        print(f"  Original: {orig_size / 1024 / 1024:.2f} MB")
        print(f"  WebP:     {webp_size / 1024:.1f} KB ({(1 - webp_size / orig_size) * 100:.1f}% reduction)")
        print(f"  Opt PNG:  {png_size / 1024 / 1024:.2f} MB\n")

print("==================================================")
print(f"Total Original: {total_orig_size / 1024 / 1024:.2f} MB")
print(f"Total WebP:     {total_webp_size / 1024 / 1024:.2f} MB ({(1 - total_webp_size / total_orig_size) * 100:.1f}% total reduction)")
print(f"Total Opt PNG:  {total_png_size / 1024 / 1024:.2f} MB")
print("==================================================")
