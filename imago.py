from PIL import Image, ImageFilter
import argparse
import os


def banner():
    print('''
+------------------------------------------+
| imago image manipulater                  |
| imago v.0.1                              |
| Author: Elvin --> elvinsl                |
| Github: https://github.com/elvinsl/imago |
+------------------------------------------+
    ''')


def get_args():
    parser = argparse.ArgumentParser(description='Imago -->> Image manipulater',
                                     epilog='I was hoping for Kenobi, why are you here?')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-i', '--image', dest='image', default=None, help='Image to manipulate',
                       metavar='<image>')
    group.add_argument('-I', '--Ifolder', dest='folder', default=None, help='Image Folder to manipulate',
                       metavar='<image folder>')
    parser.add_argument('-c', '--convert', dest='convert', choices=['1', 'l', 'p', 'rbg', 'lab', 'hsv'],
                        default=None, help='Image convert to execute')
    parser.add_argument('-r', '--resize', dest='size', default=None, help='Resize image',
                        metavar='<(width)x(height)>')
    parser.add_argument('-f', '--filter', dest='filter', choices=['blur', 'sharpen', 'smooth', 'emboss', 'detail'],
                        default=None, help='Image filter to execute')
    parser.add_argument('-o', '--output', dest='output', default=None,
                        help='Output folder for manipulated images', metavar='<output folder>')
    parser.add_argument('-k', '--keep-additional', dest='keep', help='Keep additional images too',
                        action='store_false')
    parser.add_argument('-v', '--verbose', dest='verbose', help='Print additional information',
                        action='store_true')
    values = parser.parse_args()
    return values


def resize(size=None, image=None, ifolder=None, output=None):
    if image:
        if output:
            if not os.path.exists(output):
                if args.verbose:
                    print('Making output directory...')
                os.mkdir(output)
        else:
            output = 'output'
            if not os.path.exists(output):
                if args.verbose:
                    print('Making output directory...')
                os.mkdir(output)
        img_name = image.split('.')[0]
        img = Image.open(image)
        size = (int(size.split('x')[0]), int(size.split('x')[1]))
        resized_img = img.resize(size)
        if args.verbose:
            print(f'Resizing {img_name} to {size}...')
        resized_img.save(f'{output}/{img_name}_resized.png')
        return output
    elif ifolder:
        if output:
            if not os.path.exists(output):
                if args.verbose:
                    print('Making output directory...')
                os.mkdir(output)
        else:
            output = 'output'
            if not os.path.exists(output):
                if args.verbose:
                    print('Making output directory...')
                os.mkdir(output)
        files = os.listdir(ifolder)
        size = (int(size.split('x')[0]), int(size.split('x')[1]))
        for img in files:
            img_name = img.split('.')[0]
            i = Image.open(f'{ifolder}/{img}')
            resized_img = i.resize(size)
            if args.verbose:
                print(f'Resizing {img_name} to {size}...')
            resized_img.save(f'{output}/{img_name}_resized.png')
        return output


def filter_image(filter_option=None, image=None, ifolder=None, output=None):
    filters = {
        'blur': ImageFilter.BLUR,
        'smooth': ImageFilter.SMOOTH,
        'detail': ImageFilter.SMOOTH_MORE,
        'sharpen': ImageFilter.SHARPEN,
        'emboss': ImageFilter.EMBOSS
    }
    if not ifolder:
        if output:
            if not os.path.exists(output):
                if args.verbose:
                    print('Making output directory...')
                os.mkdir(output)
        else:
            output = 'output'
            if not os.path.exists(output):
                if args.verbose:
                    print('Making output directory...')
                os.mkdir(output)
        img_name = image.split('.')[0]
        img = Image.open(image)
        filtered_image = img.filter(filters[filter_option])
        if args.verbose:
            print(f'Filtering {img_name}...')
        filtered_image.save(f'{output}/{img_name}_filtered.png')
        return output
    else:
        images = os.listdir(ifolder)
        if output:
            if not os.path.exists(output):
                if args.verbose:
                    print('Making output directory...')
                os.mkdir(output)
        else:
            output = 'output'
            if not os.path.exists(output):
                if args.verbose:
                    print('Making output directory...')
                os.mkdir(output)
        for image in images:
            try:
                img_name = image.split('.')[0]
                temp_image = Image.open(f'{ifolder}/{image}')
                filtered_image = temp_image.filter(filters[filter_option])
                if args.verbose:
                    print(f'Filtering {img_name}...')
                filtered_image.save(f'{output}/{img_name}_filtered.png')
            except ValueError:
                print(f"Can't use {filter_option} filter")
        return output


def convert_image(convert_to=None, image=None, ifolder=None, output=None):
    if not ifolder:
        if output:
            if not os.path.exists(output):
                if args.verbose:
                    print('Making output directory...')
                os.mkdir(output)
        else:
            output = 'output'
            if not os.path.exists(output):
                if args.verbose:
                    print('Making output directory...')
                os.mkdir(output)
        img_name = image.split('.')[0]
        img = Image.open(image)
        filtered_image = img.convert(convert_to.upper())
        if args.verbose:
            print(f'Converting {img_name}...')
        filtered_image.save(f'{output}/{img_name}_converted.png')
        return output
    else:
        images = os.listdir(ifolder)
        if output:
            if not os.path.exists(output):
                if args.verbose:
                    print('Making output directory...')
                os.mkdir(output)
        else:
            output = 'output'
            if not os.path.exists(output):
                if args.verbose:
                    print('Making output directory...')
                os.mkdir(output)
        for image in images:
            try:
                img_name = image.split('.')[0]
                temp_image = Image.open(f'{ifolder}/{image}')
                filtered_image = temp_image.convert(convert_to.upper())
                if args.verbose:
                    print(f'Converting {img_name}...')
                filtered_image.save(f'{output}/{img_name}_converted.png')
            except ValueError:
                print(f"Can't convert {convert_to}")
        return output


def del_add(input_image=None, input_folder=None, output_folder=None):
    if not output_folder:
        output_folder = 'output'
        org_num = int(len(os.listdir(input_folder)))
    if not input_folder:
        img_len = len(input_image)
        org_num = 1
    else:
        org_num = int(len(os.listdir(input_folder)))
    files = os.listdir(output_folder)
    files.sort(key=len, reverse=True)
    delete_files = files[org_num:]
    for file in delete_files:
        os.remove(f'{output_folder}/{file}')


args = get_args()
output_folder = args.folder
banner()
try:
    if args.size:
        output_folder = resize(args.size, args.image,
                               output_folder, args.output)
    if args.filter:
        output_folder = filter_image(
            args.filter, args.image, output_folder, args.output)
    if args.convert:
        output_folder = convert_image(
            args.convert, args.image, output_folder, args.output)
    if args.keep:
        del_add(args.image, args.folder, args.output)
except FileNotFoundError:
    print('File not found')
