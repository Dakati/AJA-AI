import os
import easyocr

reader = easyocr.Reader(['en'], gpu=False)


def capture_screen():
    filename = "screen.png"

    os.system(
        'powershell -command "Add-Type -AssemblyName System.Windows.Forms; '
        'Add-Type -AssemblyName System.Drawing; '
        '$bmp = New-Object System.Drawing.Bitmap([System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Width,[System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Height); '
        '$graphics=[System.Drawing.Graphics]::FromImage($bmp); '
        '$graphics.CopyFromScreen(0,0,0,0,$bmp.Size); '
        '$bmp.Save(\'' + filename + '\');"'
    )

    return filename


def read_screen():
    image = capture_screen()

    result = reader.readtext(image, detail=0)

    text = "\n".join(result)

    return text