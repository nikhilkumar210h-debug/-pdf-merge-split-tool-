import pypdf
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

root.update()
root.attributes('-topmost', True)


print(pypdf.__version__)

try:
    i = int(input("Enter \n1 for merge\n2 for split\n0 to quit\n: "))

    if i == 1:
        files = filedialog.askopenfilenames(
            parent=root,
            title="Select PDFs to merge",
            filetypes=[("PDF Files", "*.pdf")]
        )

        if not files:
            print("No files selected ❌")
        else:
            merge = pypdf.PdfWriter()

            for pdf in files:
                merge.append(pdf)
            r1 = input("Enter file name to save: ")

            with open(r1+".pdf", "wb") as f:
                merge.write(f)

            print("Merge done ✅")

    elif i == 2:
        file = filedialog.askopenfilename(
            parent=root,
            title="Select PDF to split",
            filetypes=[("PDF Files", "*.pdf")]
        )

        if not file:
            print("No file selected ❌")
        else:
            # first 2 pages
            writer1 = pypdf.PdfWriter()
            writer1.append(file, pages=pypdf.PageRange(':2'))
            r2 = input("Enter file name to save: ")

            with open(r2+".pdf", "wb") as f:
                writer1.write(f)

            # last 2 pages
            writer2 = pypdf.PdfWriter()
            writer2.append(file, pages=pypdf.PageRange('-2:'))
            r3 = input("Enter file name to save: ")

            with open(r3+".pdf", "wb") as f:
                writer2.write(f)

            print("Split done ✅")

    elif i == 0:
        print("Have a nice day")

    else:
        print("Invalid choice ❌")

except ValueError:
    print("Invalid input ❗ Please enter a number")
finally:
    root.destroy()