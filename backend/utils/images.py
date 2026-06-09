from io import BytesIO
from django.core.files.base import ContentFile
from django.utils.text import slugify
from PIL import Image
import uuid


def crop_image(
    image_file,
    target_width,
    target_height,
    quality=85,
):
    image_file.seek(0)

    img = Image.open(image_file)

    if img.mode not in ("RGB", "RGBA"):
        img = img.convert("RGB")

    original_width, original_height = img.size

    target_ratio = target_width / target_height
    original_ratio = original_width / original_height

    # image too wide
    if original_ratio > target_ratio:
        new_width = int(original_height * target_ratio)
        left = (original_width - new_width) // 2

        img = img.crop((
            left,
            0,
            left + new_width,
            original_height
        ))

    # image too tall
    else:
        new_height = int(original_width / target_ratio)
        top = (original_height - new_height) // 2

        img = img.crop((
            0,
            top,
            original_width,
            top + new_height
        ))

    img = img.resize(
        (target_width, target_height),
        Image.LANCZOS
    )

    buffer = BytesIO()

    img.save(
        buffer,
        format="WEBP",
        quality=quality
    )

    buffer.seek(0)

    filename = f"{uuid.uuid4().hex}.webp"

    return ContentFile(buffer.read(), name=filename)