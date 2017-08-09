# -*- coding: utf-8 -*-
{
    'name': 'Force Delete Bank Statement',
    'category': 'Accounting',
    'author': 'Jose M. Coronado',
    'summary': 'Custom',
    'version': '1.0',
    'description': """
**MAIN COMPONENT: account_cancel**
This custom module for Odoo Enterprise (Online/On Premise) force deletes a bank statement.
It uses Odoo methods such as 'button_draft' and 'button_cancel_reconciliation' for a greater
degree of sustainability. For this to function correctly, all journals related to the bank statement
should allow cancellation of journal entries. This will not work on bank statements that have been
reconciled with journal items before the company's lock date (i.e. if the fiscal period is closed).

**IMPACT ON FINANCIALS WARNING**
This custom module does delete journal entries that are made external to the Bank Reconciliation (e.g.
Payments, etc.). It only deletes journal entries that stem from the bank reconciliation process (black
lines),in other words those that create a journal entry on reconiliation of a bank statement line.

ONLY USE IF ABSOLUTELY NECESSARY - INSTALLATION AT USERS OWN RISK - AUTHOR OF MODULE DOES NOT CLAIM ANY
RESPONSIBILITY FOR DELETION OF ENTRIES, OR ANY ACCOUNTING RELATED ISSUES STEMMING FROM THIS MODULE.
        """,
    'depends': ['base','account_accountant','account_cancel'],
    'data': [
        'data/actions_views.xml',
    ],
    'installable': True,
}
