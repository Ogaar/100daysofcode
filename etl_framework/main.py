from extractor import Extractor
from loader import Loader

extractor = Extractor("sqlite")
extracted_file = extractor.extract()

loader = Loader("csv")
loader.load(extracted_file)
