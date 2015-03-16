# PDFextract

PDFextract is a convenient CLI-wrapper for pdftk which enables the user to easily extract
multiple pages (consecutively or discontinuous) from a given source PDF file.
PDFextract saves the extracted artifacts as individual target PDF files (one for
each page range) or combines them into a single target PDF.

# Dependencies

pdftk must be installed on your system, otherwise PDFextract will fail to execute.

# Installation

Clone the repository, then install the script by executing

```
$ python setup.py install
```

# Examples

1. Extract pages from a single, continuous page range (pages 3 to 5) from source.pdf and save the output to target.pdf.


	```
	pdfextract source.pdf target.pdf 3-5
	```

2. Extract pages from discontinuous page ranges (pages 3 to 5 and 7 to 12) from source.pdf and save the output to target.pdf. This will automatically yield several target PDFs, each suffixed with the respective page range.

	```
	pdfextract source.pdf target.pdf 3-5,7-12
	```

3. Extract pages from discontinuous page ranges (pages 3 to 5 and 7 to 12) from source.pdf and save the output to a single target.pdf.

	```
	pdfextract source.pdf target.pdf 3-5,7-12 --join
	```

# License

This script is released under the MIT license.
