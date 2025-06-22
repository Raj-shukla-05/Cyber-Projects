from PIL import Image
import argparse

# Function to hide data in an image
def encode_image(input_image_path, output_image_path, secret_message):
    img = Image.open(input_image_path)
    encoded = img.copy()
    width, height = img.size
    index = 0

    # Append delimiter to message to know when to stop during decoding
    secret_message += "#####"

    binary_message = ''.join([format(ord(i), '08b') for i in secret_message])

    for row in range(height):
        for col in range(width):
            if index < len(binary_message):
                pixel = img.getpixel((col, row))
                r, g, b = pixel[:3]  # Handle RGB and RGBA
                r = (r & ~1) | int(binary_message[index])
                index += 1
                encoded.putpixel((col, row), (r, g, b))
            else:
                encoded.save(output_image_path)
                print("[+] Encoding complete. Saved as:", output_image_path)
                return
    encoded.save(output_image_path)
    print("[+] Encoding complete. Saved as:", output_image_path)

# Function to decode data from an image
def decode_image(input_image_path):
    img = Image.open(input_image_path)
    width, height = img.size
    binary_data = ""
    
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            r, g, b = pixel[:3]  # Handle RGB and RGBA
            binary_data += str(r & 1)

    all_bytes = [binary_data[i: i+8] for i in range(0, len(binary_data), 8)]
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "#####":  # Delimiter found
            break
    print("[+] Decoded message:", decoded_data[:-5])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Steganography Tool: Hide and Extract messages in images')
    parser.add_argument('-e', '--encode', nargs=3, metavar=('input', 'output', 'message'),
                        help='Encode a message into an image')
    parser.add_argument('-d', '--decode', metavar='input',
                        help='Decode a message from an image')

    args = parser.parse_args()

    if args.encode:
        input_path, output_path, secret_message = args.encode
        encode_image(input_path, output_path, secret_message)
    elif args.decode:
        input_path = args.decode
        decode_image(input_path)
    else:
        parser.print_help()
