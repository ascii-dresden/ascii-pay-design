from image_creation import create_images
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser('provide csv data')
    parser.add_argument('data', metavar='p', type=str, nargs=1, help="path to csv data")
    parser.add_argument('-d', '--destination', type=str, help="save destination")
    args = parser.parse_args()

    create_images(args.data[0], args.destination)
