import frappe
import json 
@frappe.whitelist()
def cancel_invoices(names, status):
    if not frappe.has_permission("Sales Invoice", "write"):
        frappe.throw(_("Not permitted"), frappe.PermissionError)

    names = json.loads(names)
    for name in names:
        si = frappe.get_doc("Sales Invoice", name)
        if si.docstatus == 1:
            si.cancel()
    frappe.local.message_log = []