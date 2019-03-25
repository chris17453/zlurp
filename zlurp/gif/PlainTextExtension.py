class PlainTextExtension:
    def __init__(self,stream):
        self.Introducer= stream.byte(value=0x21)         # Extension Introducer (always 21h) 
        self.Label= stream.byte(value=0x01)              # Extension Label (always 01h) 
        self.BlockSize= stream.byte(value=0x0C)          # Size of Extension Block (always 0Ch) 
        self.TextGridLeft= stream.word()                 # X position of text grid in pixels 
        self.TextGridTop= stream.word()                  # Y position of text grid in pixels 
        self.TextGridWidth= stream.word()                # Width of the text grid in pixels 
        self.TextGridHeight= stream.word()               # Height of the text grid in pixels 
        self.CellWidth= stream.byte()                    # Width of a grid cell in pixels 
        self.CellHeight= stream.byte()                   # Height of a grid cell in pixels 
        self.TextFgColorIndex= stream.byte()             # Text foreground color index value 
        self.TextBgColorIndex= stream.byte()             # Text background color index value 
        self.plainTextData= stream.byte(eod=0x00)        # The Plain Text data 
        self.Terminator= stream.byte(value=0x00)         # Block Terminator (always 0) 


    def debug():
        
        print("Plain Text Extension Block")

        print(" Introducer: {0}".format(self.Introducer))
        print(" Label: {0}".format(self.Label))
        print(" BlockSize: {0}".format(self.BlockSize))
        print(" TextGridLeft: {0}".format(self.TextGridLeft))
        print(" TextGridTop: {0}".format(self.TextGridTop))
        print(" TextGridWidth: {0}".format(self.TextGridWidth))
        print(" TextGridHeight: {0}".format(self.TextGridHeight))
        print(" CellWidth: {0}".format(self.CellWidth))
        print(" CellHeight: {0}".format(self.CellHeight))
        print(" TextFgColorIndex: {0}".format(self.TextFgColorIndex))
        print(" TextBgColorIndex: {0}".format(self.TextBgColorIndex))
        print(" plainTextData: {0}".format(self.plainTextData))
        print(" Terminator: {0}".format(self.Terminator))
