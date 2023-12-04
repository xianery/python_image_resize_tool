import PIL
from PIL import Image
import PySimpleGUI as gui
import os

def resize(file, resampling, multiplier):
    with Image.open(file) as img:

        # width, height = img.size
        # width, height = width * multiplier, height * multiplier

        width, height = int(img.width * multiplier), int(img.height * multiplier)
        resized_image = img.resize((width, height), resample=resampling)
        return resized_image


def main():
    gui.theme('Dark Gray 13')
    layout_menu = [
        [gui.Text('Photo path'), gui.InputText(f"{os.getcwd()}" + "\photo.jpg"), gui.FileBrowse()],
        [gui.Text('Output file'), gui.InputText(f"{os.getcwd()}" + "\photo_resized.jpg"), gui.FileBrowse()],
        [gui.Text('Resample type'), gui.Combo(['Nearest', 'Box', 'Bilinear', 'Bicubic', 'Lanczos'], size=(15,10), default_value='<select>'), 
         gui.Text('Multiplier of resize'), gui.Slider(range=(.1,4.0), default_value=.1, resolution=.1, size=(20,10), orientation='horizontal')],
        [gui.Button('Resize', key='resize_ready')]
    ]
    
    window = gui.Window('Pillow Resize Tool', layout_menu)

    while True:
        event, values = window.read()

        try:
            input_file = values[0]
            output_file = values[1]
            resample_type = values[2]
            multiplier_resize = values[3]
            flag_complete = False
            
            if event == 'resize_ready':
                if resample_type == 'Nearest':
                    resize(input_file, Image.Resampling.NEAREST, multiplier_resize).save(output_file)
                    flag_complete = True
                elif resample_type == 'Box':
                    resize(input_file, Image.Resampling.BOX, multiplier_resize).save(output_file)
                    flag_complete = True
                elif resample_type == 'Bilinear':
                    resize(input_file, Image.Resampling.BILINEAR, multiplier_resize).save(output_file)
                    flag_complete = True
                elif resample_type == 'Bicubic':
                    resize(input_file, Image.Resampling.BICUBIC, multiplier_resize).save(output_file)
                    flag_complete = True
                elif resample_type == 'Lanczos':
                    resize(input_file, Image.Resampling.LANCZOS, multiplier_resize).save(output_file)
                    flag_complete = True
                elif resample_type == '<select>':
                    gui.popup("Resample type isn't selected")
                    continue
            if flag_complete:
                gui.popup('Done!')
        except PIL.UnidentifiedImageError as image_unknown_error:
            gui.popup("Thats Isn't image")
        except FileNotFoundError as file_error:
            if "No such file or directory" in str(file_error):
                gui.popup("File isn't selected")
        except SyntaxWarning as syntax_warn:
            pass
        except PermissionError as permission_error:
            gui.popup(permission_error)
        except ValueError as value_error:
            gui.popup(value_error)
        except AttributeError as _:
            gui.popup('Some fields are empty')
        except TypeError as _:
            pass

        if event == gui.WIN_CLOSED:
            print('Window closed')
            break

    window.close()

if __name__ == "__main__":
    main()