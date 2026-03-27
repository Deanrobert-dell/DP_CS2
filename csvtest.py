"""Csv
Take income from Elijah's list and append it to a csv file
Take expenses and import them, keep them in categories
FOR each item IN expense_items:
    rows.APPEND({
      date: item.date,
      type: "expense",
      description: item. *blank*,
      category: item.category ,
Match each income and expense with date
"""

def csv():
    income_items = []
    expense_items = []
    rows = []

    # Append income items to the CSV rows
    for item in income_items:
        rows.append({
            "date": item.date,
            "type": "income",
            "description": item.description,
            "category": item.category,
        })

    # Append expense items to the CSV rows
    for item in expense_items:
        rows.append({
            "date": item.date,
            "type": "expense",
            "description": item.description,
            "category": item.category,
        })

    # Match each income and expense with date
    for income in income_items:
        for expense in expense_items:
            if income.date == expense.date:
                rows.append({
                    "date": income.date,
                    "type": "match",
                    "description": f"Matched income: {income.description} with expense: {expense.description}",
                    "category": income.category,
                })

    return rows