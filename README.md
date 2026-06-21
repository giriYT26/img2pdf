# Img2PDF

**Img2PDF** is a Python command-line tool that converts one or more images into a PDF file.

## Installation

Install using pip:

```bash
pip install img2pdf
```

## Usage

### If Installed via pip

#### Convert a Single Image to PDF

```bash
img2pdf --image img01.jpg
```

or

```bash
img2pdf -i img01.jpg
```

#### Convert Multiple Images to PDF

```bash
img2pdf --images img01.jpg img02.jpg img03.jpg
```

By default, the generated PDF will be saved as **output.pdf**.

#### Specify a Custom Output Filename

```bash
img2pdf -i img01.jpg -o result.pdf
```

---

### If Installed from GitHub

#### Clone the Repository

```bash
git clone https://github.com/giriYT26/img2pdf.git
cd img2pdf
pip install -r requirements.txt
```

#### Convert a Single Image to PDF

```bash
python img2pdf.py -i img01.jpg
```

#### Convert Multiple Images to PDF

```bash
python img2pdf.py --images img01.jpg img02.jpg img03.jpg
```

By default, the generated PDF will be saved as **output.pdf**.

#### Specify a Custom Output Filename

```bash
python img2pdf.py -i img01.jpg -o result.pdf
```

## Supported Image Formats

* JPG / JPEG
* PNG
* BMP
* TIFF
* WebP

## License

This project is licensed under the MIT License.

## Author

Created and maintained by Giridharan.

GitHub: https://github.com/giriYT26
