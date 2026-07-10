---
title: Files
---

# Files

Curation checklist for files:

- **Number of files:** Datasets containing more than 300 files cannot be published due to capacity issues with file DOI activation at DataCite. If more files need to be deposited, there are two alternatives:
    - Pack the files into one or more (max. 300) container files.
    - Distribute the data files across multiple (sub-)datasets.

- Is the dataset documented in a ReadMe file? Note! This is an absolute requirement. We recommend researchers using our ReadMe file template. The ReadMe file name must contain the string "readme" (in small and/or capital letters), and not split between the file name and the extension, thus e.g. "ReadMe.txt", and not "Read.me").

- Is forced numbering applied to the ReadMe file (e.g. "0_ReadMe.txt"), so that it appears on the top of the file overview?

- Can the files be opened?

- Are the file names consistent and understandable?

- Are the data provided in (a) preferred file format(s)? Consult the list of preferred file formats in the deposit guidelines. If the file type is not on this list, have a look in the folder Filformat in the channel Langtidsbevaring in the DataverseNO-brukarforum Teams and check whether a file format assessment has been carried out for the file type/format. If not, consult other resources for help, such as DANS file format list, the Library of Congress information pages on file formats, and the UK National Archive's PRONOM service. If you are unsure about the file format, contact DataverseNO at support@dataverse.no. If the data cannot be stored in a preferred format, they can still be published, but with the restrictions this implies for long-term preservation (cf. DataverseNO Preservation Policy). New preferred file formats should be discussed in the curator group. Contact DataverseNO at support@dataverse.no in case you want a new file format to be included on the DataverseNO list of preferred formats. NB! Container files are not preferred. In a new version of Dataverse, folders are retained at file upload, and there is therefore no need for container files anymore.

- If appropriate, the data files may also be archived in the original file format(s) in addition to preferred format(s).

- Do all files have a file extension, e.g. .txt, .pdf?

- If data is uploaded in both the original and a preferred format, the file name of the original file must be identical with the file name in the preferred format. (Otherwise, creating file overviews for long-term preservation will be very difficult.)

- File names must not contain spaces, commas and other special characters.

- If an embargo is applied to one or more data files, the curator must ensure that:
    - The ReadMe file is not embargoed as it must always remain openly accessible.
    - The embargo is properly justified as DataverseNO is a repository for open research data. A valid reason for an embargo is if the data file(s) contain commercially valuable information, such that immediate open access could harm the commercial interests of the depositor and complicate IP protection. If the depositor provides a different reason, the curator should consult the DataverseNO User Forum. Note that embargo is a temporary restriction, not a substitute for permanent restricted or controlled access. Thus, if the depositor's reason for embargo requires permanent restricted or controlled access (e.g., the files contain personal data), the files should not be published at DataverseNO.
    - The depositor has understood that the embargo will end automatically at the specified end date and if changes are required, they must contact the support services of their home institution. Embargos can last for a maximum of two years.

**File size:**

DataverseNO has no upper size limit for a dataset. However, below is some advice and procedures for handling uploads of large files.

A file upload can consist of several files. If a user must split the files on several uploads this can be done by saving the dataset after each upload.

The following advice, size limits and procedures apply to single files, file uploads and datasets:

- The size of individual files should not exceed 100 GB. Bigger files can create problems for others when it comes to downloading and reusing data.
- A file upload should not exceed 200 GB in total size to minimize the likelihood that errors will occur when transmitting the data.
- If the files in a dataset are more than 200 GB in total, the handling of the dataset must be agreed on and scheduled with UiT. The curator agrees/clarifies with the researcher and with UiT at support@dataverse.no.

You can find detailed information on file naming conventions, preferred file formats, and documentation of research data in the section Prepare your data for depositing in the menu item Deposit. There, you will also find detailed guidance on how to save/convert different document types into preferred file formats. If you have questions about this, please contact the support services of your home institution.

Best practice implies saving tabular data as tabulator-separated plain text files, encoded in Unicode UTF-8 without so-called BOM ('Byte Order Mark'). If this is not possible within the spreadsheet software, you may do this in Notepad++ as described here:

1. Open the (converted) text file (.txt) in Notepad++ (Notepad++ is based on open source code, and may be downloaded from https://notepad-plus-plus.org/. Ask IT support at your institution for help to install the software on your computer).
2. Click Encoding in the top menu, and select Convert to UTF-8 without BOM.
3. Save the file.

**Statistics data (e.g. R and SPSS)**

A useful overview of file formats that are used in various statistics programs is available here. As for R, their conclusion is as follows:

> In conclusion, if you are working with R you should provide a .csv* file which includes your data and separate .R- or .Rmd-files which include your syntax to ensure long-term availability. Additionally, you may add Rdata-files for easier access to the same information.

(* We recommend tabulator-separated Unicode UTF-8 .txt.)

The script is in the .R files. .R-files are plain text files (the .R extension may be replaced by .txt). .Rmd: RMarkdown files are a great way to combine data documentation, data visualization and data analysis in one single file.

In other words, we want this:

- Basic data as tabulator-separated Unicode UTF-8 text files (.txt) = preferred file format
- The R code as Unicode UTF-8 (.R) = preferred file format
- .rda = non-preferred file format, but works in R, which is an open source based and openly documented software
- Possibly .rmd
