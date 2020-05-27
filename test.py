import model


def compress():
    args = ['model.py', 'compress', 'pictures/image4.jpg', 'compressed.tfci']
    args = model.parse_args(args)
    model.compress(args)

def decompress():
    args = ['model.py', 'decompress', 'compressed.tfci', 'reconstruction.png']
    args = model.parse_args(args)
    model.decompress(args)

if __name__ == '__main__':
    # compress()

    decompress()
