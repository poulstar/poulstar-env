import typer
from pathlib import Path
from . import logo
from typing_extensions import Annotated

app = typer.Typer(pretty_exceptions_show_locals=False)


@app.command(help="Put your logo on the images.")
def logo(
    output: Annotated[Path, typer.Argument()] = "output_image.png",
    background: Path = typer.Option(...),
    overlay: Path = typer.Option(...),
):
    if background.exists():
        pass
    else:
        print("background image does not exist.")
        exit()
    if overlay.exists():
        pass
    else:
        print("Overlay image does not exist.")
        exit()
    
    if not output.parent.exists():
        print("Your path does not exist.")
        exit()
    elif output.parent.exists():
        if output.suffix == ".png":
            pass
        else:
            print("Invalid file extension. Only .png files are allowed.")
            exit()

    pos = input(
    """Enter Your Position: 
    rt = right/top
    lt = left/top
    rb = right/bottom
    lb = left/bottom
    ct = center/top
    cb = center/bottom
    cm = center/middle
    """
    )
    logo.merge_images(
        background_path=background,
        overlay_path=overlay,
        output_path=output,
        position=pos,
    )


@app.command()
def poulstar():
    print(f"Poulstar")


if __name__ == "__main__":
    app()
