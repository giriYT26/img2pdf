# Img2pdf
img2pdf is a python script that converts images to pdf

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install img2pdf.

```bash
pip install img2pdf
```

## Usage
### If Installed via pip:
- single image -> pdf
   ```bash
  img2pdf --image img01.jpg
  ```
or 
```bash        
img2pdf -i img01.jpg
  ```
- multi image -> pdf
  ```bash
  img2pdf --images img01.jpg img03.jpg img04.jpg
  ```

for all the above code the output pdf name will be named **output.pdf**
- Custom output name
  ```bash
  img2pdf -i img01.jpg -o result.pdf
  ```
### If Installed via github
#### First clone the repo
```bash
git clone https://github.com/giriYT26/img2pdf.git
cd img2pdf
pip install -r requirements.txt
```
- single image
  ```bash
  python img2pdf -i img01.jpg
  ```
- multi image -> pdf
  ```bash
  python img2pdf --images img01.jpg img02.jpg img03.jpg img04.jpg
  ```

for all the above code the output pdf name will be named **output.pdf**
- Custom output name
  ```bash
  python img2pdf -i img01.jpg -o result.pdf
  ```

  ## Supported Formats
- JPG / JPEG
- PNG
- BMP
- TIFF
- WebP

  ## License
  MIT
  ## Author
  Made by [Giridharan](https://github.com/giriYT26)

