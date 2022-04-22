'''
Written by Patrick Jacques the 21rst of April 2022

class for expression data of a gene
'''

class Expression:
    def __init__(self, expr_array):
        self.name = expr_array[0]
        self.length = expr_array[1]
        self.effective_length = expr_array[2]
        self.tpm = expr_array[3]
        self.number_of_reads = expr_array[4]
    def get_name(self):
        return self.name
    def get_length(self):
        return self.length
    def get_tpm(self):
        return self.tpm
    def get_nbr_reads(self):
        return self.number_of_reads