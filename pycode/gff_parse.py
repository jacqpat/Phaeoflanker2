'''
Written by Patrick Jacques the 5th of April 2022

parse a GFF file
'''

class Gene:
    def __init__(self,gff_array):
        self.sequence = gff_array[0]
        self.source = gff_array[1]
        self.element = gff_array[2]
        self.start = gff_array[3]
        self.end = gff_array[4]
        self.score = gff_array[5]
        self.brin = gff_array[6]
        self.phase = gff_array[7]
        self.attributes = self.attributes_parser(gff_array[8])
    def attributes_parser(self,attributes):
        attr = {}
        attr_1 = attributes.split(';')
        for a in attr_1:
            b = a.split('=')
            attr[b[0]] = b[1]
        return attr
    def resume(self):
        print(self.element,':',self.sequence,':',self.start,'-',self.end)
        for k,v in self.attributes.items():
            print(k,':',v)
        print('\n')
    def taille(self):
        return (int(self.end) - int(self.start))
        
