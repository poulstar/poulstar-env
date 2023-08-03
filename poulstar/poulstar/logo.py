from PIL import Image


def merge_images(background_path, overlay_path, output_path, position):
    background = Image.open(background_path)

    overlay = Image.open(overlay_path)

    overlay_width, overlay_height = overlay.size
    max_width = background.width // 4
    max_height = background.height // 4
    if overlay_width > max_width or overlay_height > max_height:
        ratio = max(max_width / overlay_width, max_height / overlay_height)
        overlay = overlay.resize(
            (int(overlay_width * ratio), int(overlay_height * ratio))
        )

    if position == "rt":
        position = (background.width - overlay.width, 0)
    elif position == "lt":
        position = (0, 0)
    elif position == "rb":
        position = (
            background.width - overlay.width,
            background.height - overlay.height,
        )
    elif position == "lb":
        position = (0, background.height - overlay.height)
    elif position == "ct":
        position = (int(background.width / 2 - overlay.width / 2), 0)
    elif position == "cb":
        position = (
            int(background.width / 2 - overlay.width / 2),
            background.height - overlay.height,
        )
    elif position == "cm":
        position = (
            int(background.width / 2 - overlay.width / 2),
            int(background.height / 2 - overlay.height / 2),
        )
    else:
        print("error: unknown position")
        exit()

    background.paste(overlay, position, overlay)

    background.save(output_path)
