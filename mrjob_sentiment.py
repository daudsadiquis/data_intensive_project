from mrjob.job import MRJob
from mrjob.protocol import TextValueProtocol

class Sentiment140ToCSV(MRJob):
    OUTPUT_PROTOCOL = TextValueProtocol

    def mapper(self, _, line):
        # Split the line by endline delimiter
        fields = line.split(',')

        # Extract the desired fields
        f1 = fields[0]
        f2 = fields[1]
        f3 = fields[2]
        f4 = fields[3]
        f5 = fields[4]
        f6 = fields[5]

        # Emit the extracted fields as key-value pairs
        yield None, (f1, f2, f3, f4, f5, f6)

    def reducer(self, _, values):

        # Emit the values separated by commas
        for fields in values:
            yield None, ','.join(fields)

if __name__ == '__main__':
    Sentiment140ToCSV.run()
