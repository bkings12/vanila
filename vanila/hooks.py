app_name = "vanila"
app_title = "Vanila"
app_publisher = "unganisha"
app_description = "vanilla css"
app_email = "info@unganishanetworks.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/vanila/css/vanila.css"
# app_include_js = "/assets/vanila/js/vanila.js"

# include js, css files in header of web templat
#web_include_css = "https://fonts.googleapis.com"
#web_include_css = "https://fonts.gstatic.com"
#web_include_css = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.10.0/css/all.min.css"
#web_include_css = "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.4.1/font/bootstrap-icons.css"
#web_include_css = "/assets/vanila/css/style.css"
#web_include_css = "/assets/vanila/css/bootstrap.min.css"
#web_include_css = "/assets/vanila/lib/tempusdominus/css/tempusdominus-bootstrap-4.min.css"
#web_include_css = "/assets/vanila/lib/owlcarousel/assets/owl.carousel.min.css"
#web_include_css = "/assets/vanila/lib/animate/animate.min.css"
#web_include_css = "/assets/vanila/css/bootstrap.min.css"
#web_include_css = "/assets/vanila/css/bootstrap.min.css"
#
#
#
#web_include_js = "https://code.jquery.com/jquery-3.4.1.min.js"
#web_include_js = "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
#web_include_js = "/assets/vanila/lib/wow/wow.min.js"
#web_include_js = "/assets/vanila/lib/easing/easing.min.js"
#web_include_js = "/assets/vanila/lib/waypoints/waypoints.min.js"
#web_include_js = "/assets/vanila/lib/counterup/counterup.min.js"
#web_include_js = "/assets/vanila/lib/owlcarousel/owl.carousel.min.js"
#web_include_js = "/assets/vanila/lib/tempusdominus/js/moment.min.js"
#web_include_js = "/assets/vanila/lib/tempusdominus/js/moment-timezone.min.js"
#web_include_js = "/assets/vanila/lib/tempusdominus/js/tempusdominus-bootstrap-4.min.js"
#web_include_js = "/assets/vanila/js/main.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "vanila/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "vanila/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "vanila.utils.jinja_methods",
# 	"filters": "vanila.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "vanila.install.before_install"
# after_install = "vanila.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "vanila.uninstall.before_uninstall"
# after_uninstall = "vanila.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "vanila.utils.before_app_install"
# after_app_install = "vanila.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "vanila.utils.before_app_uninstall"
# after_app_uninstall = "vanila.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "vanila.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"vanila.tasks.all"
# 	],
# 	"daily": [
# 		"vanila.tasks.daily"
# 	],
# 	"hourly": [
# 		"vanila.tasks.hourly"
# 	],
# 	"weekly": [
# 		"vanila.tasks.weekly"
# 	],
# 	"monthly": [
# 		"vanila.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "vanila.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "vanila.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "vanila.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["vanila.utils.before_request"]
# after_request = ["vanila.utils.after_request"]

# Job Events
# ----------
# before_job = ["vanila.utils.before_job"]
# after_job = ["vanila.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"vanila.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

