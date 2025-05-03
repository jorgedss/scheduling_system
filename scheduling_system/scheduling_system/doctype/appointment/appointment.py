# Copyright (c) 2025, Jorge Souza and contributors
# For license information, please see license.txt

from frappe.utils import now as _datetime
import frappe
from frappe.model.document import Document
from frappe.utils import add_to_date
from frappe.utils.data import format_datetime


class Appointment(Document):
	def before_save(self):
			self.set_end_date()
			self.check_schedule_conflict()

	def validate(self):
		if self.start_date and self.start_date < _datetime():
			frappe.throw(
                frappe._("Start datetime cannot be in the past."),
                title=frappe._("Invalid datetime")
            )

	def set_end_date(self):
		if self.start_date and self.duration:
			h, m, s = map(int, self.duration.split(':'))
			self.end_date = add_to_date(self.start_date, hours=h, minutes=m, seconds=s)
		else:
			self.end_date = None

	def check_schedule_conflict(self):
		if not (self.seller and self.start_date and self.end_date):
			return

		conflicts = frappe.get_list(
			"Appointment",
			filters={
				"seller": self.seller,
				"start_date": ["<", self.end_date],
				"end_date": [">", self.start_date],
				"name": ["!=", self.name]  
			},
			fields=["start_date", "end_date"],
			order_by="start_date asc",
			limit=1
		)

		if conflicts:
			conflict_dict = conflicts[0]
			start = format_datetime(conflict_dict["start_date"])
			end = format_datetime(conflict_dict["end_date"])

			frappe.throw(frappe._("This seller has an appointment from {0} to {1}. Please choose another time.").format(start, end),
									title=frappe._("Scheduling conflict"))