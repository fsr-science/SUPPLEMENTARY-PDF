import tempfile
import unittest
from pathlib import Path

from ocr_compress_pdfs import build_command


class OcrCompressPdfTests(unittest.TestCase):
    def test_command_skips_existing_text_and_uses_compression(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "BOOK.PDF"
            target = Path(temp_dir) / "BOOK_OCR.PDF"
            command = build_command(
                source,
                target,
                language="eng",
                jobs=2,
                quality=70,
                dpi=300,
            )

            self.assertIn("ocrmypdf", command[0])
            self.assertIn("--skip-text", command)
            self.assertIn("--optimize", command)
            self.assertIn("--jpeg-quality", command)
            self.assertEqual(command[-2:], [str(source), str(target)])


if __name__ == "__main__":
    unittest.main()
