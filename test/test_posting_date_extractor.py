import sys
import time
import os
import unittest

# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

from digExtractor.extractor import Extractor
from digExtractor.extractor_processor import ExtractorProcessor
from digPostingDateExtractor.posting_date_extractor import PostingDateExtractor

class TestDrugUseExtractorMethods(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_price_extractor(self):
        doc = {'content': 'online: Jul 07, 00:44 \n  ', 'b': 'world'}

        extractor = PostingDateExtractor().set_metadata({'extractor': 'drug'})
        extractor_processor = ExtractorProcessor().set_input_fields(['content']).set_output_field('extracted').set_extractor(extractor)
        updated_doc = extractor_processor.extract(doc)
        self.assertEqual(updated_doc['extracted']['value'], '2016-07-07')

    

if __name__ == '__main__':
    unittest.main()



