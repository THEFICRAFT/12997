from PIL import Image, ImageEnhance
import numpy as np

# Load dan resize gambar
original_img = Image.open("nama_file_logo_kamu.png").convert("RGBA")
resized_img = original_img.resize((512, 512), resample=Image.BICUBIC)

# Parameter animasi
gif_duration = 3  # durasi dalam detik
gif_fps = 12  # frame per detik
gif_frames = gif_duration * gif_fps

gif_frame_list = []

for i in range(gif_frames):
    t = i / gif_fps  # waktu saat ini dalam detik

    # ✨ Efek kilau neon (naik turun brightness)
    pulse = 1 + 0.3 * np.sin(2 * np.pi * t * 1.5)
    enhanced_img = ImageEnhance.Brightness(resized_img).enhance(pulse)

    # 🪽 Efek gerakan sayap (ubah ukuran sedikit)
    scale = 1 + 0.01 * np.sin(2 * np.pi * t * 2)
    new_size = (int(enhanced_img.width * scale), int(enhanced_img.height * scale))
    frame = enhanced_img.resize(new_size, resample=Image.BICUBIC)

    # Tempelkan ke background hitam
    background = Image.new("RGBA", resized_img.size, (0, 0, 0, 255))
    offset = ((background.width - frame.width) // 2, (background.height - frame.height) // 2)
    background.paste(frame, offset, frame)

    # ✍️ Efek teks fade-in (simulasi seluruh gambar fade-in)
    alpha = min(1, t / 1.5)  # efek muncul dalam 1.5 detik pertama
    frame_np = np.array(background).astype(np.float32)
    frame_np *= alpha
    frame_np = np.clip(frame_np, 0, 255).astype(np.uint8)

    gif_frame = Image.fromarray(frame_np).convert("P", palette=Image.ADAPTIVE)
    gif_frame_list.append(gif_frame)

# Simpan sebagai GIF
gif_frame_list[0].save(
    "theficraft_neon_animated.gif",
    save_all=True,
    append_images=gif_frame_list[1:],
    duration=int(1000 / gif_fps),
    loop=0
)
