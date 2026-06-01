'''
Resume Logger Module
Appends one row to an Excel workbook each time a custom resume is applied.

Columns:
  Date Applied | Company | Job Title | Resume File (Resume_Company.pdf) |
  Projects Used | Job Description Snippet

The Excel file auto-creates on first run with styled headers.
'''

import os
from datetime import datetime
from modules.helpers import print_lg

try:
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    _OK = True
except ImportError:
    _OK = False
    print_lg("ResumeLogger: 'openpyxl' not installed. Run: pip install openpyxl")


_HEADERS    = ["Date Applied", "Company", "Job Title",
               "Resume File (click to open)", "Projects Used",
               "Job Description (Snippet)"]
_COL_WIDTHS = [22, 28, 35, 60, 70, 60]
_HDR_COLOR  = "1F4E79"   # dark blue header
_ALT_COLOR  = "D6E4F0"   # light blue alternate rows


def log_resume_application(
    company: str,
    job_title: str,
    resume_path: str,
    selected_projects: list,
    job_description: str = "",
    log_path: str = "all excels/resume_log.xlsx"
) -> None:
    '''
    Appends one application row to the Excel resume log.
    Creates the file with styled headers if it does not exist.
    '''
    if not _OK:
        return

    try:
        log_dir = os.path.dirname(log_path)
        if log_dir:
            os.makedirs(log_dir, exist_ok=True)

        if os.path.exists(log_path):
            wb = openpyxl.load_workbook(log_path)
            ws = wb.active
        else:
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.title = "Resume Log"
            _write_header(ws)

        row_idx = ws.max_row + 1
        abs_path = os.path.abspath(resume_path) if resume_path else "Default resume"

        row_data = [
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            company or "Unknown",
            job_title or "Unknown",
            abs_path,
            ", ".join(selected_projects) if selected_projects else "Default resume used",
            (job_description or "")[:400],
        ]

        thin = Border(
            left=Side(style="thin"), right=Side(style="thin"),
            top=Side(style="thin"), bottom=Side(style="thin")
        )
        fill = PatternFill(start_color=_ALT_COLOR, end_color=_ALT_COLOR,
                           fill_type="solid") if row_idx % 2 == 0 else None

        for col_idx, value in enumerate(row_data, start=1):
            cell = ws.cell(row=row_idx, column=col_idx, value=value)
            cell.border = thin
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            if fill:
                cell.fill = fill

        # Keep column widths at least at defined minimums
        for col_idx, width in enumerate(_COL_WIDTHS, start=1):
            letter = ws.cell(row=1, column=col_idx).column_letter
            ws.column_dimensions[letter].width = max(
                ws.column_dimensions[letter].width or 0, width
            )

        wb.save(log_path)
        print_lg(f"ResumeLogger: ✅ Logged row {row_idx} → {log_path}")
        print_lg(f"ResumeLogger:    Resume: {abs_path}")

    except Exception as e:
        print_lg(f"ResumeLogger: Failed — {e}")


def _write_header(ws) -> None:
    hdr_fill  = PatternFill(start_color=_HDR_COLOR, end_color=_HDR_COLOR, fill_type="solid")
    hdr_font  = Font(color="FFFFFF", bold=True, size=11)
    hdr_align = Alignment(horizontal="center", vertical="center", wrap_text=True)
    thin      = Border(
        left=Side(style="thin"), right=Side(style="thin"),
        top=Side(style="thin"), bottom=Side(style="thin")
    )
    for col_idx, (header, width) in enumerate(zip(_HEADERS, _COL_WIDTHS), start=1):
        cell = ws.cell(row=1, column=col_idx, value=header)
        cell.fill      = hdr_fill
        cell.font      = hdr_font
        cell.alignment = hdr_align
        cell.border    = thin
        ws.column_dimensions[cell.column_letter].width = width
    ws.row_dimensions[1].height = 25
    ws.freeze_panes = "A2"
