from PIL import Image, ImageDraw, ImageFont
import csv
import qrcode


def create_images(data_path, destination):
    # banner values
    banner_top = 527
    banner_start = 47
    banner_color = (241, 239, 218)
    # shadow values
    shadow_color = (217, 216, 197)
    shadow_thickness = 12
    # text/font values
    text_color = (77, 77, 77)
    font_size = 39
    size_inc_per_char = 23
    name_text_pos = (70, 540)
    number_text_pos = (70, 597)
    max_name_length = 32
    # pin values
    pin_color = (226, 222, 101)
    pin_size = 10
    # qr code values
    qr_pos = 63
    # set save destination
    save_destination = destination
    if save_destination is None:
        save_destination = "./images/results/"

    with open(data_path) as csvFile:
        data = csv.reader(csvFile)
        for row in data:
            name = str(row[0]).strip()
            name_len = len(name)
            # skip row if name is to long
            if name_len > max_name_length:
                print("Name '{}' is to long! Choose a name with 33 or less chars".format(name))
                continue

            # skip row if number does not contain 16 numbers
            number = str(row[1]).replace(' ', '')
            if len(number) < 16 or not number.isdigit():
                print("id '{}' is not valid".format(number))
                continue

            # min width of banner
            banner_width = 535

            # increase the size of banner if needed
            if name_len > 19:
                overflow = name_len - 19
                banner_width += overflow * size_inc_per_char

            # get the base image
            base = Image.open("./images/ascii_pay_neu_empty.png")
            base_size = base.size
            # create draw context
            draw = ImageDraw.Draw(base)
            # create font
            font = ImageFont.truetype("./data/ttf/JetBrainsMono-Regular.ttf", font_size)

            # create the qrcode
            qr_code = qrcode.QRCode(box_size=5, border=0)
            qr_code.add_data("https://pay.ascii.coffee/?code={}".format(number))
            qr_file = qr_code.make_image()
            qr_file.save("./images/qr-codes/qr-{}.png".format(number))

            # insert qr-code
            qr_img = Image.open("./images/qr-codes/qr-{}.png".format(number))
            base.paste(qr_img, (qr_pos, qr_pos))

            # draw banner
            draw.rectangle((banner_start, banner_top, banner_width, base_size[1]), fill=banner_color)
            # draw shadow
            draw.rectangle((banner_start, banner_top, banner_width, banner_top + shadow_thickness),
                           fill=shadow_color)
            # draw pins
            draw.ellipse((banner_start + shadow_thickness, banner_top + shadow_thickness, banner_start +
                          shadow_thickness + pin_size, banner_top + shadow_thickness + pin_size), fill=pin_color)
            draw.ellipse((banner_width - shadow_thickness - pin_size, banner_top + shadow_thickness, banner_width -
                          shadow_thickness, banner_top + shadow_thickness + pin_size), fill=pin_color)

            # draw name and number
            display_num = number[:4] + ' ' + number[4:8] + ' ' + number[8:12] + ' ' + number[12:16]
            draw.text(name_text_pos, name, font=font, fill=text_color)
            draw.text(number_text_pos, display_num, font=font, fill=text_color)

            # save new img
            name_save_str = name.replace(' ', '_')
            base.save("{dest}{name}_{number}.png".format(dest=save_destination , name=name_save_str, number=number))
