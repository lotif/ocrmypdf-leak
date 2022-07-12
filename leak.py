from memory_profiler import profile
import ocrmypdf
import pikepdf
import tempfile


@profile
def ocr(test_doc):
    opts = {
        "output_type": "pdf",
        "pdf_renderer": "auto",
        "force": True,
    }
    ocrmypdf.ocr(test_doc, "result.pdf", **opts)


if __name__ == "__main__":
    test_docs = ["nasa_early_years.pdf", "short-test.pdf", "test_2pg.pdf", "2011.13534.pdf", "2207.04064.pdf"]
    i = 0
    while True:
        i = i + 1 if i < 2 else 0
        test_doc = test_docs[i]

        rdr = pikepdf.Pdf.open(test_doc)
        writer = pikepdf.Pdf.new()
        for page in rdr.pages:
            with tempfile.NamedTemporaryFile("wb") as fp:
                writer.pages.append(page)
                writer.save(fp)
                ocr(fp.name)
