---
title: Prepare your data
---

# Prepare your data

Before depositing your data in DataverseNO make sure your data set complies with our guidelines below.

## a) File naming and organization

Following good practice for file naming and organizing makes it much easier to find the right data file, not just for you, but also for your collaborators, and later on for other researchers who may re-use your data. Please make sure your file names comply with the following fundamental file naming recommendations:

- Files must be named consistently.
- File names must be descriptive, but short (< 25 characters).
- Do not use spaces. Instead, use underscores (e.g. first_study), hyphens (e.g. first-study) or camel case (FirstStudy).
- Avoid characters like \\ / ? : * " > < | : # % " { } | ^ [ ] ` ~ æÆ øØ åÅ äÄ öÖ …
- Use the international date convention YYYY-MM-DD (e.g. 2017-10-25).
- The name of a file in original file format must be identical with the name of the corresponding file in preferred file format (see below).

The way your files should be organized depends on the file type and the discipline. You should follow best-practice recommendations within your field.

For spreadsheets, which are a common file type within many fields, you should follow these general recommendations:

- One table = one file (one spreadsheet)
- One column = one variable
- One row = one observation / sample
- One cell = one value / piece of information
- The first row is the header including variable names.
- Variable names must not include special characters, spaces, or start with a number.
- Use the international date convention YYYY-MM-DD (e.g. 2017-10-25).

For more general recommendations and tips about best-practice organization of spreadsheets / tabular files, see the chapter Data Organisation in Spreadsheets in The Turing Way handbook to reproducible, ethical and collaborative data science.

## b) Preferred file formats

### What are preferred file formats?

The choice of a preferred file format is crucial in order to ensure that your data will be readable also in the future. Some file formats are more likely to allow long-term readability than others are. Such formats are usually

- non-proprietary
- open, with documented international standards
- using standard character encoding, preferably Unicode (e.g. UTF-8)
- uncompressed (space permitting)

The table below gives an overview of preferred vs. non-preferred file formats for a selection of document types. The list of file formats in the column "Non-preferred file formats" is non-exhaustive and includes the formats considered the ones used most commonly. If your dataset contains file formats not listed here, please contact the support services of your home institution. When uploading your data to the repository, please make sure you add your files in a preferred format. Make also sure that all of your files contain a valid file extension, e.g. .txt, .pdf. If your data cannot be stored in a preferred format, they can still be published in their original format, but in that case, DataverseNO does not commit to preserve the data in the long term. If appropriate, the file may also be archived in their original file format in addition to preferred format(s). The recommended file formats for TROLLing are also listed in the Format Recommendations of the CLARIN Standards Information System.

| File type | Preferred file formats (examples) | Non-preferred file formats (examples) |
|---|---|---|
| Audio | Uncompressed and lossless Wav or AIFF (.wav/.aiff); Compressed and lossless FLAC (.flac) | Compressed and lossy Mp3 (.mp3); AAC (.m4a); Monkey's Audio (.ape); Ogg Vorbis (.ogg); Windows Media Audio (.wma) |
| Container file | In case container files need to be archived as container files, use .zip. See more in section Upload data files. | |
| Image | Uncompressed TIFF (.tif or .tiff); Compressed and lossless PNG (.png) | Compressed and lossy JPEG (.jpg); Scalable Vector Graphics (.svg); Adobe Photoshop (.psd); Apple Picture File (.pct); Graphics Interchange Format (.gif); Raw Image Data File (.raw); Windows Bitmap (.bmp) |
| Slide, illustration | PDF/A (.pdf) combined with original file | PowerPoint (.pptx) |
| Spreadsheet, tabular file | Plain text with Unicode UTF-8 character encoding, tab-separated (.tsv, .txt) or comma-/semicolon-separated (.csv) | Excel (.xlsx) |
| Text | Plain text (.txt); Markdown (.md); If formatting needed: XML, PDF/A (.pdf) combined with original file | Word (.docx) |
| Programming languages | MATLAB (.m, .mat); Python (.py) | |
| Markup language | XML (.xml); HTML (.html); Related files: .css, .xslt, .js, .es | SGML (.sgml); Markdown (.md) |
| Transcription | File format: PDF/A (.pdf) combined with original file; PDF/A (.pdf) combined with Comma/Tab Separated Values (.csv/.txt); Font: Unicode IPA (e.g. Charis SIL, Doulos SIL, Gentium Plus, Andika), ASCII SAMPA | File format: Word (.docx); Excel (.xlsx); Font: Transcription legacy fonts (SIL IPA(93)) |
| Video | MPEG-4 (.mp4) | AVI (.avi); Flash Video (FLV); Quicktime (.mov); Windows Media Video (WMV) |
| Array data | netCDF (.nc) | |
| Statistical analysis | R (.R, .RData) | SPSS (.dat/.sps); STATA (.dat/.DO); SPSS Portable (.por); SPSS (.sav); STATA (.dta); SAS (.7dat, .sd2, .tpt) |
| Qualitative data analysis | Basic data in preferred file format, e.g. PDF/A, plain text in Unicode (.txt); Analysis dump/package as REFI-QDA Project (.qdpx) | The different workspace dump formats, e.g. .nvp, .hpr |
| Workspace dump formats for mass spectrometry | mzML (.mzML) | Agilent D (.D); Bruker BAF (.BAF); Bruker FID (.FID); Chromtech DAT (.DAT); … |

### How to save or convert your data into a preferred file format?

This section contains information on the following document types: Audio, container, image, text, transcription, and video. If your data contain types not listed here, please contact the support services of your home institution.

**Audio:**

- **Recording:** The quality of your audio file depends on the purpose of your recording. If the recording is of such nature that acoustic details are irrelevant, the mp3 format is sufficient. Note however, that mp3 is a lossy compression format: Information in the speech signal is irreversibly discarded during recording and can therefore be considered less suited for speech analysis in the case of data reuse. Given that the mp3-format reduces the reusability of your data, we advise recording in an uncompressed format, .wav or .aiff.
- **Conversion:** If space is an issue, you can convert the uncompressed .wav and .aiff-files after recording. We recommend a format that does not remove information, like FLAC (Free Lossless Audio Codec). Conversion to FLAC is fully reversible, i.e. the original sound file is restored when decompressed. File conversion can easily be done in free software like Audacity (http://web.audacityteam.org/) or Praat (http://www.fon.hum.uva.nl/praat/).

**Container files:**

For packing files into container files, please follow the recommendations below:

- Use container files with extensions .zip (do not use .7z, tar.gz, .rar, and so on).
- Use one of the following tools to pack your files into a container:
    - 7-Zip (for Windows)
    - Keka (for Mac)
- Do not use compression or encryption when packing your files into containers.

**Image:**

- **Compression:** Images are often compressed to reduce the amount of redundant or irrelevant data information. This does not mean that the quality of images is automatically reduced when they are compressed.
- **Conversion:** If your images are stored in a format considered non-preferred (see the section What are preferred file formats? above), they must be converted to JPEG, PNG or TIFF. Conversion can easily be done in the software Paint (Windows), Preview (Mac) or GIMP Image Editor (Linux). There are numerous free image converters.

**Text:**

- **Plain text:** If your data is represented in plain text, requiring little or no formatting, you are recommended to create and save your data as plain text files (.txt). You may use a simple text editor, e.g. gedit, TextEdit or WordPad. If you use a more advanced text editor when structuring your data, e.g. Microsoft Word or LibreOffice Writer, you must still save it in plain text format. To do so, select "Save as file type: Plain text (.txt)" in the menu File > Save As. Also, choose Unicode UTF-8 character encoding.
- **Formatted text:** If your data contains formatted text, e.g. including essential line breaks, tabs, figures, we recommend you to convert your data file into a PDF/A file (.pdf). The original text file as well as the PDF/A file must be uploaded. The same procedure must be carried out if you use a text editor like Microsoft Word or LibreOffice Writer when structuring your data, or a presentation editor like Microsoft PowerPoint or LibreOffice Impress.
    - To create a PDF/A file in Microsoft Word: Mac (2011): Print > PDF > Save as Adobe PDF > Adobe PDF Settings: PDF/A-1b: 2005 (CMYK). Windows (2013): Save as Adobe PDF > File type: PDF files > Options: Create PDF/A-1a: 2005 compatible file
    - To create a PDF/A file in LibreOffice Writer: Linux: Save as PDF > Check the PDF/A-1a box > Export.
    - To save/convert a PDF file as a PDF/A file in Adobe Acrobat (Pro or similar): Save As Other > More Options > PDF/A.
    - To save/convert a PDF file as a PDF/A file in PDFTRON (or similar): Go to https://www.pdftron.com/pdf-tools/pdfa-converter/, scroll down to the Drag and drop files area, choose PDF/A-1A in field 1, and upload your PDF file in field 2.
- **Tabular text:** Tabular text data must be provided as Unicode-encoded text files (.csv/.txt). If you have stored your data in a spreadsheet software like Microsoft Excel or LibreOffice Calc, the following instructions show you how to convert it to a recommended format:
    - Microsoft Excel (Mac, Windows): Choose File > Save as > Choose folder; In the option Save as type, choose Text (Tab delimited) (*.txt) (Note! Do not choose Unicode Text (*.txt)); In Tools, choose Web options; Choose the tab Encoding; In the field Save this document as, choose Unicode (UTF-8), and then click OK; Choose the tab Fonts; In the Character set window, choose Multilingual/Unicode/Other script, and click OK; Click Save; Confirm by clicking Yes. Note: This process has to be repeated for each sheet in the Excel workbook.
    - LibreOffice Calc (Linux, Mac, Windows): Click File > Save As; Linux and Windows: In the data export dialogue window, select Text encoding/Character set: Unicode (UTF-8); Field delimiter: {Tabulator} (= recommended); Text delimiter: none. Mac: In the field File type, select "Text CSV (.csv)". In the data export dialogue window, select Character set: Unicode (UTF-8); Field delimiter: {Tab}; Text delimiter: " (double quotation mark).

**Transcription:**

- **Font:** All transcriptions must be made using Unicode-encoded fonts, e.g. IPA Doulos SIL. For phonetic transcriptions, SAMPA (Speech Assessment Methods Phonetic Alphabet, ASCII characters) is an alternative to IPA. If the recommended font is not available for the type of transcription your dataset requires, it is imperative to include a separate ReadMe file in your dataset with instructions about how to read the transcriptions. Note that the font package itself must not be uploaded, given copyright restrictions.
- **Conversion:** If your videos are stored in a format considered non-preferred (see the section What are preferred file formats? above), these must be converted to the MPEG-4 format. If you do not have license to any professional conversion software, we advise you to use the VLC Media Player (standard application on both Mac and Windows), or an online free image converter.

**Workspace/analysis space:**

- **Statistical analysis software, e.g. Matlab, R, S-Plus, SPSS:** Most softwares for statistical analysis allow you to save the basic data as (or export them to) a plain text format (.txt). In addition, you must copy the script, and save it as plain text in a text editor.
- **Qualitative analysis software, e.g. ATLAS.ti, NVivo:** Some software packages for qualitative analysis allow you to save the basic data (or export them to) a preferred file format, e.g. PDF/A or plain text format (.txt). In addition, you can export the analysis package as a so-called REFI-QDA Project (.qdpx). In NVivo, this may be done in the following way: Click the menu tab Share, and then click Export Project. In the pop-up window, select REFI-QDA Project, and choose Location, i.e. where you want to save the file, and enter the filename.
- **Software for mass spectrometry:** Guidelines on how to convert .mid files to .mzML can be found here. If you are unfamiliar with the command line in Windows, please contact user support at your home institution.

## c) How to describe your data

In order for other researchers to be able to understand and reuse your data, it is essential that you describe them in a comprehensible and consistent manner before they are published. In DataverseNO, this kind of documentation must be provided in two ways, in the metadata fields, and in a separate ReadMe file which must be uploaded together with your data files:

### Metadata

Metadata is information about your data which makes them findable in discovery services. When creating a dataset, it is therefore important to fill in as much information as possible in the metadata schema (see the sections Enter metadata and Enter more metadata in the Deposit Guidelines.

### ReadMe file

A ReadMe file is a more detailed user guide to your dataset so that other researchers are able to interpret, understand, and reuse your data, including information about how the dataset was created, how complete it is, and what kind of restrictions it has.

For your dataset to be curated and published in DataverseNO or TROLLing, it is mandatory to build your ReadMe file based on this general template. For dataset containing only software code or code-based data, you may use this template for software code.

If these templates are not appropriate for your dataset, please consult with the support services of your home institution and build your own ReadMe file. The ReadMe file must minimally contain the following:

- Title of the dataset, DOI, contact information
- Methods
- Data and file overview
- Data-specific information
- Terms of Reuse

The ReadMe file should be in plain text format with Unicode UTF-8 character encoding (.txt). If you need to illustrate or format your description, you may save your ReadMe file as PDF/A (see the section What are preferred file formats? for more information). We also recommend you to add "0_" in front of the ReadMe file name (e.g. "0_ReadMe.txt"), which will make the file appear on the top of the file overview.

Here are some sample ReadMe files: sample 1 (Social Sciences); sample 2 (Life Sciences).

## d) File size, number of files, and folder structure

Check out our guidelines on file size, number of files, and folder structure before uploading files to your dataset.

## e) Acknowledgements

Parts of the guidelines above have been adapted from several sources, including:

- Data Management General Guidance. Curation Center of the California Digital Library, University of California. https://dmptool.org/dm_guidance#types.
- Praat beginners' manual by Sidney Wood. http://www.fon.hum.uva.nl/praat/manualsByOthers.html
- Preparing tabular data for description and archiving. Research Data Management Group, Cornell University. http://data.research.cornell.edu/content/tabular-data.
- Recommendations for uploading data. ETH-Bibliothek. http://www.library.ethz.ch/en/content/download/17058/442689/version/2/file/Empfehlungen_Datenupload_en.pdf
- Sustainable Formats and Conversion Strategies at the Bentley Historical Library. Version 1.0, November 9th, 2011. http://bentley.umich.edu/dchome/resources/BHL_PreservationStrategies_v01.pdf.

For questions, comments or suggestions, see our support page.

Proceed to section 2: Deposit your data
