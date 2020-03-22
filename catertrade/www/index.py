from __future__ import unicode_literals
import frappe

no_cache = True

def get_context(context):
	context["parent_categories"] = frappe.db.sql("""select name, route, is_group from `tabItem Group` where show_in_website=1 and parent_item_group='All Item Groups' """, as_dict=True)

	group_categories = frappe.db.sql("""select name from `tabItem Group` where is_group and show_in_website=1 and parent_item_group='All Item Groups' """, as_list=True)
	group_categories = [ child_category[0] for child_category in group_categories]

	child_categories = []
	for child in group_categories:
		data = frappe.db.sql("""select name, route from `tabItem Group` where show_in_website=1 and parent_item_group="{parent}" """.format(parent=child),as_dict=True)
		data_dict = {
			child : data
		}
		child_categories.append(data_dict)

	context["child_categories"]	= child_categories

	context["banners"] = frappe.db.sql("""select heading, description, item_group_route, attach_image_5 from `tabWebsite Homepage Banners`""",as_dict=True)

	context["banner_section"] = frappe.db.sql("""select heading, item_route, attach_image_5 from `tabWebsite Homepage Banner`""",as_dict=True)
	
	context["mid_page_banners"] = frappe.db.sql("""select heading, item_group_mid_route, attach_image_5 from `tabWebsite Homepage Mid Banners`""", as_dict=True)

	left_banner = frappe.db.sql("""select * from `tabSingles` where doctype="Website Homepage" """, as_dict=True)

	mid_page_left_banner = {}

	for dicts in left_banner:
			if dicts.field == "heading":
				mid_page_left_banner["heading"] = dicts.value
			elif dicts.field =="description":
				mid_page_left_banner["description"] = dicts.value
			elif dicts.field == "left_banner_route":
				mid_page_left_banner["left_banner_route"] = dicts.value
			elif dicts.field == "mid_page_left_banner":
				mid_page_left_banner["mid_page_left_banner"] = dicts.value

	context["mid_page_left_banner"] = mid_page_left_banner

	item_groups_homepage = frappe.db.sql("""select item_groups from `tabWebsite Homepage Item Groups` order by idx""", as_list=True)

	item_groups_homepage = [ item_group_child[0] for item_group_child in item_groups_homepage]

	context["deals"] = frappe.db.sql("""select item_name, thumbnail, route from `tabItem` where item_group='{}' limit 6""".format(item_groups_homepage[0]),as_dict=True)	

	context["featured"] = frappe.db.sql("""select item_name, thumbnail, route from `tabItem` where item_group='{}' limit 6""".format(item_groups_homepage[1]),as_dict=True)	
	
 	context["latest"] = frappe.db.sql("""select item_name, thumbnail, route from `tabItem` where item_group='{}' limit 4""".format(item_groups_homepage[2]),as_dict=True)	
	
 	context["end"] = frappe.db.sql("""select item_name, thumbnail, route from `tabItem` where item_group='{}' limit 3""".format(item_groups_homepage[3]),as_dict=True)	
	
 	context["left_banners"] = frappe.db.sql("""select heading, left_item_group_mid_route, attach_image_5 from `tabWebsite Homepage Left Banners`""",as_dict=True)

 	return context