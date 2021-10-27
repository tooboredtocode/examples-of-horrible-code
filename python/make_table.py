def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    return "\n".join((start + mid.join((pad_char * ((padding := column_width - len(str(row[index]) if index < len(row) else "")) // 2 if centered else 1) + (cell_content := str(row[index]) if index < len(row) else "") + pad_char * (-(-padding // 2) if centered else (column_width - len(cell_content)) - 1)) for index, column_width in enumerate(list(max(len(str(item)) + 2 for item in list((row[index] if len(row) > index else "") for row in (rows + [labels] if labels else rows))) for index in range(max(len(row) for row in (rows + [labels] if labels else rows)))))) + end) for start, mid, end, pad_char, row in itertools.chain(([("┌", "┬", "┐", "─", []), ("│", "│", "│", " ", labels), ("├", "┼", "┤", "─", [])] if labels else [("┌", "┬", "┐", "─", [])]), (("│", "│", "│", " ", row) for row in rows), [("└", "┴", "┘", "─", [])]))

def make_table_pretty(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    return "\n".join(
        (
            start
            + mid.join(
            (
                pad_char * ((padding := column_width - len(str(row[index]) if index < len(row) else "")) // 2 if centered else 1)
                + (cell_content := str(row[index]) if index < len(row) else "")
                + pad_char * (-(-padding // 2) if centered else (column_width - len(cell_content)) - 1)
            ) for index, column_width in enumerate(
                list(
                    max(
                        len(str(item)) + 2 for item in list(
                            (row[index] if len(row) > index else "") for row in (rows + [labels] if labels else rows)
                        )
                    ) for index in range(max(len(row) for row in (rows + [labels] if labels else rows))))
            )
        )
            + end
        ) for start, mid, end, pad_char, row in itertools.chain(([("┌", "┬", "┐", "─", []), ("│", "│", "│", " ", labels), ("├", "┼", "┤", "─", [])] if labels else [("┌", "┬", "┐", "─", [])]), (("│", "│", "│", " ", row) for row in rows), [("└", "┴", "┘", "─", [])]))