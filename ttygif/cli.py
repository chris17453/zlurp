import argparse
from .gif.gif import gif
from .tty.fonts import font

def cli_main():
    parser = argparse.ArgumentParser("ttygif", usage='%(prog)s [options]', description="""tty output to gif""", epilog="Dont yaknow?")

    # actions
    parser.add_argument('-v', '--debug', help='show debuging statistics', action='store_true')
    parser.add_argument('-i', '--input', help='source file', default= None)
    parser.add_argument('-o', '--output', help='destination file', default= None)
    parser.add_argument('-x', '--extract', help='Extract data from gif as json', action='store_true')
    parser.add_argument('-w', '--web', help='Convert a gif to a html canvas web page.', action='store_true')
    parser.add_argument('-s', '--screen', help='Create font html canvas web page.', action='store_true')
    
    args = parser.parse_args()
    if args.web:
        gif().canvas_it(args.input,args.output)
    
    if args.extract:
        gif().extract(args.input,args.output)

    if args.screen:
        gif().screen(font,args.output)
    





if __name__=='__main__':
    cli_main()
