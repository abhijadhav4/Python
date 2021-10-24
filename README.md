# PyPDFForm

PyPDFForm is a pure Python library for PDF form processing. 
It allows filling a PDF form programmatically by creating 
a Python dictionary with keys matching its annotated names 
for elements like text fields and checkboxes. It also supports other functionalities such as 
drawing image and merging multiple PDFs together.

## Installing

Install using [pip](https://pip.pypa.io/en/stable/quickstart/):

```shell script
pip install PyPDFForm
```

## Quick Example

A sample PDF form can be found [here](https://github.com/chinapandaman/PyPDFForm/blob/master/pdf_samples/v2/sample_template.pdf). Download it and try:

```python
import os

from PyPDFForm import PyPDFForm2

PATH_TO_DOWNLOADED_SAMPLE_PDF_FORM = os.path.join(
    os.path.expanduser("~/Downloads"), "sample_template.pdf"
)  # Change this to where you downloaded the sample PDF form

PATH_TO_FILLED_PDF_FORM = os.path.join(
    os.path.expanduser("~"), "output.pdf"
)  # Change this to where you wish to put your filled PDF form

with open(PATH_TO_FILLED_PDF_FORM, "wb+") as output:
    output.write(
        PyPDFForm2(PATH_TO_DOWNLOADED_SAMPLE_PDF_FORM)
        .fill(
            {
                "test": "test_1",
                "check": True,
                "test_2": "test_2",
                "check_2": False,
                "test_3": "test_3",
                "check_3": True,
            },
        )
        .read()
    )
```

After running the above code snippet you can find `output.pdf` at the location you specified, 
and it should look like [this](https://github.com/chinapandaman/PyPDFForm/blob/master/pdf_samples/v2/sample_filled.pdf).

## Documentation

* [API Reference](https://github.com/chinapandaman/PyPDFForm/blob/master/docs/v2/api_reference.md)
* [API Reference (Old)](https://github.com/chinapandaman/PyPDFForm/blob/master/docs/api_reference.md)
* [Examples](https://github.com/chinapandaman/PyPDFForm/blob/master/docs/v2/examples.md)
* [Examples (Old)](https://github.com/chinapandaman/PyPDFForm/blob/master/docs/examples.md)

## PyPDFForm vs PyPDFForm2

PyPDFForm provides additional functionalities like editable support for PDF forms created 
using Adobe Acrobat or Sejda.

PyPDFForm2 supports PDF forms made by a wider range of tools, while discarding some of those additional 
functionalities.

It is strongly advised that you use PyPDFForm2 since only minimum supports will be made to PyPDFForm 
from now on.
