from math import ceil


class File2YoutubeVideo:

    def __init__(self, args):
        self.bin_array = []
        self.args: dict = {args[i]: args[i + 1] for i in range(0, len(args), 2)}
        self.input_file = self.args['-i']
        self.output_file = self.args['-o']

    def file2array(self):
        with open(file=self.input_file, mode='rb') as input_file:
            input_file = input_file.read().hex()
            for i in range(ceil(len(input_file) / 4)):
                self.bin_array.append(f"{int(input_file[i * 4: i * 4 + 4], 16):0>16b}")
        

if __name__ == '__main__':
    input_str = "-i /home/godfather/Program/File2YoutubeVideo/What-is-Alcohol-by-Volume-or-ABV.jpg -o sweet_beer".split()
    f2yv = File2YoutubeVideo(input_str)
    f2yv.file2array()
    print(f2yv.bin_array)
