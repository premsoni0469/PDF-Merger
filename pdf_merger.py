import streamlit as st
from PyPDF2 import PdfMerger
import io

st.set_page_config(page_title="PDF Merger", page_icon="📄")
st.title("📄 PDF Merger App")
st.write("Upload PDF files in the **exact order** you want them merged (top to bottom = first to last).")

uploaded_files = st.file_uploader(
    "Upload PDF files", 
    type="pdf", 
    accept_multiple_files=True
)

if uploaded_files:
    st.write(f"Total files uploaded: **{len(uploaded_files)}**")
    st.markdown("### 🧾 Merge Queue (Top ➡️ Bottom):")

    # Show each file in a vertical list (like a queue)
    for idx, file in enumerate(uploaded_files, start=1):
        st.write(f"**{idx}.** 📄 {file.name}")

    if st.button("🔗 Merge PDFs"):
        try:
            merger = PdfMerger()
            for pdf_file in uploaded_files:
                merger.append(pdf_file)

            output_pdf = io.BytesIO()
            merger.write(output_pdf)
            merger.close()
            output_pdf.seek(0)

            st.success("🎉 PDFs merged successfully!")
            st.download_button(
                label="📥 Download Merged PDF",
                data=output_pdf,
                file_name="merged_output.pdf",
                mime="application/pdf"
            )
        except Exception as e:
            st.error(f"❌ Error while merging PDFs: {e}")
else:
    st.info("Upload multiple PDF files to begin.")
