import argparse
from .gif.gif import gif
from .gif.encode import encode_gif
from .tty.fonts import font
from .tty.viewer import viewer 
from .asciicast.reader import asciicast_reader
from .cast2gif import cast2gif
import pprint
import time

def cli_main():
    parser = argparse.ArgumentParser("ttygif", usage='%(prog)s [options]', description="""tty output to gif""", epilog="Dont yaknow?")

    # actions
    parser.add_argument('-v', '--debug',   help='show debuging statistics', action='store_true')
    parser.add_argument('-i', '--input',   help='source file', default= None)
    parser.add_argument('-o', '--output',  help='destination file', default= None)
    parser.add_argument('-x', '--extract', help='Extract data from gif as json', action='store_true')
    parser.add_argument('-w', '--web',     help='Convert a gif to a html canvas web page.', action='store_true')
    parser.add_argument('-s', '--screen',  help='Create font html canvas web page.', action='store_true')
    parser.add_argument('-t', '--test',    help='test viewer', action='store_true')
    

    args = parser.parse_args()
    if args.web:
        gif().canvas_it(args.input,args.output)
    
    if args.extract:
        gif(debug=None).extract(args.input,args.output)

    if args.screen:
        gif().screen(font,args.output)
    

    if args.test:
        cast2gif(args.input,args.output)
                    

if __name__=='__main__':
    cli_main()
