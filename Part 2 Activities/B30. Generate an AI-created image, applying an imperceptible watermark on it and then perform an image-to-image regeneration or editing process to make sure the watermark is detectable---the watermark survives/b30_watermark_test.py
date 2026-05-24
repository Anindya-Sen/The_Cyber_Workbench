import cv2
from PIL import Image, ImageEnhance
from imwatermark import WatermarkEncoder, WatermarkDecoder
from pathlib import Path


# =========================
# SETTINGS
# =========================
INPUT_IMAGE = "original.png"
WATERMARKED_IMAGE = "watermarked.png"
EDITED_IMAGE = "edited.jpg"   # save as JPG to simulate a realistic light edit
WATERMARK_TEXT = "B30A"       # 4 characters = 32 bits
METHOD = "dwtDct"             # recommended default method


# =========================
# STEP 1: Embed watermark
# =========================
def embed_watermark():
    print("Embedding invisible watermark...")

    bgr = cv2.imread(INPUT_IMAGE)
    if bgr is None:
        raise FileNotFoundError(f"Could not find input image: {INPUT_IMAGE}")

    encoder = WatermarkEncoder()
    encoder.set_watermark("bytes", WATERMARK_TEXT.encode("utf-8"))

    watermarked = encoder.encode(bgr, METHOD)
    cv2.imwrite(WATERMARKED_IMAGE, watermarked)

    print(f"Saved watermarked image as: {WATERMARKED_IMAGE}")


# =========================
# STEP 2: Extract watermark
# =========================
def extract_watermark(image_path: str):
    print(f"Extracting watermark from: {image_path}")

    bgr = cv2.imread(image_path)
    if bgr is None:
        raise FileNotFoundError(f"Could not open image: {image_path}")

    decoder = WatermarkDecoder("bytes", 32)  # 4 chars = 32 bits
    wm = decoder.decode(bgr, METHOD)

    try:
        text = wm.decode("utf-8")
    except Exception:
        text = str(wm)

    print(f"Detected watermark: {text}")
    return text


# =========================
# STEP 3: Apply a gentle edit
# =========================
def make_light_edit():
    print("Applying a gentle edit...")

    img = Image.open(WATERMARKED_IMAGE).convert("RGB")

    # Gentle edits that are more likely to preserve the watermark
    brightness = ImageEnhance.Brightness(img)
    img = brightness.enhance(1.05)   # slightly brighter

    contrast = ImageEnhance.Contrast(img)
    img = contrast.enhance(1.08)     # slightly more contrast

    color = ImageEnhance.Color(img)
    img = color.enhance(1.03)        # very small color change

    # Save as JPG with high quality
    img.save(EDITED_IMAGE, quality=95)

    print(f"Saved edited image as: {EDITED_IMAGE}")


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    print("=== B30 Watermark Test ===")

    # Check file exists
    if not Path(INPUT_IMAGE).exists():
        raise FileNotFoundError(
            f"Put your AI-generated image in this folder and name it '{INPUT_IMAGE}'"
        )

    # Embed watermark
    embed_watermark()

    # Check watermark before editing
    print("\n--- Check watermark before editing ---")
    before = extract_watermark(WATERMARKED_IMAGE)

    # Apply gentle edit
    make_light_edit()

    # Check watermark after editing
    print("\n--- Check watermark after editing ---")
    after = extract_watermark(EDITED_IMAGE)

    print("\n=== RESULT ===")
    if before == WATERMARK_TEXT and after == WATERMARK_TEXT:
        print("Success: the watermark survived the edit.")
    elif before == WATERMARK_TEXT and after != WATERMARK_TEXT:
        print("The watermark was embedded correctly, but it did NOT survive the edit.")
    else:
        print("The watermark was not read correctly even before editing. Try a different image or rerun.")